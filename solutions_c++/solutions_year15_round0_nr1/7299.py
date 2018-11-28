
/**
 * BISMILLAHIRRAHMANIRRAHIM
 * @author Raihan
 * SUST_CSE_10
 */

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <assert.h>

using namespace std;

#define pq              priority_queue
#define btc(x)          __builtin_popcount(x)
#define mp(x, y)        make_pair(x, y)
#define paii            pair< int, int >
#define padd            pair< double, double >
#define pasi            pair< string, int >
#define pais            pair< int, string >
#define mem(a,b)        memset(a, b, sizeof(a))
#define pb(a)           push_back(a)
#define pi              (2*acos(0))
#define oo              1<<20
#define dd              double
#define ll              long long int
#define llu             long long unsigned
#define ERR             1e-5
#define fst             first
#define sec             second
#define scni1(a)        scanf(" %d",&a)
#define scni2(a,b)      scanf(" %d %d",&a,&b)
#define scni3(a,b,c)    scanf(" %d %d %d",&a,&b,&c)
#define scnll1(a)       scanf(" %I64d",&a)
#define scnll2(a,b)     scanf(" %I64d %I64d",&a,&b)
#define scnll3(a,b,c)   scanf(" %I64d %I64d %I64d",&a,&b,&c)
#define SZ(a)           (int)a.size()
#define All(a)          a.begin(),a.end()

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
template<class T> inline T lcm(T a,T b) { if(a<0)return lcm(-a,b); if(b<0)return lcm(a,-b); return a*(b/(gcd(a,b)));}
template<class T> inline T gcd(T a,T b) { if(a<0)return gcd(-a,b); if(b<0)return gcd(a,-b); return (b==0)?a:gcd(b,a%b);}

template<class T1> void deb(T1 e){cout<<e<<endl;}
template<class T1,class T2> void deb(T1 e1,T2 e2){cout<<e1<<" "<<e2<<endl;}
template<class T1,class T2,class T3> void deb(T1 e1,T2 e2,T3 e3){cout<<e1<<" "<<e2<<" "<<e3<<endl;}
template<class T1,class T2,class T3,class T4> void deb(T1 e1,T2 e2,T3 e3,T4 e4){cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<endl;}
template<class T1,class T2,class T3,class T4,class T5> void deb(T1 e1,T2 e2,T3 e3,T4 e4,T5 e5){cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<" "<<e5<<endl;}
template<class T1,class T2,class T3,class T4,class T5,class T6> void deb(T1 e1,T2 e2,T3 e3,T4 e4,T5 e5,T6 e6){cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<" "<<e5<<" "<<e6<<endl;}

#define MAXL 1010
#define MAXS 1000010
#define MAXP 90000
#define INFIN 1001001001

int main()
{
    freopen ("A-large.in", "r", stdin);
    freopen ("A-large.out", "w", stdout);
    int i, j, t, test, tot, cum_sum, smax;
    string str;
    cin >> test;
    for(t=1; t<=test; t++)
    {
        cum_sum = 0;
        tot = 0;
        cin >> smax >> str;
        if( str[0]=='0' )
        {
            tot = 1;
            cum_sum = 1;
        }
        else
        {
            tot = 0;
            cum_sum += (str[0]-'0');
        }
        for(i=1; i<=smax; i++)
        {
            if( str[i]!='0' )
            {
                if( cum_sum < i )
                {
                    tot += ( i - cum_sum );
                    cum_sum += ( i - cum_sum ) + (str[i]-'0');
                }
                else
                    cum_sum += ( str[i] - '0' );
            }
        }
        printf("Case #%d: %d\n", t, tot);
    }
    return 0;
}


