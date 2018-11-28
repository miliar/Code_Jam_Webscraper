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





int main()
{
  //freopen("A-large.in","r",stdin);
 //freopen("out.txt","w",stdout);

ll p,t,n,i;

rd(t);
  // while(t--)
  rep(p,1,t+1)
   {
     string s;
     cin>>s;
     n=s.length();

     string ans="";//s[0];
     ans+=s[0];
     rep(i,1,n)
     {
        if(s[i]>=ans[0])
         ans = s[i]+ans;
        else
         ans+=s[i];
     }

     cout<<"Case #"<<p<<": "<<ans<<endl;




   }

   return 0;
}
