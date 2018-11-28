#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
#include <string>
#include <sstream>
#include <list>

using namespace std;

#define pq priority_queue
#define btc(x) __builtin_popcount(x)
#define mp(x, y) make_pair(x, y)
#define paii pair< int, int >
#define pasi pair< string, int >
#define pais pair< int, string >
#define mem(a,b) memset(a, b, sizeof(a))
#define pb(a) push_back(a)
#define pi (2*acos(0))
#define oo 1<<20
#define dd double
#define ll long long int
#define llu long long unsigned
#define ERR 1e-5
#define fst first
#define sec second
#define SZ(a) (int)a.size()
#define All(a) a.begin(),a.end()
#define FOR(i,p,k) for (i=p; i<k;i++)
#define REP(i,n) for (i=0;i<n;i++)
#define REV(i,n) for (i=n;i>=0;i--)
#define csprint(a) printf("Case %d: ",a)
//int x[]={1,0,-1,0};int y[]={0,1,0,-1}; //4 Direction
//int x[]={1,1,0,-1,-1,-1,0,1};int y[]={0,1,1,1,0,-1,-1,-1};//8 direction
//int x[]={2,1,-1,-2,-2,-1,1,2};int y[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
//int x[]={2,1,-1,-2,-1,1};int y[]={0,1,1,0,-1,-1}; //Hexagonal Direction

///Power && Bigmod
//ll Pow(ll B,ll P){  ll R=1; while(P>0)  {if(P%2==1) R=(R*B);P/=2;B=(B*B);}return R;}
//int BigMod(ll B,ll P,ll M){ ll R=1; while(P>0)  {if(P%2==1){R=(R*B)%M;}P/=2;B=(B*B)%M;} return (int)R;} /// (B^P)%M

///Sieve_Prime
//int prime[MAXP]; bool flag[MAXL];
//int sieve() { int i, j, total = 0, val;val = sqrt(MAXL)+1;flag[0]=flag[1]=1;for(i=2; i<val; i++)if(!flag[i])
//for(j=i; j*i<=MAXL; j++)flag[i*j] = 1;for(i=2; i<=MAXL; i++)if(!flag[i])prime[total++] = i; return total; }

///IntToString
//string tostring(int n) {string s, ret;do{s+=(n%10+'0');n/=10;}while(n);for(int i=s.size()-1;i>=0;i--)ret += s[i];return ret;}

///StringToInt
//int toint(string s) {int ret=0;for(int i=0;i<s.size();i++){ret=(s[i]-'0')+ret*10;}return ret;}

///StringMod
//int string_mod(string s, int b) {int ret=0;for(int i=0;i<s.size();i++){ret=(s[i]-'0'%b)+ret*10;}return ret%b;}

///GCD && LCM
//template<class T> inline T lcm(T a,T b) { if(a<0)return lcm(-a,b); if(b<0)return lcm(a,-b); return a*(b/(gcd(a,b)));}
//template<class T> inline T gcd(T a,T b) { if(a<0)return gcd(-a,b); if(b<0)return gcd(a,-b); return (b==0)?a:gcd(b,a%b);}

#define MAXL 1010
#define MAXS 1000010
#define MAXP 90000
#define INFIN 1001001001

vector<int>arr_1[5], arr_2[5];
int ans_1, ans_2;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int i, j, t, test, a, ans;
    scanf("%d", &test);
    for(t=1; t<=test; t++)
    {
        for(i=0; i<4; i++)
            arr_1[i].clear();
        for(i=0; i<4; i++)
            arr_2[i].clear();

        scanf("%d", &ans_1);
        for(i=0; i<4; i++)
            for(j=0; j<4; j++)
            {
                scanf("%d", &a);
                arr_1[ i ].pb( a );
            }
        scanf("%d", &ans_2);
        for(i=0; i<4; i++)
            for(j=0; j<4; j++)
            {
                scanf("%d", &a);
                arr_2[ i ].pb( a );
            }

        map< int , int >tag;
        tag.clear();

        for(i=0; i<4; i++)
            if( (ans_1-1) == i )
                for(j=0; j<SZ( arr_1[i] ); j++)
                    tag[ arr_1[i][j] ] = 1;

        int tot = 0;
        for(i=0; i<4; i++)
            if( (ans_2-1) == i )
                for(j=0; j<SZ( arr_2[i] ); j++)
                {
                    if( tag[ arr_2[i][j] ] )
                    {
                        tot++;
                        ans = arr_2[i][j];
                    }
                }

        if( !tot )
            printf("Case #%d: Volunteer cheated!\n", t);
        else if( tot>1 )
            printf("Case #%d: Bad magician!\n", t);
        else
            printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}

