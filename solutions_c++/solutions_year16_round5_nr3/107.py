/**
 *    author:  itmo1
 *    created: 11.06.2016 19:22:40       
**/
#define __USE_MINGW_ANSI_STDIO 0
#include <bits/stdc++.h>

#define F first
#define S second
#define pb push_back
#define mp make_pair
#define forn(i, n) for(int i = 0 ; (i) < (n) ; ++i)
#define eprintf(...) fprintf(stderr, __VA_ARGS__),fflush(stderr)
#define sz(a) ((int)(a).size())
#define all(a) (a).begin(),a.end()
#define pw(x) (1LL<<(x))

using namespace std;

typedef long long ll;
typedef double dbl;
typedef vector<int> vi;
typedef pair<int, int> pi;

const int inf = 1.01e9;
const dbl eps = 1e-9;

/* --- main part --- */

const int N = 1010;

struct pt
{
    dbl x, y, z;
    pt(){}
    pt(dbl xx, dbl yy, dbl zz): x(xx), y(yy), z(zz) {}
    void read()
    {
        scanf("%lf%lf%lf", &x, &y, &z);
    }
};

inline dbl dist(pt p1, pt p2)
{
    dbl dx = p1.x - p2.x;
    dbl dy = p1.y - p2.y;
    dbl dz = p1.z - p2.z;
    return sqrt(dx * dx + dy * dy + dz * dz);
}

pt A[N];
pt B[N];
int p[N];

pair<dbl, pi> e[N * N];
int ec = 0;

inline int get(int x)
{
    if (p[x] != x) p[x] = get(p[x]);
    return p[x];
}

int main()
{
    #ifdef home
        assert(freopen("1.in", "r", stdin));
        assert(freopen("1.out", "w", stdout));
    #endif
    int tn;
    scanf("%d", &tn);
    forn(tt, tn)
    {
        int n;
        int s;
        scanf("%d%d", &n, &s);
        forn(i, n)
        {
            A[i].read();
            B[i].read();
        }
        forn(i, n) p[i] = i;
        ec = 0;
        forn(i, n) forn(j, i)
        {
            e[ec++] = mp(dist(A[i], A[j]), mp(i, j));
        }
        sort(e, e + ec);            
        dbl res = 0;
        forn(i, ec)
        {
            int x = e[i].S.F;
            int y = e[i].S.S;
            dbl d = e[i].F;
            if (get(x) != get(y))
            {
                if (rand() & 1) swap(x, y);
                p[get(x)] = get(y);
                res = d;
            }
            if (get(0) == get(1)) break;
        }
        printf("Case #%d: %.10f\n", tt + 1, res);
    }

              
    #ifdef home
        eprintf("time = %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
    #endif
    return 0;
}
