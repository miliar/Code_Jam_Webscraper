/**
 *    author:  itmo1
 *    created: 11.06.2016 17:12:28       
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

const int N = 110;

inline ll rnd()
{
    return rand() + rand() * pw(15) + rand() * pw(30) + rand() * pw(45);
}

const ll MX = RAND_MAX * pw(45);

vi v[N];
dbl d[N];
int c[N];

dbl cnk[N][N];

char s[N];
char cool[N * 2];
char r[N];

int p[N * 2];

void dfs(int x)
{
    c[x] = 0;
    d[x] = 1;
    forn(i, sz(v[x]))
    {
        int y = v[x][i];
        dfs(y);
        c[x] += c[y];
        d[x] = d[x] * d[y] * cnk[c[x]][c[y]];
    }
    c[x] += 1;
}

int n;

const int TN = 1 << 7;

pair<dbl, int> T[2 * TN];

pair<dbl, int> Merge(pair<dbl, int> &t1, pair<dbl, int> &t2)
{
    return mp(t1.F * t2.F * cnk[t1.S + t2.S][t1.S], t1.S + t2.S);
}

void upd(int x, pair<dbl, int> z)
{
    x += TN;
    T[x] = z;
    while (x > 1)
    {
        x >>= 1;
        T[x] = Merge(T[2 * x], T[2 * x + 1]);
    }
}

pair<dbl, int> get(int l, int r)
{
    l += TN;
    r += TN;
    pair<dbl, int> res = mp(1, 0);
    while (l <= r)
    {
        if ((l & 1) == 1) res = Merge(res, T[l]);
        if ((r & 1) == 0) res = Merge(res, T[r]);
        l = (l + 1) >> 1;
        r = (r - 1) >> 1;
    }
    return res;
}


void makeRand()
{
    set<int> S;
    S.insert(0);
    forn(i, 2 * TN) T[i] = mp(1, 0);
    upd(0, mp(d[0], c[0]));
    forn(ii, n + 1)
    {
        //eprintf("step %d\n", ii);
        vi vv;
        for (auto it : S) vv.pb(it);
        vector<pair<int, dbl>> e;
        
        forn(i, sz(vv))
        {
            int x = vv[i];
            int C = c[x] - 1;
            dbl D = d[x];
            /*forn(j, sz(vv)) if (i != j)
            {
                int y = vv[j];
                C += c[y];
                D = D * d[y] * cnk[C][c[y]];
            } */
            pair<dbl, int> t1 = get(0, x - 1), t2 = get(x + 1, TN - 1);
            C += t1.S;
            D *= t1.F * cnk[C][t1.S];
            C += t2.S;
            D *= t2.F * cnk[C][t2.S];

            e.pb(mp(x, D));
            //eprintf("have %d %.0f\n", x, D);
        }

        dbl R = rnd() * 1. / MX;
        dbl sum = 0;
        forn(i, sz(e)) sum += e[i].S;
        sum *= R;
        int ans = e[sz(e) - 1].F;
        forn(i, sz(e))
        {
            if (e[i].S + eps >= sum)
            {
                ans = e[i].F;
                break;
            }
            sum -= e[i].S;
        }
        S.erase(ans);
        upd(ans, mp(1, 0));
        forn(j, sz(v[ans]))
        {
            int y = v[ans][j];
            S.insert(y);
            upd(y, mp(d[y], c[y]));
        }
        if (ii) r[ii - 1] = s[ans - 1];
    }
    //eprintf("%s\n", r);
}
                
                



int main()
{
    #ifdef home
        assert(freopen("1.in", "r", stdin));
        assert(freopen("1.out", "w", stdout));
    #endif

    forn(i, N)
    {
        cnk[i][0] = 1;
        for (int j = 1; j <= i; ++j) cnk[i][j] = cnk[i - 1][j - 1] + cnk[i - 1][j];
    }

    int tn;
    scanf("%d", &tn);
    forn(tt, tn)
    {
        eprintf("test %d from %d\n", tt + 1, tn);
        printf("Case #%d: ", tt + 1);
        scanf("%d", &n);
        forn(i, n + 1) v[i].clear();
        for (int i = 1; i <= n; ++i)
        {
            int x;
            scanf("%d", &x);
            v[x].pb(i);
        }
        scanf("%s", s);
        dfs(0);
        int m;
        scanf("%d", &m);
        forn(qi, m)
        {
            scanf("%s", cool);
            int l = strlen(cool);
            dbl res = 0;
            dbl cnt = 0;
            forn(_, 1500)
            {
                makeRand();
                forn(i, n) cool[l + 1 + i] = r[i];
                int nn = l + n + 1;
                for (int i = 1; i < nn; i++)
                {
                    p[i] = p[i - 1];
                    while (p[i] && cool[i] != cool[p[i]]) p[i] = p[p[i] - 1];
                    if (cool[i] == cool[p[i]]) p[i]++;
                }
                int ok = 0;
                forn(i, nn) if (p[i] == l) ok = 1;
                res += ok;
                cnt += 1;
            }
            res /= cnt;
            printf("%.2f%c", res, " \n"[qi + 1 == m]);
        }
    }
    
    #ifdef home
        printf("time = %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
    #endif
    return 0;
}
