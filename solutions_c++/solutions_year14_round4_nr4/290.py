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

#define TEST "small"
const int N = 10;

vector<string> s;
int n;
map<int, int> M;
const int MOD = 1e9 + 7;

vi p[N];
typedef vector<string> vs;
void f(int x)
{
    if (x == (int)s.size())
    {
        int r = 0;
        forn (i, n) {
            vector<string> cur;
            for (int y: p[i])
                cur.pb(s[y]);
            vs a;
            for (string c: cur)
            {
                string z;
                a.pb(z);
                forn (i, c.length())
                {
                    z += c[i];
                    a.pb(z);
                }
            }
            sort(all(a));
            a.resize(unique(all(a)) - a.begin());
            r += a.size();
        }
        M[r]++;
    }
    else
    {
        forn (i, n)
        {
            p[i].pb(x);
            f(x + 1);
            p[i].pop_back();
        }
    }
}

void solve()
{
    int m;
    cin >> m >> n;
    s.resize(m);
    M.clear();
    forn (i, m)
        cin >> s[i];
    f(0);
    i64 vans = M.rbegin()->first;
    i64 qans = M.rbegin()->second;
    cout << vans << " " << qans % MOD << "\n";
}

int main() {
#ifndef TEST
	freopen("input.txt", "r", stdin);
#else 
    freopen(TEST".in", "r", stdin);
    freopen(TEST".out", "w", stdout);
#endif
    int T;
    cin >> T;
    for1 (t, T)
	{
		cout << "Case #" << t << ": ";
	    solve();
    }
	return 0;
}
