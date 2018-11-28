
/**
 * BISMILLAHIRRAHMANIRRAHIM
 * @author Raihan
 * SUST_CSE_10
 */

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
#define r_All(a) a.rbegin(),a.rend()
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

vector<double>naomi, ken;
vector<double>tem1, tem2;
int n, loop;
int dp[(1<<11)][11];

int rec( int mask , int pos )
{
    if( btc( mask )==SZ(naomi) ) return 0;
    int &ret = dp[ mask ][ pos ];
    if( ret!=-1 ) return ret;
    ret = 0;

    for(int i=0; i<SZ( ken ); i++)
        if( !(mask&(1<<i)) )
            ret = max( ret , rec( mask|(1<<i) , pos+1 )+(naomi[pos]>ken[i]) );

//    cout<<"ret -> "<<ret<<endl;
    return ret;
}

int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
    int i, j, t, test;
    double a;
    scanf("%d", &test);
    for(t=1; t<=test; t++)
    {
        map<double , int>col;
        col.clear();
        naomi.clear();
        ken.clear();
        tem1.clear();
        tem2.clear();

        scanf("%d", &n);
        for(i=0; i<n; i++)
        {
            scanf("%lf", &a);
            naomi.pb( a );
            tem1.pb( a );
        }
        for(i=0; i<n; i++)
        {
            scanf("%lf", &a);
            ken.pb( a );
            tem2.pb( a );
        }

        sort( All( tem1 ) );
        sort( All( tem2 ) );
        reverse( All(tem1) );
        reverse( All(tem2) );

        int opt_war = 0, dec_war;
        for(i=0; i<SZ( tem2 ); i++)
            for(j=0; j<SZ( tem1 ); j++)
                if( tem2[i]>tem1[j] && !col[ tem1[j] ] )
                {
                    opt_war++;
                    col[ tem1[ j ] ] = 1;
                    break;
                }

        mem( dp , -1 );
        dec_war = rec( 0 , 0 );
        printf("Case #%d: %d %d\n", t, dec_war, n-opt_war);
    }
    return 0;
}

