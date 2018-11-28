// This has got to be the shittiest solution I've ever written in my entire life!!!
#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <utility>
#include <sstream>
#include <boost/cstdint.hpp>
#include <boost/lexical_cast.hpp>
#include <cstring>

#define log false && cerr
//#define log cerr
#define logp cerr 

using namespace std;

struct NumComparator {
    bool operator ()(const std::string& a, const std::string& b) {
      if (a.length() < b.length()) return true;
      if (a.length() > b.length()) return false;
      if (a < b) return true;
      return false; 
    }
};

typedef vector<string> numset;
numset tab;

bool isPalindrome(const char* s, int len) {
    for (int l = 0, r = len - 1; l < r; l++, r--)
        if (s[l] != s[r])
            return false;

    return true;
}

static inline uint32_t fastlog2(const uint32_t x) {
      uint32_t y;
      asm ( "\tbsr %1, %0\n"
             : "=r"(y)
             : "r" (x)
      );
      return y;
}

char binLUP[] = { '0', '1' };

void computePaliBaseEven(int seed, char *s) {
    int digits = fastlog2(seed) + 1;
    for (int i = 0; i < digits; ++i, seed >>= 1)
        s[digits - 1 - i] = s[digits + i] = binLUP[seed & 1];
    s[2*digits] = 0;
}

void computePaliBaseOdd(int seed, char *s, int middle) {
    int digits = fastlog2(seed) + 1;
    for (int i = 0; i < digits; ++i, seed >>= 1)
        s[digits - 1 - i] = s[digits + 1 + i] = binLUP[seed & 1];
    s[digits] = binLUP[middle & 1];
    s[2*digits+1] = 0;
}

struct BigNum {
    static const int BASE = 1e8;
    static const int BASE_LOG = 8;

    long a[20];
    int digits;

    BigNum() {
        digits = 0;
        memset(a, 0, sizeof(a));
    }

    BigNum(const char *s) {
        digits = 0;
        int len = strlen(s);
        long d = 0, pw = 1;
        for (int i = 0; i < len; ++i) {
            int c = s[len - i - 1] - '0';
            d += c * pw;

            pw *= 10;

            if (i % BASE_LOG == BASE_LOG - 1) {
                a[digits++] = d;
                d = 0;
                pw = 1;
            }
        }

        if (d)
            a[digits++] = d;
    }

    int toString(char *s) {
        int len = 0;
        int d;
        for (int i = 0; i < digits - 1; ++i) {
            d = a[i];
            for (int j = 0; j < BASE_LOG; ++j) {
               s[len++] = '0' + d % 10; 
               d /= 10;
            }
        }

        d = a[digits - 1];
        for (int j = 0; d; ++j) {
           s[len++] = '0' + d % 10; 
           d /= 10;
           log << "D is: " << d << endl;
        }

        s[len] = 0;
        return len;
    }

    string toString() {
        stringstream ss;
        ss << "D: " << digits << endl;
        for (int i = 0; i < digits; ++i)
            ss << a[i] << " ";
        ss << endl;
        return ss.str();
    }

    static void mul(const BigNum& a, const BigNum& b, BigNum& c) {
        for (int i = 0; i < a.digits; ++i) {
            for (int j = 0; j < b.digits; ++j) {
                c.a[i + j] += a.a[i] * b.a[j];
                c.a[i + j + 1] += c.a[i + j] / BASE;
                c.a[i + j] %= BASE; 
            }
        }

        c.digits = a.digits + b.digits + 1;
        while (c.a[c.digits - 1] == 0)
            --c.digits;
    }
};

void checkBase(const char *s) {
    log << "Pali to check: " << s << endl;
    BigNum pali(s);
    log << "Pali debug str: " << pali.toString() << endl;

    char test[1000];
    pali.toString(test);
    log << "Pali to string: " << test << endl;

    BigNum sqr;
    BigNum::mul(pali, pali, sqr);
    log << "sqr debug str: " << sqr.toString() << endl;

    char s2[1000];
    int digits = sqr.toString(s2);
    log << "Check palindrome: " << s2 << endl;
    if (isPalindrome(s2, digits)) {
        //cout << s2 << endl;
        tab.push_back(string(s2));
        //cout << s << endl;
    }
}

void processSeed(int seed) {
    char s[1000];
    computePaliBaseEven(seed, s);
    checkBase(s);
    computePaliBaseOdd(seed, s, 0);
    checkBase(s);
    computePaliBaseOdd(seed, s, 1);
    checkBase(s);
}

void precompute10() {
    int oldPrefix = -1;
    for (int seed = 1; seed < (1 << 25); ++seed) {
        int prefix = seed & ((1 << 25) - (1 << 20));
        if (prefix != oldPrefix) {
            logp << "PROGRESS: " << (prefix >> 20) << endl;
            oldPrefix = prefix;
        }

        processSeed(seed);
    }
}

void compute2Odd(char *s, int len, char mid) {
    for (int i = 0; i < 2*len + 1; ++i)
        s[i] = '0';
    s[0] = '2';
    s[2*len] = '2';
    s[len] = mid;

    s[2*len+1] = 0;
}

void compute2Even(char* s, int len) {
    for (int i = 0; i < 2*len; ++i)
        s[i] = '0';
    s[0] = '2';
    s[2*len - 1] = '2';

    s[2*len] = 0;
}

void compute2Mid(char* s, int len, int pos1) {
    for (int i = 0; i < 2*len+1; ++i)
        s[i] = '0';
    s[len] = '2';
    s[0] = s[2*len] = '1';
    s[pos1] = s[2*len - pos1] = '1';

    s[2*len + 1] = 0;
}

void precompute2() {
    int len = 25;
    char s2[1000];

    for (int i = 1; i <= len; ++i)
    {
        compute2Odd(s2, i, '0');
        checkBase(s2);
        compute2Odd(s2, i, '1');
        checkBase(s2);
        compute2Even(s2, i);
        checkBase(s2);
    }

    for (int i = 1; i <= len; ++i)
        for (int j = 0; j < i; ++j) {
            compute2Mid(s2, i, j);
            checkBase(s2);
        }
}

int solve(const std::string& a, const std::string& b) {
    numset::iterator lb = lower_bound(tab.begin(), tab.end(), a, NumComparator());
    numset::iterator ub = upper_bound(tab.begin(), tab.end(), b, NumComparator());
    return distance(lb, ub);
}

int main() {
    tab.push_back("1");
    tab.push_back("4");
    tab.push_back("9");

    precompute2();
    precompute10();

    logp << "Sorting ..." << endl;
    sort(tab.begin(), tab.end(), NumComparator());

    //cout << "Sorted: " << endl;
    //for (int i = 0; i < tab.size(); ++i)
        //cout << tab[i] << endl;
//    processSeed(10);
//    checkBase("1111000000001111");

    int T;
    string A, B;
    cin >> T;

    for (int t = 1; t <= T; t++) {
        cin >> A >> B;
        int res = solve(A, B);
        cout << "Case #" << t << ": " << res  << endl;
    }

    return 0;
}

