#pragma comment(linker, "/STACK:12000000")

#include <algorithm>
#include <vector>
#include <iostream>
#include <fstream>
#include <iterator>
#include <cmath>
#include <cassert>
#include <iomanip>
#include <sstream>

using namespace std;

// --------------------- Template ---------------------------------------------

#define FOR(i, f, t) for (int i = (int)(f); i < (int)(t); ++i)
#define FORN(i, n) for (int i = 0; i < (int)(n); ++i)

template <class T, class IT>
inline void PRINT(IT i1, IT i2) {
    cout << '['; copy(i1, i2, ostream_iterator<T>(cout, ", ")); cout << "]\n";
}

#if defined(M_H_HOME) && (1)
#define DBG(x) (x)
#else
#define DBG(x)
#endif

typedef long long ll;
typedef long double ld;

// ------------------ Template end --------------------------------------------

vector<ll> fairSquareNumbers;

ll getPalindrome(ll head, bool even) {
    stringstream ss;
    ss << head;
    string p = ss.str(), palindrome;
    copy(p.begin(), p.end(), back_inserter(palindrome));
    copy(p.rbegin() + (even ? 0 : 1), p.rend(), back_inserter(palindrome));
    ss.str(palindrome);
    ll result;
    ss >> result;
    return result;
}

bool isPali(ll x) {
    stringstream ss;
    ss << x;
    string p = ss.str();
    return equal(p.begin(), p.end(), p.rbegin());
}

bool isSquaredPali(ll x) {
    ll lw = static_cast<ll>(sqrt(static_cast<long double>(x)) - 1); // lower bound of square root
    while (lw * lw < x) ++lw;
    return (lw * lw == x) && (isPali(lw));
}

int main() {

#if defined(M_H_HOME) && (0)
    ifstream ___ifs("c.in.1");
    cin.rdbuf(___ifs.rdbuf());
#endif

    for (ll num = 1; num <= 9999999; ++num) {
        // перебираем старшую часть палиндрома
        ll pal = getPalindrome(num, true);
        if (isSquaredPali(pal)) fairSquareNumbers.push_back(pal);
        pal = getPalindrome(num, false);
        if (isSquaredPali(pal)) fairSquareNumbers.push_back(pal);
    }
    sort(fairSquareNumbers.begin(), fairSquareNumbers.end());

    for (size_t i = 0; i < fairSquareNumbers.size(); ++i) {
        DBG(cout << fairSquareNumbers[i] << '\n');
    }
    
    size_t T;
    ll A, B;
    cin >> T;
    FOR(casen, 1, T+1) {
        cout << "Case #" << casen << ": ";
        cin >> A >> B;
        vector<ll>::const_iterator iA, iB;
        iA = lower_bound(fairSquareNumbers.begin(), fairSquareNumbers.end(), A);
        iB = lower_bound(fairSquareNumbers.begin(), fairSquareNumbers.end(), B);
        if (iB != fairSquareNumbers.end() && *iB == B) {
            cout << iB - iA + 1 << '\n';
        } else {
            cout << iB - iA << '\n';
        }
    }

    return 0;
}
