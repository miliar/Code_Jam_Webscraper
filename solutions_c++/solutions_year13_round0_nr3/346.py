#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <cassert>
using namespace std;





#define TABLECNT(x) (sizeof(x) / sizeof(x[0]))

class BN
{
    const static unsigned int len = 11;
    unsigned long long nums[len];
    const static unsigned long long maxSingleNum = 0x00000000ffffffff;

public:

    BN(unsigned long long x = 0)
    {
        for (int i = 0; i < sizeof(nums) / sizeof(nums[0]) - 1; i++) {
            nums[i] = 0;
        }

        nums[sizeof(nums) / sizeof(nums[0]) - 1] = x;
    }

    BN(vector<char> digits)
    {
        fillWithDigits(digits);
    }

    void inline fillWithDigits(vector<char> digits)
    {
        clear();
        for (vector<char>::iterator it = digits.begin(); it != digits.end(); it++) {
            int digit = (int) *it;
            //if (digit < '0' || digit > '9')
            //    break;
            multiplyBy(10);
            /* TODO: it would faster to do this addition in-place */
            //bn = bn + (digit - '0');
            add(digit);
        }
    }

    void add(const BN &x)
    {
        unsigned long long carry = 0LL;

        for (int i = TABLECNT(nums) - 1; i >= 0; --i)
        {
            unsigned long long tmp = x.nums[i] + nums[i] + carry;
            carry = (tmp & 0xffffffff00000000ull) > 8;
            nums[i] = tmp & 0x00000000ffffffff;
        }

        // if carry > 0 --> overflow
        assert(carry == 0);
    }

    void decrement() /* Caution: assumes that *this>0 */
    {
        for (int i = TABLECNT(nums) - 1; i >= 0; --i)
        {
            if (nums[i] == 0x0000000000000000) {
                nums[i] = 0x00000000ffffffff;
            } else {
                nums[i]--;
                break;
            }
        }
    }

    friend BN operator+(const BN &x, const BN &y)
    {
        // TODO: mozna zmniejszyc ilosc kodu uzywajac ::add()

        unsigned long long carry = 0LL;
        BN newBN;

        for (int i = TABLECNT(newBN.nums) - 1; i >= 0; --i)
        {
            unsigned long long tmp = x.nums[i] + y.nums[i] + carry;
            carry = (tmp & 0xffffffff00000000ull) > 8;
            newBN.nums[i] = tmp & 0x00000000ffffffff;
        }

        // if carry > 0 --> overflow
        assert(carry == 0);

        return newBN;
    }

    friend BN operator*(const BN &x, const BN &y)
    {
        BN result = 0;
        multiply(result, x, y);
        return result;
        //BN toAdd = 0;
        //int shift = 0;
        //for (int i = TABLECNT(result.nums) - 1; i >= 0; --i) {
        //    toAdd = y;
        //    toAdd.multiplyBy(x.nums[i]);
        //    toAdd.shiftDigitsLeft(shift++);
        //    result = result + toAdd;
        //}
        //return result;
    }

    static inline void multiply(BN &result, const BN &x, const BN &y)
    {
        result = 0;
        BN toAdd = 0;
        int shift = 0;
        for (int i = TABLECNT(result.nums) - 1; i >= 0; --i) {
            toAdd = y;
            toAdd.multiplyBy(x.nums[i]);
            toAdd.shiftDigitsLeft(shift++);
            result = result + toAdd;
        }
    }

    void shiftDigitsLeft(int howMany)
    {
        int i;
        for (i = 0; i < TABLECNT(nums) - howMany; i++)
            nums[i] = nums[i + howMany];
        for (; i < TABLECNT(nums); i++)
            nums[i] = 0;
    }

    unsigned long long divideBy(unsigned long long what)
    {
        int i = 0;
        unsigned long long dv = 0, carry = 0;

        while (i < TABLECNT(nums)) {
            dv = (carry << 32) | nums[i];
            if (dv < what) {
                if (TABLECNT(nums) - 1 == i) {
                    nums[i] = 0;
                    return dv;
                } else {
                    nums[i] = 0;
                    dv = (dv << 32) | nums[++i];
                }
            }
            nums[i] = dv / what;
            carry = dv % what;
            ++i;
        }
        return carry;
    }

