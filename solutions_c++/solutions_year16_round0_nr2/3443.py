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
  //freopen("B-large.in","r",stdin);
  //freopen("output.txt","w",stdout);

ll t,p,n,ans,i,j,flag1,flag2;
rd(t);
  // while(t--)
  rep(p,1,t+1)
   {
     string str;
    // getline(cin,str);
    cin>>str;
     n=str.size();
     ans=0;
    // rep(i,0,n)
    i=0;
       if(i==0 && str[i]=='-')
       {
          while(i<n && str[i]=='-')
          {
            i++;
          }
          ans++;
       }

       for(j=i;j<n;)
       {
         flag1=flag2=0;

         while(j<n && str[j]=='+'){
           j++;
          flag1=1;

         }


         while(j<n && str[j]=='-')
         {
           j++;
          flag2=1;

         }

        if(flag1 && flag2)
         ans+=2;
       }

      printf("Case #%lld: %lld\n",p,ans);

   }

   return 0;
}
