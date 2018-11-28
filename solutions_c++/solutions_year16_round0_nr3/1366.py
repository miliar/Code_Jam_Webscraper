#include<bits/stdc++.h>
using namespace std;

#define FRE(i,a,b)  for(i = a; i <= b; i++)
#define FRL(i,a,b)  for(i = a; i < b; i++)
#define mem(t, v)   memset ((t) , v, sizeof(t))
#define all(x)      x.begin(),x.end()
#define un(x)       x.erase(unique(all(x)), x.end())
#define sf(n)       scanf("%d", &n)
#define sff(a,b)    scanf("%d %d", &a, &b)
#define sfff(a,b,c) scanf("%d %d %d", &a, &b, &c)
#define sl(n)       scanf("%lld", &n)
#define sll(a,b)    scanf("%lld %lld", &a, &b)
#define slll(a,b,c) scanf("%lld %lld %lld", &a, &b, &c)
#define D(x)        cout<< endl << #x " = "<<(x)<<endl
#define DBG         pf("Hi\n")
#define pf          printf
#define pii         pair <int, int>
#define pll         pair <LL, LL>
#define pb          push_back
#define PI          acos(-1.00)
#define sz          size()
#define xx          first
#define yy          second
#define eps         1e-9

typedef long long int LL;
typedef double db;
LL exp(LL a, LL b)
{
    if(b == 0)
        return 1;
    if(b&1)
        return a*exp(a,b-1);
    LL ret = exp(a,b/2);
    return ret*ret;
}
vector <LL> sltn;
LL level[110];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int i, j, k, cs, t, c, s;
    sf(t);
    FRE(cs,1,t)
    {
        sfff(k,c,s);
        pf("Case #%d:",cs);
        int total = (ceil((db)k/(c)));
        level[c] = k;
        if(total > s)
        {
            pf(" IMPOSSIBLE\n");
            continue;
        }
        for(i = c-1; i>=1; i--)
            level[i] = level[i+1]*k;
        int cc = c;
        if(total == 1)
            c = k;
        LL place = 1, take = c;
        for(int nw = 1; nw<c; nw++, take--)
            place += (take-1)*level[nw+1];//, D(level[nw+1]),D(nw+1), D(take);
        //assert(take == 1);
        LL a = place;
        for(i = 1; i<total; i++)
            sltn.pb(place), place+= a;
        place = exp(k,cc) - a + 1;
        sltn.pb(max(1LL,place));
        for(i = 0; i<sltn.sz; i++)
            pf(" %lld",sltn[i]);
        puts("");
        sltn.clear();
    }
    return 0;
}

