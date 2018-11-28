#include <iostream>
#include <string>
#include <stdexcept>
#include <numeric>

using namespace std;

typedef long long Long;

enum Digit {One, I, J, K};
struct Unit {int sign; Digit digit; };

inline Unit operator*(const Unit &l, const Unit &r) {
    static const Unit MT[4][4] = {
        {{1, One}, {1, I},    {1, J},    {1, K}},
        {{1, I},   {-1, One}, {1, K},    {-1, J}},
        {{1, J},   {-1, K},   {-1, One}, {1, I}},
        {{1, K},   {1, J},    {-1, I},   {-1, One}}
    };
    Unit u = MT[l.digit][r.digit];
    u.sign *= l.sign;
    u.sign *= r.sign;
    return u;
}

inline bool operator==(const Unit &l, const Unit &r) {
    return l.sign == r.sign && l.digit == r.digit;
}

ostream& operator<<(ostream& os, Unit u) {
    os << ((u.sign < 0) ? '-' : ' ');
    switch (u.digit) {
    case One: return os << '1';
    case I: return os << 'i';
    case J: return os << 'j';
    case K: return os << 'k';
    }
    return os;
}

Digit CharToDigit(char c) {
    switch (c) {
    case '1': return One;
    case 'i': return I;
    case 'j': return J;
    case 'k': return K;
    }
    throw logic_error("Bad digit char");
}

Unit Pow(Unit b, Long n) {
    Unit a = {1, One};
    while (n > 1) {
        if (n & 1) {
            a = a * b;
            n -= 1;
        } else {
            b = b * b;
            n /= 2;
        }
    }
    return a * b;
}

bool CanReduce(const string &ijks, Long x) {
    constexpr Unit UI = {1, I};
    constexpr Unit UK = {1, K};
    Unit result = {1, One};
    Unit expected = {-1, One};
    Long firstI = -1;
    Long lastK = -1;
    for (Long n = 0; n < x; ++n) {
        for (size_t i = 0; i < ijks.size(); ++i) {
            result = result * Unit{1, CharToDigit(ijks[i])};
            if (result == UI && firstI < 0) firstI = n * ijks.size() + i;
            if (result == UK) lastK = Long(n * ijks.size()) + i;
        }
    }
    return firstI >= 0 && lastK > firstI && result == expected;
}
/*
bool CanReduce(const string &ijks, Long x) {
    Unit result = {1, One};
    Unit expected = {-1, One};
    for (size_t i = 0; i < ijks.size(); ++i) {
        result = result * Unit{1, CharToDigit(ijks[i])};
    }
    result = Pow(result, x);
    return result == expected;
}
*/

int main() {
    cin.sync_with_stdio(false);
    int num_tests;
    cin >> num_tests;
    string ijks;
    for (int t = 1; t <= num_tests; ++t) {
        int l, x;
        cin >> l >> x >> ijks;
        cout << "Case #" << t << ": "
             << (CanReduce(ijks, x) ? "YES" : "NO") << "\n";
    }
    return 0;
}
