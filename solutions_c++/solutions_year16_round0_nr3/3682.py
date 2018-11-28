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
#define N 100000000
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

vector<i64>lst;
bool check(int value,int p)
{
      return (value &(1<<p));
}
int Set(int value,int p)
{
  return (value |(1<<p));
}

int n,J;

int arr[(100000000/31)+10];
vector<int>p;
void seive()
{
   for(int i=3;i<=sqrt(N);i+=2)
  {
      if(check(arr[i/31],i%31)==0)
      {
          if(i>=10000)continue;
         for(int j=i*i;j<=N;j+=2*i)
         {
            arr[j/31]=Set(arr[j/31],j%31);
         }
      }
  }
   p.push_back(2);
   for(int i=3;i<=N;i+=2)
      if(!check(arr[i/31],i%31))
        p.push_back(i);
}
void solve(i64 val,int pos)
 {
     if(pos==n)
     {
         lst.pb(val*10+1);
         return;
     }
     solve(val*10+0,pos+1);
     solve(val*10+1,pos+1);
 }

i64 M;
bool oK(i64 val)
{
    i64 s=sqrt(val);
    for(int i=0;i<p.size() && p[i]<=s;i++)
    {
        if(val%p[i]==0)
        {
            M=p[i];
            return 1;
        }
    }
    return 0;
}
int main()
{
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
   int t;
   seive();
//    for(int i=0;i<30;i++)
//        cout<<p[i]<<endl;
    s1(t);
   vector<i64>out[55];
    int cnt=0;
   for(int ca=1;ca<=t;ca++)
   {
      s2(n,J);
      solve(1,2);
      for(int i=0;i<=50;i++)
      out[i].clear();
      cnt=0;
     for(int i=0;i<lst.size();i++)
        {
            int ok=1;

            int yes=1;
            vector<i64>tmp;
            tmp.pb(lst[i]);
            i64 t=lst[i];
             vector<int>d;
             while(t)
             {
                 d.pb(t%10);
                 t/=10;
             }
            for(int j=2;j<=10;j++)
            {
                i64 val=0;
                i64 pow=1;
               for(int k=0;k<n;k++)
               {
                   if(d[k])
                    val+=pow;
                   pow*=j;
               }
               if(oK(val))
               {
                 // if(lst[i]==100111)cout<<"=="<<M<<endl;
                  tmp.pb(M);
                 // v.pb(val);
               }
               else
               {
                   yes=0;break;
               }
            }
            if(yes)
            {
//               for(int i=0;i<v.size();i++)
//                cout<<v[i]<<" ";
//               cout<<endl;
                for(int j=0;j<10;j++)
                    out[cnt].pb(tmp[j]);
                cnt++;
            }
            if(cnt==J)break;
        }
        printf("Case #%d:\n",ca);
        for(int i=0;i<cnt;i++)
        {
            if(i)puts("");
            for(int j=0;j<out[i].size();j++)
            {
                if(j)printf(" ");
                printf("%lld",out[i][j]);
            }
        }
   }

   return 0;
}



