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

#define MAXL 2001
#define MAXS 1000010
#define MAXP 90000
#define INFIN (1<<29)

double dp[ MAXL ][ MAXL ][ 2 ];
int col[ MAXL ][ MAXL ][ 2 ];
double c, f, x;
int loop;

double rec( int amount , int b_amnt , int dec )
{
//    cout<<amount<<" "<<b_amnt<<" "<<dec<<endl;
//    getchar();
    if( dec ) return 0.00;
    if( amount*c>x ) return INFIN;
    if( col[ amount ][ b_amnt ][ dec ] ==loop ) return dp[amount][b_amnt][dec];
    col[ amount ][ b_amnt ][ dec ] = loop;

    double ret = INFIN;
    double chk1 = (b_amnt*f)+2.0;
    double chk2 = c;

//    cout<<"chk1 -- "<<chk1<<" chk2 -- "<<chk2<<endl;

    ret = min( ret , rec( amount , b_amnt , 1 )+( x/chk1 ) );
//    cout<<"ret_1111 -- >> "<<ret<<endl;
    ret = min( ret , rec( amount+1 , b_amnt+1 , 0 )+( chk2/chk1 ) );
//    cout<<"ret_22222222 -- >> "<<ret<<endl;

    dp[ amount ][ b_amnt ][ dec ] = ret;
    return dp[ amount ][ b_amnt ][ dec ];
}

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int i, j, t, test;
    double res;
    scanf("%d", &test);
    for(t=1; t<=test; t++)
    {
        scanf("%lf %lf %lf", &c, &f, &x);

        ++loop;
        res = rec( 0 , 0 , 0 );
        printf("Case #%d: %.7lf\n", t, res);
    }
    return 0;
}
