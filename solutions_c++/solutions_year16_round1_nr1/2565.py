//Mitesh Agrawal
#include <bits/stdc++.h>
using namespace std;
 
#define gc getchar
#define pi(n) printf("%d",n)
#define pin(n) printf("%d\n",n)
#define pis(n) printf("%d ",n)
#define pll(n) printf("%d",n)
#define plls(n) printf("%lld ",n)
#define plln(n) printf("%lld\n",n)
#define ps printf(" ")
#define pn printf("\n")
#define si(n) scanf("%d",&n)
#define sii(n,m) scanf("%lld %lld",&n,&m)
#define siii(k,n,m) scanf("%lld %lld %lld",&k,&n,&m)
#define rep(i,n) for(i=0;i<n;i++)
#define fu(i,a,n) for(i=a;i<=n;i++)
#define fd(i,n,a) for(i=n;i>=a;i--)
#define ll long long
#define ii pair<ll,ll>
#define iii pair<ii,ll>
#define ff first 
#define ss second
#define mod 10000000007
#define MAXN 100005 

int main()
{
     freopen ("A-large.in","r",stdin); 
     freopen ("A-large.out","w",stdout); 
     string s;
     string t;
     int i,j,l,test,qw;
     si(test);
     fu(qw,1,test){
          cin>>s;
          t.clear();
          l=s.size();
          t=s[0];
          for(i=1;i<l;i++){
               if(t[0]>s[i]){
                    t+=s[i];
               }
               else{
                    t=s[i]+t;
               }
          }
          printf("Case #%d: ",qw);
          cout<<t<<endl;
     }
     



     return 0;
}      