    void multiplyBy(unsigned long long what)
    {
        int i = 0;
        unsigned long long carry = 0;

        for (i = TABLECNT(nums) - 1; i >= 0; i--) {
            unsigned long long tmp = (nums[i] * what) + carry;
            nums[i] = tmp & 0x00000000ffffffff;
            carry = tmp >> 32;
        }

        // if carry > 0 --> overflow
        assert(carry == 0);
    }

    bool zero()
    {
        for (int i = 0; i < TABLECNT(nums); i++)
            if (nums[i] != 0)
                return false;
        return true;
    }

    BN pow(unsigned long long exponent)
    {
        /* TODO: lots of unneeded copying */
        vector<unsigned long long> v;
        while (exponent > 0) {
            v.push_back(exponent);
            if (0 == exponent % 2)
                exponent = exponent / 2;
            else
                exponent--;
        }

        reverse(v.begin(), v.end());

        BN result = *this;

        for (int i = 1; i < v.size(); i++) {
            if (v[i] - v[i-1] == 1)
                result = result * (*this);
            else
                result = result * result;
        }

        return result;
    }

    void clear()
    {
        fill(nums, nums + len, 0);
    }

    BN sqrt()
    {
        BN a = 0;
        BN b = *this;
        BN cur, mul;

        while (a < b) {
            // TODO: maybe a + (b - a)/2 would be better, but it requires
            // operator-() implementation
            //BN cur = a + b;
            
            cur = a;
            cur.add(b);
            cur.divideBy(2);

            multiply(mul, cur, cur);

            //cout << "a=" << a << " b=" << b << " cur=" << cur << endl;
            if (mul > *this) {
                b = cur;
                b.decrement();
            } else
            if (mul < *this) {
                a = cur + 1;
            } else
                return cur;
        }
        return a;
    }

    friend istream & operator>>(istream & in, BN & bn)
    {
        bn.clear();

        int digit; 
        do {
            digit = in.get();
        } while (digit < '0' || digit > '9');

        in.unget();

        while (true) {
            int digit = in.get();
            if (digit < '0' || digit > '9')
                break;
            bn.multiplyBy(10);
            /* TODO: it would faster to do this addition in-place */
            bn = bn + (digit - '0');
        }
        in.unget();
        return in;
    }

    friend ostream & operator<<(ostream & out, const BN & bn)
    {
#if 0
        out << hex;
        for (int i = 0; i < sizeof(bn.nums) / sizeof(bn.nums[0]); i++) {
            out << bn.nums[i] << " ";
        }
        out << dec;
#endif

        //BN copy(bn);
        vector<char> digits;
        bn.getDigits(digits);

        //while (! copy.zero()) {
        //    digits.push_back(copy.divideBy(10));
        //}

        for (vector<char>::const_reverse_iterator it = digits.rbegin(); it != digits.rend(); it++) {
            out << (int) *it;
        }

        return out;
    }

    void getDigits(vector<char> &where) const
    {
        BN copy(*this);

        while (! copy.zero()) {
            where.push_back(copy.divideBy(10));
        }
    }

    friend bool operator<(const BN &a, const BN &b)
    {
        for (int i = 0; i < TABLECNT(a.nums); i++) {
            if (a.nums[i] < b.nums[i])
                return true;
            if (a.nums[i] > b.nums[i])
                return false;
        }
        return false;
    }

    friend bool operator==(const BN &a, const BN &b)
    {
        for (int i = 0; i < TABLECNT(a.nums); i++) {
            if (a.nums[i] < b.nums[i])
                return false;
            if (a.nums[i] > b.nums[i])
                return false;
        }
        return true;
    }

    friend bool operator>(const BN &a, const BN &b)
    {
        /* TODO: in case of slowness: direct definition would be faster */
        return !(a < b) && !(a == b);
    }

    const static int maxShift = (sizeof(maxSingleNum) / 2) * 8 - 1;

    /* iterates from most important bits to least important */
    class bit_iterator {
        BN *parent;
        int n, m; /* n - points to the byte, m - points to the bit */   
    
