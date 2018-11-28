/* --- author: enot-the-rockstar ---*/
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <ctime>
#include <cassert>

#define fs first
#define sc second
#define pb push_back
#define mp make_pair
#define forn(i, n) for(int i = 0 ; (i) < (n) ; ++i)
#define forit(it,v) for(typeof((v).begin()) it = v.begin() ; it != (v).end() ; ++it)
#define eprintf(...) fprintf(stderr, __VA_ARGS__),fflush(stderr)
#define sz(a) ((int)(a).size())
#define all(a) (a).begin(),a.end()

static inline unsigned long long rdtsc() { unsigned long long d; __asm__ __volatile__ ("rdtsc" : "=A" (d) ); return d; }

using namespace std;

typedef long long ll;
typedef double dbl;
typedef vector<int> vi;
typedef pair<int, int> pi;

const int inf = (int)1e9;
const dbl eps = 1e-9;

/* --- main part --- */

#define TASK "a"

const int maxn = (int)1e5 + 10;

char s[maxn];

vi v[maxn];

set<int> sa, sb;

int val = 0;

int a[maxn], ac = 0;
int b[maxn], bc = 0;

void adda(int x)
{
    if (sa.find(x) == sa.end())
    {
        sa.insert(x);
        a[ac++] = x;
        if (sb.find(x) != sb.end())
        {
            val += 1;
        }
    }
}
void addb(int x)
{
    if (sb.find(x) == sb.end())
    {
        sb.insert(x);
        b[bc++] = x;
        if (sa.find(x) != sa.end())
        {
            val += 1;
        }
    }
}

void addA(int x)
{
    forn(i, sz(v[x])) adda(v[x][i]);
}
void addB(int x)
{
    forn(i, sz(v[x])) addb(v[x][i]);
}
int main()
{
    #ifdef home
        assert(freopen(TASK".in", "r", stdin));
        assert(freopen(TASK".out", "w", stdout));
    #endif
    int tn;
    scanf("%d", &tn);
    forn(tt, tn)
    {
        eprintf("start %d :: ", tt);
    #ifdef home
        eprintf("Time: %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
    #endif
        printf("Case #%d: ", tt + 1);
        int n;
        scanf("%d\n", &n);
        forn(i, n)
        {
            v[i].clear();
            gets(s);
            int h = 0;
            for (int j = 0; s[j]; ++j)
            {
                if ('a' <= s[j] && s[j] <= 'z')
                {
                    h = h * 239 + s[j];
                }
                else
                {
                    if (h != 0)
                    {
                        v[i].pb(h);
                    }
                    h = 0;
                }
            }
            if (h != 0) v[i].pb(h);
        }
        sa.clear();
        sb.clear();
        int res = inf;
        val = 0;
        addA(0);
        addB(1);
        ac = 0, bc = 0;
        forn(i, 1 << (n - 2))
        {
            int oldval = val;
            forn(j, n - 2)
            {
                if ((i >> j) & 1) addA(j + 2);
                else addB(j + 2);
            }
            res = min(res, val);
            val = oldval;
            while (ac > 0) sa.erase(a[--ac]);
            while (bc > 0) sb.erase(b[--bc]);
        }
        printf("%d\n", res);
    }
    #ifdef home
        eprintf("Time: %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
    #endif
    return 0;
}
 