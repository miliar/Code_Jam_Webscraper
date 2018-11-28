#include <cassert>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <numeric>
#include <bitset>
#include <vector>
#include <set>
#include <string>
#include <map>
#include <cmath>
#include <algorithm>
#include <queue>
#include <cstdlib>
#include <functional>
#include <cstring>
#include <ctime>
#include <memory.h>

#define y1 AAA_BBB
#define y0 AAA_AAA

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for(int i = (int)(a); i <= (int)(b); ++i)
#define for1(i, n) for(int i = 1; i <= (int)(n); ++i)
#define all(v) (v).begin(), (v).end()
#define sz(v) ((int)(v.size()))

using namespace std;

typedef long long i64;
typedef unsigned long long u64;
typedef long double ld;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef vector<pii> vpi;

template <class T> T inline sqr(T x) {
    return x * x;
}

const ld pi = 3.1415926535897932384626433832795;
const ld eps = 1e-8;

#define TEST "large"

void solve()
{
    int n;
    i64 p, q, r, S;
    cin >> n >> p >> q >> r >> S;
    vi a(n);
    forn (i, n) a[i] = ((i * p + q) % r) + S;
    vector<i64> s(n + 1);
    forn (i, n)
        s[i + 1] = s[i] + a[i];
    i64 ans = 1e18;
    for1 (i, n)
    {
        i64 s1 = s[i-1];
        i64 srem = s[n] - s1;
        int l = i, r = n + 1;
        while (l + 1 < r)
        {
            int mid = (l + r) / 2;
            if (s[mid] - s1 < srem / 2)
                l = mid;
            else
                r = mid;
        }
        for (int di = -2; di <= 2; di++)
        {
            int p = di + l;
            if (p >= i && p <= n) {
            i64 s2 = s[p] - s1;
            i64 s3 = s[n] - s[p];
            ans = min(ans, max(s1, max(s2, s3)));
            }
        }
    }
    cout << (s[n] - ans) / ld(s[n]) << "\n";
}

int main() {
#ifndef TEST
	freopen("input.txt", "r", stdin);
#else 
    freopen(TEST".in", "r", stdin);
    freopen(TEST".out", "w", stdout);
#endif
    cout.precision(15);
    cout << fixed;
    int T;
    cin >> T;
    for1 (t, T)
	{
		cout << "Case #" << t << ": ";
	    solve();
    }
	return 0;
}