    public:
        bit_iterator(BN *parent, int n = 0, int m = 0) : parent(parent), n(n), m(m)
        { }

        friend bool operator==(const bit_iterator &a, const bit_iterator &b) {
            return a.parent == b.parent && a.n == b.n && a.m == b.m;
        }

        friend bool operator!=(const bit_iterator &a, const bit_iterator &b) {
            return ! (a == b);
        }

        bit_iterator & operator++() {
            if (m > 0)
                m--;
            else {
                n++;
                m = maxShift;
            }
            return *this;
        }

       bool is_set() {
           return (parent->nums[n] & (1 << m)) != 0;
       }

       bool operator*() {
           return is_set();
       }

       void set(bool value) {
            parent->nums[n] = (parent->nums[n] & ~(1ull << m)) | ((value ? 1ull : 0ull) << m);
       }

       friend int operator-(const bit_iterator &a, const bit_iterator &b) {
           if (a.n == b.n) {
                return b.m - a.m;
           } else {
                return (a.n - b.n - 1) * (maxShift + 1) + (maxShift - a.m) + b.m + 1;
           }
       }
    };

    friend class bit_iterator;

    /* TODO: return reference, keep inner end() iterator, etc */
    bit_iterator end() {
        return bit_iterator(this, TABLECNT(nums), maxShift);
    }

    bit_iterator begin() {
        int n = 0;
        while (nums[n] == 0 && n < (TABLECNT(nums) - 1))
            n++;

        int m = maxShift;
        while (m > 0 && (nums[n] & (1 << m)) == 0)
            m--;

        return bit_iterator(this, n, m);
    }

    template<typename T>
    static BN fromBitSequence(T from, T to) {
        int size = to - from;

        BN newBN;
        newBN.clear();

        int n = (TABLECNT(newBN.nums) - 1) - (size / (maxShift + 1));

        if (size % (maxShift + 1) == 0) {
            n++;
        }

        int m = size % (maxShift + 1) - 1;

        bit_iterator it(&newBN, n, m);

        for (T i = from; i != to; ++i, ++it) {
            it.set(*i);
        }

        return newBN;
    }

};







template<typename T>
inline void pv(const vector<T> & v, string separator = " ")
{
    for (typename vector<T>::const_iterator it = v.begin(); it != v.end(); it++) {
        cout << *it << separator;
    }

    //cout << endl;
}

/* jesli niepazysta liczba cyft i w srodku 1 zwraca true */
bool next_palindrome(const vector<char> & src, vector<char> & dst)
{
    //dst.clear();

    static vector<char> left, right;
    static bool init = true;
    if (init) {
        init = false;

        left.reserve(500000);
        right.reserve(500000);
    }

    left.clear();
    right.clear();

    int middle = -1;

    copy(src.begin(), src.begin() + src.size() / 2, back_inserter(left));
    copy(src.rbegin(), src.rbegin() + src.size() / 2, back_inserter(right));

    bool even = src.size() % 2 == 0;

    if (! even)
        middle = src[src.size() / 2];

    while (! equal(left.begin(), left.end(), right.begin()))
    {
        if (lexicographical_compare(left.rbegin(), left.rend(), right.rbegin(), right.rend()))
        {
            bool all_nines = true;

            if (! even) {
                if (middle < 1) {
                    middle++;
                    all_nines = false;
                    copy(left.begin(), left.end(), right.begin());
                    continue;
                } else {
                    middle = 0;
                }
            }

            for (vector<char>::reverse_iterator it = left.rbegin(); it != left.rend(); it++)
            {
                if (*it < 1)
                {
                    (*it)++;
                    all_nines = false;
                    break;
                } else {
                    *it = 0;
                }
            }

            copy(left.begin(), left.end(), right.begin());

            //if (all_nines) {
            //    cout << "BUM, 9tki do konca " << endl;
            //}
        } else {
            copy(left.begin(), left.end(), right.begin());
        }
    }

    copy(left.begin(), left.end(), back_inserter(dst));
    if (! even) {
        dst.push_back(middle);
    }
    copy(right.rbegin(), right.rend(), back_inserter(dst));

    return !even && middle == 1;

    //cout << "middle: " << middle << endl;

    //cout << "left: ";
    //pv(left);

    //cout << "right: ";
    //pv(right);
}

