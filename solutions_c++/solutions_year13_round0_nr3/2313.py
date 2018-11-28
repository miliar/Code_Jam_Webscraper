#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int T = 0;
long long A = 0, B = 0;

class Number : public vector <int> {
public:
    Number() : vector <int>() {};
    Number(long x);
    Number(const Number &n) : vector <int>(n) {};

    bool isPalindrome();
    Number nextPalindrome();
    Number square();
    void print(ostream &o) const;

    bool operator==(const Number &n) const;

    friend ostream &operator<<(ostream &o, const Number &n);
};

bool Number::operator==(const Number &n) const
{
    if (size() != n.size())
        return false;
    for (int i = 0; i < size(); ++i) {
        if (at(i) != n[i]) {
            return false;
        }
    }
    return true;
}

ostream &operator<<(ostream &o, const Number &n)
{
    n.print(o);
    return o;
}

Number::Number(long x)
{
    while (x > 0) {
        push_back(x % 10);
        x /= 10;
    }
}

bool Number::isPalindrome()
{
    int n = size();
    for (int i = 0; i <= n / 2; ++i) {
        if (at(i) != at(n - 1 - i)) {
            return false;
        }
    }
    return true;
}

Number Number::nextPalindrome()
{
    Number ans(*this);
    int n = size();
    int mid = n / 2; // n=5 -> mid=2, n=6 -> mid=3
    bool inc = false;
    if (!isPalindrome()) {
        for (int i = (n - 1) / 2 + 1 /* n=5 -> 3, n=6 -> 3 */; i < n; ++i) {
            if (at(i) < at(n - 1 - i)) {
                inc = true;
                break;
            }
        }
    } else {
        inc = true;
    }
    if (inc) {
        int carry = 1;
        while (carry && mid < n) {
            ans.at(mid) += carry;
            carry = ans.at(mid) / 10;
            ans.at(mid) %= 10;
            ++mid;
        }
        if (mid == n && carry) {
            ans.push_back(1);
          //  ans.print();
        }
    }
    n = ans.size(); // could have changed
    for (int i = n / 2 /* n=5 -> 3, n=6 -> 3 */; i < n; ++i) {
        //cout << "> " << n - 1 - i << ", " << i << '\n';
        ans.at(n - 1 - i) = ans.at(i);
    }
    return ans;
}

Number Number::square()
{
    int n = size();
    int* result = new int [2 * n];
    for (int i = 0; i < 2 * n; ++i) {
        result[i] = 0;
    }
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            result[i + j] += at(i) * at(j);
        }
    }
    for (int i = 0; i < 2 * n - 1; ++i) {
        result[i + 1] += result[i] / 10;
        result[i] %= 10;
    }
    int last;
    for (last = 2 * n - 1; last >= 0 && result[last] == 0; --last) ;
    Number answ;
    for (int i = 0; i <= last; ++i) {
        answ.push_back(result[i]);
    }
    delete [] result;
    return answ;
}

void Number::print(ostream &o) const
{
    for (int i = size() - 1; i >= 0; --i) {
        o << at(i);
    }
}

int main()
{
    cin >> T;
    for (int testCase = 1; testCase <= T; ++testCase) {
        cin >> A >> B;
        // cout << A << ' ' << B << '\n';
        Number start = ceil(sqrt((long double) A)), end = floor(sqrt((long double) B));

        // cout << start << ' ' << end << '\n';
        
        if (!start.isPalindrome()) {
            start = start.nextPalindrome();
        }
        end = end.nextPalindrome();

        // cout << start << ' ' << end << '\n';
        int count = 0;
        while (start != end) {
            // cout << start << ' ' << start.square() << ' ' << start.square().isPalindrome() << '\n';
            count += start.square().isPalindrome();
            start = start.nextPalindrome();
        }
        cout << "Case #" << testCase << ": " << count << '\n';
    }
    return 0;
}