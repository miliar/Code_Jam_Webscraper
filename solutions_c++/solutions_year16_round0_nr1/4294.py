/**



   Pradip chandra karmaker
   Comilla University(6th_ICT)
*/



#include<bits/stdc++.h>
using namespace std;
#define xx first
#define yy second
#define pb push_back
#define mp make_pair
#define clr(a) memset(a,0,sizeof a)
#define neg(a) memset(a,-1,sizeof a)
#define Sort(a) sort(a.begin(),a.end())
#define All(a) a.begin(),a.end()
typedef long long i64;
typedef pair<int,int> pi;
#define mod 1000000007LL





template<class T>T Bitcnt(T a){int sum=0;while(a){if(a&1)sum++;a/=2;}return sum;}
template<class T>T Max3(T a,T b,T c){return max(a,max(b,c));}
template<class T>T Lcm(T a,T b){T tmp=__gcd(a,b);return (a/tmp)*b;}
template<class T> T Pow(T a,T b){T ans=1;T base=a;while(b){if(b&1)ans=(ans*base);base=(base*base);b/=2;}return ans;}
i64 Bigmod(i64 a,i64 b)
{
    i64 res=1;
    i64 pw=a%mod;
    while(b>0)
    {
       if(b&1)res=(res*pw)%mod;
       pw=(pw*pw)%mod;
       b/=2;
    }
    return res;
}


#define s1(a) scanf("%d",&a)
#define s2(a,b) scanf("%d %d",&a,&b)
#define s3(a,b,c) scanf("%d %d %d",&a,&b,&c)
#define sl1(a) scanf("%lld",&a)
#define sl2(a,b) scanf("%lld %lld",&a,&b)
#define sl3(a,b,c) scanf("%lld %lld %lld",&a,&b,&c)
#define p1(a) printf("%d",a)
#define p2(a,b) printf("%d %d",&a,&b)
#define NL printf("\n")
#define N 4000000
#define rep(i,a,b)    for(int i=a;i<=b;i++)
#define rrep(i,b,a)   for(int i=b;i>=a;i--)
#define fs(i,a,s)     for(int i=a;s[i];i++)

int a_x[]={1,-1,0,0};
int a_y[]={0,0,1,-1};
i64 X,Y;

void extend_euclid(i64 a,i64 b)
{
    if(b==0)
    {
        X=a;Y=0;return;
    }
    extend_euclid(b,a%b);
    i64 x,y;
    x=Y;
    y=X-(a/b)*Y;
    X=x;
    Y=y;
}
i64 inverse_modulo(i64 a,i64 b)
{
    extend_euclid(a,b);
    return (X+mod)%mod;
}

/** dijkstra,bitmask,ME,scc,backtraking,grid dp,segment tree,bit,LCA,bfs,dfs,BPM,MAX_FLOW,MCM,Tree dp,kmp,MST,Meet in the middle*/

/**Triangle characteristics,Phi,bitwise_seive,SOD,articulation,topological,HLD,Z,knapsack,Coin,Digit,LIS,LCS,minimum vertex
cover,josephus,chinese remainder,square root decomposition,ternary search,binary search,Number of theory(divisor,prime),chinese remainder,Generic functoin,Convex hull*/

/*************************************************************************************************************************************************************************************************/

bool ok[20];
int main()
{
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);

    int t;
    s1(t);

     rep(ca,1,t)
      {
          i64 n;
          sl1(n);
          memset(ok,0,sizeof ok);
          if(n==0)
          {
              printf("Case #%d: INSOMNIA\n",ca);

          }
          else
          {
              i64 t=1;
              while(1)
              {
                  i64 tmp=n*t;
                   while(tmp)
                   {
                       int rem=tmp%10;
                       tmp/=10;
                       ok[rem]=1;

                   }
                   int yes=1;
                 for(int i=0;i<=9;i++)if(ok[i]==0)yes=0;
                 if(yes){
                    printf("Case #%d: %lld\n",ca,n*t);break;}
                 else t++;
              }
          }
      }
   return 0;
}


