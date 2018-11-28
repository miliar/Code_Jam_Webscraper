#pragma comment(linker, "/stack:128000000")

#include <algorithm>
#include <iostream>
#include <cassert>
#include <iomanip>
#include <climits>
#include <utility>
#include <cstring>
#include <complex>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <bitset>
#include <string>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <set>
#include <map>

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define forl(i, n) for (int i = 1; i <= int(n); i++)
#define fore(i, l, r) for (int i = int(l); i <= int(r); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define all(a) (a).begin(), (a).end()
#define sz(a) int((a).size())
#define pb(a) push_back(a)
#define mp(a, b) make_pair((a), (b))
#define x first
#define y second
#define ft first
#define sc second

using namespace std;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = INT_MAX / 2;
const ld EPS = 1e-9;
const ld PI = 3.1415926535897932384626433832795;

const int K = 4 * 100 * 1000 * 1000 + 13;
bool prime[K];

int szp = 0;
int primes[K];

int k, n;

inline bool read()
{
    if (!(cin >> n >> k))
        return false;

    return true;
}

inline void gen_primes()
{
    memset(prime, true, sizeof(prime));
    szp = 0;
    prime[0] = prime[1] = false;

    fore(i, 2, K - 1)
        if (prime[i])
        {
                primes[szp++] = i;

                for(int j = 2 * i; j < K; j += i)
                    prime[j] = false;
        }
}

int sz = 0, a[40], res[40];

inline int get_d(li x)
{
    forn(i, szp)
    {
        if (li(primes[i]) >= x)
            break;
             
        if (x % li(primes[i]) == 0)
            return primes[i];
    }

    return -1;
}

inline li to_int(int base)
{
    li ans = 0;

    ford(i, sz)
        ans = (ans * li(base)) + li(a[i]);

    return ans;
}

inline bool check(int x)
{
    sz = 0;
    while(x > 0)
    {
        a[sz++] = (x & 1);
        x >>= 1;
    }

    if (a[0] != 1 || a[sz - 1] != 1)
        return false;

    assert(sz < 40);

    fore(base, 2, 10)
    {
        li val = to_int(base);

        int d = get_d(val);

        if (d == -1)
            return false;

        res[base] = d;
    }

    return true;
}

inline void solve(int test)
{
	printf("Case #%d:\n", test + 1);

    forn(mask, (1 << (n - 1)))
    {
        if (k == 0)
            break;

        int x = (1 << (n - 1)) + mask;

        if (check(x))
        {
            //cout << x << " ";
            ford(i, sz)
                cout << a[i];
            cout << " ";
            fore(base, 2, 10)
                cout << res[base] << " ";
            cout << endl;

            k--;
        }
    }

    assert(k == 0);
}

int main()
{
#ifdef HP
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif

    gen_primes();

	int testCnt;
	assert(cin >> testCnt);

	forn(test, testCnt)
	{
    	assert(read());
    	solve(test);
	}

    return 0;
}

