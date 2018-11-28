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
#define sii(n,m) scanf("%d %d",&n,&m)
#define siii(k,n,m) scanf("%d %d %d",&k,&n,&m)
#define rep(i,n) for(i=0;i<n;i++)
#define fu(i,a,n) for(i=a;i<=n;i++)
#define fd(i,n,a) for(i=n;i>=a;i--)
#define ll long long
#define ii pair<int,int>
#define iii pair<ii,int>
#define ff first 
#define ss second
#define mod 1000000007
#define MAXN 100005 

int main()
{
     freopen ("B-small-attempt0 (1).in","r",stdin);
     freopen ("B-small-attempt0 (1).out","w",stdout);
     int i,qw,j,t,n,k,l;
     double p[205];
     double ans,it,it1;
     si(t);
     fu(qw,1,t){
          printf("Case #%d: ",qw);
          sii(n,k);
          ans=0;
          rep(i,n)
               scanf("%lf",&p[i]);
          rep(i,1<<(n)){
               if(__builtin_popcount(i)!=k)
                    continue;
               vector<double> v;
               rep(j,n){
                    if(((i>>j)&1)==1)
                         v.push_back(p[j]);
               }

               // rep(j,v.size())
               //      cout<<v[j]<<" ";
               // pn;

               it=0;
               rep(j,(1<<k)){
                    if(__builtin_popcount(j)!=k/2)
                         continue;
                    it1=1;
                    rep(l,k){
                         if(((j>>l)&1)==1){
                              it1*=v[l];
                              // printf("Yes %lf\n",v[l]);
                         }
                         else {
                              it1*=(1-v[l]);
                              // printf("No %lf\n",v[l]);
                         }
                    }
                    it+=it1;
               }
               // cout<<it<<endl;
               if(ans<it)
                    ans=it;
          }
          printf("%.7lf\n",ans);
     }


     return 0;
}    