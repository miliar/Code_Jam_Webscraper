/* --- Author: Vladimir Smykalov, enot.1.10@gmail.com --- */
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

using namespace std;

typedef long long ll;
typedef double ld;
typedef vector<int> vi;
typedef pair<int, int> pi;

const int inf = (int)1e9;
const ld eps = 1e-9;

/* --- main part --- */

#define TASK "a"

const int maxn = (int) 2010;
int a[maxn], b[maxn];
int aa[maxn], bb[maxn];
int res[maxn];

int t[maxn];
inline void clear()
{
    memset(t, 0, sizeof t);
}
inline int get(int x)
{
    x += 1;
    int res = 0;
    for(; x ; x -= x & -x) res = max(res, t[x]);
    return res;
}
inline void add(int x, int dx)
{
    x += 1;
    t[x] = dx;
    for(; x < maxn ; x += x & -x) t[x] = max(t[x], dx);
}
int n;
inline bool recalc()
{
    clear();
    forn(j, n)
    {
        aa[j] = get(res[j] - 1) + 1;
        add(res[j], aa[j]);
    }
    clear();
    for(int j = n - 1 ; j >= 0 ; j--)
    {
        bb[j] = get(res[j] - 1) + 1;
        add(res[j], bb[j]);
    }
    bool ok = true;
    forn(i, n)
    {
        if(a[i] < aa[i]) ok = false;
        if(b[i] < bb[i]) ok = false;
    }
    return ok;                                                                                        
}

inline bool rec(int i)
{
    //forn(j, n) eprintf("%d%c", res[j], " \n"[j + 1 == n]);
    if(i == n) return true;
    if(not recalc()) return false;
    bool ok = false;
    forn(j, n) if(res[j] == n + 1)
    {
        if(a[j] == aa[j] && b[j] == bb[j])
        {
            res[j] = i + 1;
            ok = rec(i + 1);
            if(ok) break;
            res[j] = n + 1;
            recalc();
        }
    }
    return ok;
}

int main()
{
    #ifdef home
        assert(freopen(TASK".in", "r", stdin));
        assert(freopen(TASK".out", "w", stdout));
    #endif
    int tn;
    scanf("%d", &tn);
    forn(_, tn)
    {
        printf("Case #%d: ", _ + 1);
        eprintf("Case #%d:\n", _ + 1);
        scanf("%d", &n);
        forn(i, n) scanf("%d", &a[i]);
        forn(i, n) scanf("%d", &b[i]);
        forn(i, n) aa[i] = 1, bb[i] = 1;
        forn(i, n) res[i] = n + 1;
        bool ok = rec(0);
        assert(ok);
        forn(i, n) printf("%d%c", res[i], " \n"[i + 1 == n]);
    }

    #ifdef home
        eprintf("Time: %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
    #endif
    return 0;
}
 