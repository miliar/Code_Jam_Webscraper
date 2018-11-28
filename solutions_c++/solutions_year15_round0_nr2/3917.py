
#include<bits/stdc++.h>
//#include <windows.h>
using namespace std;

#define FRE(i,a,b)  for(i = a; i <= b; i++)
#define FRL(i,a,b)  for(i = a; i < b; i++)
#define mem(t, v)   memset ((t) , v, sizeof(t))
#define sqr(x)      ((x)*(x))
#define all(x)      x.begin(),x.end()
#define un(x)       x.erase(unique(all(x)), x.end())
#define sf(n)       scanf("%d", &n)
#define sff(a,b)    scanf("%d %d", &a, &b)
#define sfff(a,b,c) scanf("%d %d %d", &a, &b, &c)
#define D(x)        cout<<#x " = "<<(x)<<endl
#define pf          printf
#define VI          vector <int>
#define pii         pair <int, int>
#define pll         pair <LL, LL>
#define pb          push_back
#define mp          make_pair
#define pi          acos(-1.00)
#define DBG         pf("Hi\n")
#define sz          size()
#define ins         insert
#define fi          first
#define se          second
#define xx          first
#define yy          second
#define inf         (1<<29)
#define hp          (LL) 999983
#define MOD         100007
#define eps         1e-9
#define MAX         1000

typedef long long int LL;
typedef double db;

//int dx[] = {+0,+1,+0,-1};
//int dy[] = {+1,+0,-1,+0};
//int dx[] = {-1,-1,-1,+0,+0,+1,+1,+1};
//int dy[] = {-1,+0,+1,-1,+1,-1,+0,+1};
//bool check(LL n, int pos) {return (bool) (n & ((LL)1<<pos));}
//LL on(LL n, int pos) {return n | ((LL)1<<pos); }
//LL off(LL n, int pos) {return n & ~((LL)1<<pos); }

map<VI, int> M;

int calc(VI sq)
{
    sort(all(sq));
    if(!sq.sz) return 0;
    if(*max_element(all(sq)) == 1) return 1;

    if(M.find(sq) != M.end()) return M[sq];

    int i, mx = 0, gbg, ret = 0, l, r, j;

    VI v1, v2;
    v1.clear();
    v2.clear();


    for(i = 0; i < sq.sz; i++)
        if(sq[i] != 1) v1.pb(sq[i] - 1);

    ret = calc(v1);
    for(i = 0; i < sq.sz; i++)
    {
        if(sq[i] != 1)
        {
            for(l = 1; l < sq[i]; l++)
            {
                v2.clear();
                r = sq[i] - l;
                v2.pb(l);
                v2.pb(r);

                for(j = 0; j < sq.sz; j++)
                    if(j != i)
                        v2.pb(sq[j]);
                ret = min(ret, calc(v2));
            }
        }
    }

    return M[sq] = 1 + ret;
}

int main()
{
    freopen("c:\\Users\\User\\Desktop\\in.txt", "r", stdin);
    freopen("c:\\Users\\User\\Desktop\\out.txt", "w", stdout);
    //ios_base::sync_with_stdio(0); cin.tie(0);

    int i, j, k, t, cs, n, m, mn, mx, v;
    int res, cnt, cur, tp;
    vector<int> sq;

    sf(t);
    FRE(cs,1,t)
    {
        M.clear();
        sq.clear();

        res = inf;
        cnt = 0;

        sf(n);
        FRE(i,1,n)
            sf(v), sq.pb(v);

        pf("Case #%d: %d\n", cs, calc(sq));
    }
    return 0;
}



