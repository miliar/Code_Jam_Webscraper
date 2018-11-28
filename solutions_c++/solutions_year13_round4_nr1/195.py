#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>
#include <queue>
#include <map>
#include <cstdio>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <cstring>
#define REP(i,x,v)for(int i=x;i<=v;i++)
#define REPD(i,x,v)for(int i=x;i>=v;i--)
#define FOR(i,v)for(int i=0;i<v;i++)
#define FORE(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
#define FOREACH(i,t) FORE(i,t)
#define REMIN(x,y) (x)=min((x),(y))
#define REMAX(x,y) (x)=max((x),(y))
#define pb push_back
#define sz size()
#define mp make_pair
#define fi first
#define se second
#define ll long long
#define IN(x,y) ((y).find((x))!=(y).end())
#define un(v) v.erase(unique(ALL(v)),v.end())
#define LOLDBG
#ifdef LOLDBG
#define DBG(vari) cerr<<#vari<<" = "<<vari<<endl;
#define DBG2(v1,v2) cerr<<(v1)<<" - "<<(v2)<<endl;
#else
#define DBG(vari)
#define DBG2(v1,v2)
#endif
#define CZ(x) scanf("%d",&(x));
#define CZ2(x,y) scanf("%d%d",&(x),&(y));
#define CZ3(x,y,z) scanf("%d%d%d",&(x),&(y),&(z));
#define wez(x) int x; CZ(x);
#define wez2(x,y) int x,y; CZ2(x,y);
#define wez3(x,y,z) int x,y,z; CZ3(x,y,z);
#define SZ(x) int((x).size())
#define ALL(x) (x).begin(),(x).end()
#define tests int dsdsf;cin>>dsdsf;while(dsdsf--)
#define testss int dsdsf;CZ(dsdsf);while(dsdsf--)
using namespace std;
typedef pair<int,int> pii;
typedef vector<int> vi;
template<typename T,typename TT> ostream &operator<<(ostream &s,pair<T,TT> t) {return s<<"("<<t.first<<","<<t.second<<")";}
template<typename T> ostream &operator<<(ostream &s,vector<T> t){s<<"{";FOR(i,t.size())s<<t[i]<<(i==t.size()-1?"":",");return s<<"}"<<endl; }
inline void pisz (int x) { printf("%d\n", x); }
#define MOD 1000002013LL
ll start[3111],stop[3111],p[3111];
ll ile[3222];

int main()
{
    ios_base::sync_with_stdio(0);
    int te=1;
    tests
    {
        ll n,m;cin>>n>>m;
        vector<ll> v;
        ll koszt=0;
        FOR(i,m)
        {
            cin>>start[i]>>stop[i]>>p[i];
            v.pb(start[i]);
            v.pb(stop[i]);
            ll x=stop[i]-start[i];
            //DBG(x);
            koszt+=(((n+n-x+1)*x/2)%MOD)*p[i];
            koszt%=MOD;
            //DBG(koszt);
        }
        sort(ALL(v));un(v);
        FOR(i,v.sz+3)ile[i]=0;
        FOR(i,m)
        {
            FOR(j,v.sz-1)
            {
                if (start[i]<=v[j] && v[j+1]<=stop[i]) ile[j]+=p[i];
            }
        }
        ll wyn=0;
        
        while(1)
        {
            int x=0,y=0;
            int i=0;
            while(i<v.sz)
            {
                int j=i;
                while(ile[j]) j++;
                if (v[j]-v[i]>v[y]-v[x])
                {
                    x=i;
                    y=j;
                }
                if (i==j) i++;
                else i=j;
            }
            if (x==y) break;
            ll mn=(1LL<<60);
            REP(k,x,y-1)REMIN(mn,ile[k]);
            REP(k,x,y-1)ile[k]-=mn;
            ll d=v[y]-v[x];
            wyn+=(((n+n-d+1)*d/2)%MOD)*(mn%MOD);
            wyn%=MOD;
        }
        koszt-=wyn;
        koszt%=MOD;
        koszt=(koszt+MOD)%MOD;
        int K=koszt;
        printf("Case #%d: %d\n",te++,K);
    }

    return 0;
}
