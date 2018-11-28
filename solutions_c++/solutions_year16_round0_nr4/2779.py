#include<bits/stdc++.h>

using namespace std;
typedef long long int ll;
typedef vector<ll> vi;
typedef vector<vi> vvi;
typedef pair<ll,ll> ii;
typedef vector<ii> vii;

#define all(x) (x).begin(),(x).end()
#define pb push_back
#define mp make_pair
#define tr(c,it) for(typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define rd(x) scanf("%lld",&x)
#define wr(x) printf("%lld\n",x)
#define rep(i,a,b) for(i=a;i<b;i++)
#define pi 3.141592653589793238462643383279
#define f first
#define s second
#define MOD 1000000007     // 10^9+7
#define INF 1000000008     // 10^9+8

ll fastpow(ll a,ll b)
{
ll   ans=1;
   while(b)
   {
      if(b%2)
       ans*=a;

      a*=a;
      b>>=1;
   }

   return ans;
}

int main()
{
  // freopen("D-small-attempt0.in","r",stdin);
   //freopen("output.txt","w",stdout);

ll t,p,k,c,s,x,prev,i;
rd(t);
  // while(t--)
  rep(p,1,t+1)
   {
      rd(k);
      rd(c);
      rd(s);

      x=fastpow(k,c-1);
      printf("Case #%lld: ",p);
      printf("1 ");
      prev=1;
      for(i=1;i<k;i++)
      {
        printf("%lld ",prev+x);
        prev=prev+x;
      }
      cout<<endl;
   }

   return 0;
}
