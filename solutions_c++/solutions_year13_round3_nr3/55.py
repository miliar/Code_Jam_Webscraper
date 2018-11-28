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

const int maxn = (int)2e6 + 10;
const int N = 1 << 21;
int t[2 * N], tf[2 * N];

inline void push(int x)
{
    if(x < N && tf[x] == 1)
    {
        t[2 * x] = max(t[x], t[2 * x]);
        t[2 * x + 1] = max(t[x], t[2 * x + 1]);
        tf[x] = 0;
        tf[2 * x] = 1;
        tf[2 * x + 1] = 1;
    }
}
inline void modify(int ind, int l, int r, int lq, int rq, int q)
{
    push(ind);
    if(t[ind] >= q) return;
    if(lq <= l && r <= rq)
    {
        t[ind] = q;
        tf[ind] = 1;
        return;
    }
    if(lq >= r || rq <= l) return;
    int m = (l + r) >> 1;
    modify(2 * ind, l, m, lq, rq, q);
    modify(2 * ind + 1, m, r, lq, rq, q);
    t[ind] = min(t[2 * ind], t[2 * ind + 1]);
}
inline int get(int ind, int l, int r, int lq, int rq)
{
    push(ind);
    if(lq <= l && r <= rq)
    {
        return t[ind];
    }
    if(lq >= r || rq <= l) return 2 * inf;
    int m = (l + r) >> 1;
    return min(get(2 * ind, l, m, lq, rq), get(2 * ind + 1, m, r, lq, rq));
}
                                              
struct TR
{
    int d, n, w, e, s, dd, dp, ds;
};

int C[maxn], cc = 0;
pair<int, pi> e[maxn];
int ec = 0;        
TR tt[(int)1010];


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
        cc = 0;
        ec = 0;
        memset(t, 0, sizeof t);
        memset(tf, 0, sizeof tf);

        printf("Case #%d: ", _ + 1);
        int n;
        scanf("%d", &n);
        forn(i, n)
        {
            scanf("%d%d%d%d%d%d%d%d", &tt[i].d, &tt[i].n, &tt[i].w, &tt[i].e, &tt[i].s, &tt[i].dd, &tt[i].dp, &tt[i].ds);
            int cur = tt[i].d;
            //tt[i].dp += tt[i].e - tt[i].w;
            forn(j, tt[i].n)
            {
                e[ec++] = mp(cur, mp(i, j));
                cur += tt[i].dd;
                C[cc++] = tt[i].w + tt[i].dp * j;
                C[cc++] = tt[i].e + tt[i].dp * j;
            }
        }
        sort(C, C + cc);
        cc = unique(C, C + cc) - C;
        sort(e, e + ec);
        int RES = 0;
        for(int i = 0 ; i < ec ;)
        {
            int j = i + 1;
            while(j < ec && e[j].fs == e[i].fs) j += 1;
            for(int k = i ; k < j ; k++)
            {
                int x = e[k].sc.fs;
                int y = e[k].sc.sc;
                int lq = lower_bound(C, C + cc, tt[x].w + tt[x].dp * y) - C;
                int rq = lower_bound(C, C + cc, tt[x].e + tt[x].dp * y) - C;
                int q = tt[x].s + tt[x].ds * y;
                int gg = get(1, 0, N, lq, rq);                
                if(gg < q) RES += 1;
            }
            for(int k = i ; k < j ; k++)
            {
                int x = e[k].sc.fs;
                int y = e[k].sc.sc;
                int lq = lower_bound(C, C + cc, tt[x].w + tt[x].dp * y) - C;
                int rq = lower_bound(C, C + cc, tt[x].e + tt[x].dp * y) - C;
                assert(lq < rq);
                int q = tt[x].s + tt[x].ds * y;
                modify(1, 0, N, lq, rq, q);
                assert(get(1, 0, N, lq, rq) >= q);
            }
            i = j;
        }
        printf("%d\n", RES);

    }
    #ifdef home
        eprintf("Time: %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
    #endif
    return 0;
}
 