inline bool is_palindrome(const vector<char> & v)
{
    return equal(v.begin(), v.begin() + v.size() / 2, v.rbegin());
}

inline void to_vector(unsigned long long x, vector<char> & dest)
{
    dest.clear();
    while (x > 0)
    {
        dest.push_back(x % 10);
        x /= 10;
    }
    reverse(dest.begin(), dest.end());
}

void naive_next_palindrome(const vector<char> & src, vector<char> & dst)
{
    unsigned long long x = 0;
    //dst.clear();

    for (vector<char>::const_iterator it = src.begin(); it != src.end(); it++)
    {
        x = (x * 10) + *it;
    }

    to_vector(x, dst);

    while (! is_palindrome(dst))
    {
        x++;
        to_vector(x, dst);
    }
}

inline void increment(vector<char> & v)
{
    for (vector<char>::reverse_iterator it = v.rbegin(); it != v.rend(); it++) {
        if (*it < 1) {
            (*it)++;
            return;
        } else
            *it = 0;
    }
    v.insert(v.begin(), 1);
}

int main()
{
    int hm;
    //scanf("%d", &hm);

    vector<char> digits, dest_digits, digits2, digits_copy, digits_copy2;
    digits.reserve(1000000);
    dest_digits.reserve(1000001);
    digits2.reserve(1000001);
    digits_copy.reserve(1000000);
    digits_copy2.reserve(1000000);

    //getchar();


    vector<BN> cache;
    cache.reserve(100000);

    //digits.push_back(1);

    BN a, b;

    a = 1;
    b = 1;

    /* 10 ^ 50 */
    b.multiplyBy(10000000000);
    b.multiplyBy(10000000000);
    b.multiplyBy(10000000000);
    b.multiplyBy(10000000000);
    b.multiplyBy(10000000000);


    b.multiplyBy(10000000000);
    b.multiplyBy(10000000000);
    b.multiplyBy(10000000000);
    b.multiplyBy(10000000000);
    b.multiplyBy(10000000000);

    b.add(2);


    //cin >> a >> b;

    BN cur = a, cur2;
    BN curSquare;

    cur = cur.sqrt();
    cur.decrement();

    digits.clear();
    cur.getDigits(digits);

    vector<char> better_digits;
    better_digits.push_back(1);
    for (int j = 1; j < digits.size(); j++) {
        better_digits.push_back(0);
    }

    digits.swap(better_digits);
    
    unsigned long long counter = 0;

    //cout << "digs "; pv(digits); cout << endl;

    while (true) {
        //cur.getDigits(digits);
        bool one_in_middle = next_palindrome(digits, dest_digits);

        digits.swap(dest_digits);

        //cout << "digs "; pv(digits, ""); cout << endl;

        dest_digits.clear();

        //increment(dest_digits);
        //dest_digits.swap(dest_digits2);
        //dest_digits.clear();

        //next_palindrome(dest_digits2, dest_digits);
        //counter++;



        if (one_in_middle && digits.size() > 1) {
            digits[digits.size() / 2] = 2;
            cur.fillWithDigits(digits);
            BN::multiply(curSquare, cur, cur);
            if ((curSquare > a || curSquare == a) && (curSquare < b || curSquare == b)) {
                digits2.clear();
                curSquare.getDigits(digits2);
                if (is_palindrome(digits2)) {
                    //cout << "YEST " << cur << " ZZZ 1" << endl;
                    cache.push_back(curSquare);
                    counter++;
                }
            }
            digits[digits.size() / 2] = 1;
        }

        cur.fillWithDigits(digits);

        digits_copy = digits;
        digits_copy2 = digits;

        increment(digits);

        if (digits.size() > digits_copy.size()) {
            fill(digits_copy.begin(), digits_copy.end(), 0);
            digits_copy[0] = 2;
            digits_copy[digits_copy.size() - 1] = 2;


            cur2.fillWithDigits(digits_copy);
            BN::multiply(curSquare, cur2, cur2);
            if ((curSquare > a || curSquare == a) && (curSquare < b || curSquare == b)) {
                digits2.clear();
                curSquare.getDigits(digits2);
                if (is_palindrome(digits2)) {
                    //cout << "YEST " << cur2 << " ZZZ 2" << endl;
                    cache.push_back(curSquare);
                    counter++;
                }
            }


            if (digits_copy.size() % 2 == 1) {
                digits_copy[digits_copy.size() / 2]++;

                cur2.fillWithDigits(digits_copy);
                BN::multiply(curSquare, cur2, cur2);
                if ((curSquare > a || curSquare == a) && (curSquare < b || curSquare == b)) {
                    digits2.clear();
                    curSquare.getDigits(digits2);
                    if (is_palindrome(digits2)) {
                        //cout << "YEST " << cur2 << " ZZZ 3" << endl;
                        cache.push_back(curSquare);
                        counter++;
                    }
                }
            }
        }

        BN::multiply(curSquare, cur, cur);

        //cout << "square " << curSquare << endl;

        if (curSquare < a) // Chyba sie moze zdazyc, sqrt jest niedoskonale
            continue;

        if (curSquare > b)
            break;

        digits2.clear();
        curSquare.getDigits(digits2);

        if (is_palindrome(digits2)) {
            //cout << "EEE YEST "; pv(digits2, ""); cout << endl;
            //cout << "YEST " << cur << endl;
            cache.push_back(curSquare);
            counter++;
        }

    }


    sort(cache.begin(), cache.end());

#if 0
    for (vector<BN>::iterator it = cache.begin(); it != cache.end(); it++) {
        cout << *it << " " << it->sqrt() << endl;
    }
#endif
    

    cerr << "ready" << endl;

    cin >> hm;

    for (int i = 0; i < hm; i++)
    {
        BN x, y;
        cin >> x >> y;

        vector<BN>::iterator a = lower_bound(cache.begin(), cache.end(), x);
        vector<BN>::iterator b = upper_bound(cache.begin(), cache.end(), y);



        cout << "Case #" << i + 1 << ": " << static_cast<unsigned long long>(b - a) << endl;
    }




#if 0
        digits.push_back(0);

        dest_digits.clear();
        //dest_digits2.clear();

        unsigned long long counter = 1;

        next_palindrome(digits, dest_digits);

        cout << "Z "; pv(digits, ""); cout << " jest "; pv(dest_digits, ""); cout << endl;

        while (dest_digits.size() == digits.size()) {

            cout << "a "; pv(dest_digits, ""); cout << endl;
            
            increment(dest_digits);
            dest_digits.swap(dest_digits2);
            dest_digits.clear();

            next_palindrome(dest_digits2, dest_digits);
            counter++;
        }

        cout << "Between ";
        pv(digits, "");
        cout << " and ";
        pv(digits, "");
        cout << "0 : " << endl;

        //cout << counter << endl;
        cout << "Ratio: " << counter << "/" << (unsigned long long)(pow(10, digits.size()) - pow(10, digits.size() - 1)) << endl;
        cout << "Ratio (as float): " << ((double) counter) / (pow(10, digits.size()) - pow(10, digits.size() - 1)) << endl;

        cout << endl;
        
#endif
  //      while (true)
  //      {
  //          int c = getchar();
  //          if (c == 10 || c == 13)
  //              break;
  //          c -= '0';
  //          digits.push_back(c);
  //      }

        //pv(digits);

        //cout << "raw input ";
        //pv(digits);

        //increment(digits);

        //cout << "inc input ";
        //pv(digits);

        //naive_next_palindrome(digits, dest_digits2);
//        next_palindrome(digits, dest_digits);
//
//        pv(dest_digits, "");
//
//        //if (! equal(dest_digits.begin(), dest_digits.end(), dest_digits2.begin()))
//        //{
//        //    cout << "difference for " << endl;
//        //    pv(dest_digits2);
//        //    pv(dest_digits);
//        //} else {
//        //    cout << "equal" << endl;
//        //    pv(dest_digits2);
//        //    pv(dest_digits);
//        //}
//
//        digits.clear();
//        dest_digits.clear();
//        //dest_digits2.clear();
    return 0;
}
