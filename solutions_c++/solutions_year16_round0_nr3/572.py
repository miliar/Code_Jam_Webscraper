#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <complex>
#include <ctime>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#pragma comment(linker, "/STACK:64000000")

template<class T> inline T sqr (T x) {return x * x;}

typedef unsigned uint;
typedef long long lng;
typedef unsigned long long ulng;
typedef long double ld;
typedef pair<int, int> PII;
typedef pair<lng, int> PLI;
typedef pair<lng, lng> PLL;
typedef pair<int, PII> PIII;
typedef pair<lng, PII> PLII;
#define FAIL ++*(int*)0
#define left asdleft
#define right asdright
#define mp make_pair
#define pb push_back
#define clr(ar,val) memset(ar, val, sizeof(ar))
#define sz(C) (int)((C).size())
#define all(C) (C).begin(), (C).end()
#define RR 151
#define X first
#define Y second
const int INF = 1000*1000*1000;
const lng LINF = INF * 1ll * INF;
const double EPS = 1e-9;

#define TASK "C"

ulng get_factor(ulng x) {
    if (x == 2) return 1;
    if (x % 2 == 0) return 2;
    for (ulng i = 3; i * i <= x; i += 2) {
        if (x % i == 0)
            return i;
    }
    return 1;
}

int bit_count(ulng x) {
    int res = 0;
    for (; x; x &= x - 1)
        ++res;
    return res;
}

const int n = 32;

int count_subsets() {
    const int k = 6;
    int primes[k] = { 3, 5, 7, 11, 13, 17 };
    int powers[11][k][n];
    for (int base = 2; base <= 10; ++base) {
        for (int p = 0; p < k; ++p) {
            int prime = primes[p];
            powers[base][p][0] = 1;
            for (int i = 1; i < n; ++i) {
                powers[base][p][i] = powers[base][p][i - 1] * base % prime;
            }
        }
    }
    int total = 0;
    for (int mask = 0; mask < (1 << (n - 2)); ++mask) {
        if (bit_count(mask) % 2 == 0)
            continue;
        bool ok = true;
        for (int base = 2; base <= 10 && ok; base += 2) {
            bool any = false;
            for (int p = 0; p < k && !any; ++p) {
                int rem = powers[base][p][0] + powers[base][p][n - 1];
                for (int i = 0; i < n - 1; ++i) {
                    if (mask & (1 << i)) {
                        rem += powers[base][p][i + 1];
                    }
                }
                any |= rem % primes[p] == 0;
            }
            ok &= any;
        }
        total += ok;
    }
    return total;
}

bool check(ulng mask, int factors[11]) {
    for (int base = 2; base <= 10; ++base) {
        int rem = 0;

        int power = 1;
        rem += power;
        for (int i = 0; i < n - 2; ++i) {
            power *= base;
            power %= factors[base];
            if (mask & (1ULL << i)) {
                rem += power;
            }
        }
        power *= base;
        power %= factors[base];
        rem += power;
        rem %= factors[base];
        if (rem) {
            cerr << base << ' ' << factors[base] << ' ' << rem << endl;
            return false;
        }
    }
    return true;
}

void doit(int m) {
    const int k = 6;
    int primes[k] = { 3, 5, 7, 11, 13, 17 };
    int powers[11][k][n];
    for (int base = 2; base <= 10; ++base) {
        for (int p = 0; p < k; ++p) {
            int prime = primes[p];
            powers[base][p][0] = 1;
            for (int i = 1; i < n; ++i) {
                powers[base][p][i] = powers[base][p][i - 1] * base % prime;
            }
        }
    }
    int factors[11] = { 0 };
    for (int base = 3; base <= 10; base += 2) {
        factors[base] = 2;
    }
    for (ulng mask = 0; mask < (1ULL << (n - 2)); ++mask) {
        if (bit_count(mask) % 2)
            continue;
        bool ok = true;
        for (int base = 2; base <= 10 && ok; base += 2) {
            bool any = false;
            for (int p = 0; p < k && !any; ++p) {
                int rem = powers[base][p][0] + powers[base][p][n - 1];
                for (int i = 0; i < n - 1; ++i) {
                    if (mask & (1ULL << i)) {
                        rem += powers[base][p][i + 1];
                    }
                }
                if (rem % primes[p] == 0) {
                    any = true;
                    factors[base] = primes[p];
                }
            }
            ok &= any;
        }
        if (ok) {
            cout << 1;
            for (int i = n - 3; i >= 0; --i) {
                cout << (int)!!(mask & (1ULL << i));
            }
            cout << 1;
            for (int base = 2; base <= 10; ++base) {
                cout << ' ' << factors[base];
            }
            cout << endl;
            if (!check(mask, factors)) {
                cerr << "FAIL" << endl;
                exit(123);
            }
            if (--m == 0) break;
        }
    }
}

void solve() {
    int n, m;
    cin >> n >> m;
    cout << endl;
    doit(m);
}

//#define DEBUG
//#define SMALL
#define LARGE

int main() {
#ifdef SMALL                                   
    freopen(TASK "-small-attempt2.in", "r", stdin);
    freopen(TASK "-small-attempt2.out", "w", stdout);
#endif
#ifdef LARGE
    freopen(TASK "-large.in", "r", stdin);
    freopen(TASK "-large.out", "w", stdout);
#endif
#ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

	//stress();

	int T;
	char buf[32];
    fgets(buf, sizeof buf, stdin);
    sscanf(buf, "%d", &T);
    for (int test = 1; test <= T; ++test) {
        fprintf(stderr, "Test %d is in progress...", test);
        printf("Case #%d: ", test);
        solve();
        fprintf(stderr, "done.\n");
    }


    return 0;
}
