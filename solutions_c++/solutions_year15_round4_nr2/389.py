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

const int maxn = 110;

pair<dbl, dbl> a[maxn];

int n;
dbl v, t;

vector<pair<dbl, dbl> > v1, v2, v3;

bool ok(dbl x)
{
    dbl V = 0;
    forn(i, sz(v2)) V += x * v2[i].sc;
    int i = 0, j = 0;
    dbl xi = x, xj = x;
    while (i < sz(v1) && j < sz(v3))
    {
        if (xi < eps)
        {
            i += 1;
            xi = x;
            continue;
        }
        if (xj < eps)
        {
            j += 1;
            xj = x;
            continue;
        }
        dbl t1 = v1[i].fs;
        dbl t2 = v3[j].fs;
        dbl r1 = v1[i].sc;
        dbl r2 = v3[j].sc;
        if ((xi * r1 * t1 + xj * r2 * t2) / (xi * r1 + xj * r2) > t)
        {
            dbl xxj = xi * r1 * (t - t1) / r2 / (t2 - t);
            V += xi * r1 + xxj * r2;
            //eprintf("add %.10lf %.10lf (T = %.10lf)\n", xi, xxj, (xi * r1 * t1 + xxj * r2 * t2) / (xi * r1 + xxj * r2));
            xi = 0;
            xj -= xxj;
        }
        else
        {
            dbl xxi = xj * r2 * (t - t2) / r1 / (t1 - t);
            V += xj * r2 + xxi * r1;
            //eprintf("add %.10lf %.10lf (T = %.10lf)\n", xj, xxi, (xxi * r1 * t1 + xj * r2 * t2) / (xxi * r1 + xj * r2));
            xj = 0;
            xi -= xxi;
        }
    }      
    //eprintf("V = %.10lf, x = %.10lf\n", V, x);
    return v < V;
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
        printf("Case #%d: ", tt + 1);
        scanf("%d%lf%lf", &n, &v, &t);
        forn(i, n) scanf("%lf%lf", &a[i].sc, &a[i].fs);
        sort(a, a + n);
        v1.clear();
        v2.clear();
        v3.clear();
        forn(i, n)
        {
            if (a[i].fs < t - eps) v1.pb(a[i]);
            else if (a[i].fs < t + eps) v2.pb(a[i]);
            else v3.pb(a[i]);
        }
        if (a[0].fs > t + eps || a[n - 1].fs < t - eps)
        {
            printf("IMPOSSIBLE\n");
            continue;
        }
        dbl l = 0, r = 1e100;
        forn(_, 1000)
        {
            dbl m = (l + r) / 2;
            if (ok(m)) r = m;
            else l = m;
        }
        printf("%.10lf\n", l);
    }         

    #ifdef home
        eprintf("Time: %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
    #endif
    return 0;
}
 