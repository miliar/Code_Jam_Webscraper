#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <fcntl.h>
#include <fstream>
// #include <hash_map>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <unistd.h>
#include <utility>
#include <vector>

// Use C++ Big Integer Library written and maintained by Matt McCutchen <matt@mattmccutchen.net>
// Url: https://mattmccutchen.net/bigint/
#include "./bigint/BigIntegerLibrary.hh"

using namespace std;
// using namespace __gnu_cxx;  // Essential if you want to use hash_map.

typedef BigInteger ll;

#define rep(i, n) for (ll i = 0; i < (n); ++i)
#define sz(x) (static_cast<int> ((x).size()))
#define fev(i, v) for (int i = 0; i < sz(v); ++i)
#define pb push_back

ll A, B;

bool isPalindrome(const char *buf) {
    int len = strlen(buf);
    for (int i = 0; 2 * i < len - 1; ++i) {
        if (buf[i] != buf[len - 1 - i]) {
            return false;
        }
    }
    return true;
}

bool isPalindrome(ll n) {
    char buf[120];
    string tmp = bigIntegerToString(n);
    strcpy(buf, tmp.c_str());
    return isPalindrome(buf);
}

vector<ll> cache;
vector<ll> roots;

const ll kMax = 100000;

void once() {
    assert(cache.empty() && roots.empty());
    rep(i, kMax) {
        if (isPalindrome(i)) {
            ll ii = i;
            ii *= i;
            if (isPalindrome(ii)) {
                cache.pb(ii);
                roots.pb(i);
                // cout << "\t" << i << " " << ii << endl;
            }
        }
    }
    for (int digit = 6; digit < 51; ++digit) {
        cout << digit << endl;
        vector<ll> buffer;
        fev (it, roots) {
            ll n = roots[it];
            string tmp = bigIntegerToString(n);
            int len = sz(tmp);
            int diff = digit - len - 2;
            if (diff >= 0 && diff % 2 == 0) {
                    string pad(diff / 2, '0');
                    for (char lead = '1'; lead <= '2'; ++lead) {
                        string candidate = lead + pad + tmp + pad + lead;
                        // assert(sz(candidate) == digit);
                        // assert(isPalindrome(candidate.c_str()));
                        ll i = stringToBigInteger(candidate);
                        ll ii = i * i;
                        if (isPalindrome(ii)) {
                            cache.pb(ii);
                            buffer.pb(i);
                            // cout << "\t" << i << " " << ii << endl;
                        }
                    }
            }
            if (n == 0 && digit % 2 == 0) {
                    // assert(digit >= 2);
                    string pad(digit - 2, '0');
                    for (char lead = '1'; lead <= '2'; ++lead) {
                        string candidate = lead + pad + lead;
                        // assert(sz(candidate) == digit);
                        // assert(isPalindrome(candidate.c_str()));
                        ll i = stringToBigInteger(candidate);
                        ll ii = i * i;
                        if (isPalindrome(ii)) {
                            cache.pb(ii);
                            buffer.pb(i);
                            // cout << "\t" << i << " " << ii << endl;
                        }
                    }
            }
        }
        fev(i, buffer) {
            roots.pb(buffer[i]);
        }
    }
    /*
    fe(it, roots) {
        ll i = *it;
        cout << "\t" << i << " " << i * i << endl;
    }
    */
    cout << "Total: " << sz(cache) << endl;
}

ll solveLg2() {
    ll cnt = 0;
    fev (i, cache) {
        if (cache[i] >= A && cache[i] <= B) {
            ++cnt;
        }
    }
    return cnt;
}

void main2() {
    once();

    /*
    A = 2000000;
    B = 10000000;
    assert(solveLg2() == 1);
    */

    /*ifstream in("sample.txt");
    ofstream out("sample.output");*/
    /*ifstream in("C-large-1.in");
    ofstream out("C-large-1.output");*/
    ifstream in("C-large-2.in");
    ofstream out("C-large-2.output");
    int num_cases;
    in >> num_cases;
    cout << num_cases << endl;
    char buf[1000];
    in.getline(buf, 500);
    for (int i = 1; i <= num_cases; ++i) {
        in.getline(buf, 500);
        char *sep = strchr(buf, ' ');
        *sep = '\0';
        string a_str(buf), b_str(sep + 1);
        A = stringToBigInteger(a_str);
        B = stringToBigInteger(b_str);
        // cout << A << " " << B << endl;
        ll ans = solveLg2();
        // cout << "Case #" << i << ": " << ans << endl;
        out << "Case #" << i << ": " << ans << endl;

    }
    in.close();
    out.close();
}

int main() {
    main2();

    return 0;
}
