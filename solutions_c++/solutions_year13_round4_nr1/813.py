#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<vector>
#include<map>
#include<queue>
#include<set>
#include<cstring>
#define MAX(a,b) (a>b?a:b)
#define MIN(a,b) (a<b?a:b)
#define pb push_back
#define mp make_pair
#define F first
#define S second
using namespace std;
long long P=1000002013;
const long long n_max=1005;
long long n,m,t,T,a[n_max],b[n_max],c[n_max];
long long ans,q,sum,i,j,k,x,y;
vector<pair<long long,pair<long long,long long> > > v;
long long s1[2005],s2[2005],S;

long long calc(long long a,long long b){
          long long cur,k,x=b-a;

          cur=((n*(n+1))/2 -((n-x+P)*(n-x+1+P))/2)%P;
          return (cur);
}

main()
{freopen("A-large.in","r",stdin);
 freopen("out.txt","w",stdout);
 scanf("%lld",&T);

 for(t=1;t<=T;t++){
     scanf("%lld%lld",&n,&m);
     ans=sum=0;
     S=0;
     for(i=1;i<=m;i++){
          scanf("%lld%lld%lld",&a[i],&b[i],&c[i]);
          ans+=(calc(a[i],b[i])*c[i])%P;
     }
     v.clear();
     for(i=1;i<=m;i++)v.pb(mp(a[i],mp(1,c[i]))),v.pb(mp(b[i],mp(2,c[i])));
     sort(v.begin(),v.end());
     for(i=0;i<v.size();i++)
          if(v[i].S.F==1){
                              S++;
                              s1[S]=v[i].F;
                              s2[S]=v[i].S.S;

          }else{
          q=v[i].S.S;
          while(q){
                y=MIN(q,s2[S]);
                s2[S]-=y;
                q-=y;
                x=s1[S];
                sum+=(calc(x,v[i].F)*y)%P;
                if(s2[S]==0)S--;
          }
          }
     ans-=sum;
      while(ans<0)ans+=P;
      ans%=P;
     cout<<"Case #"<<t<<": "<<ans<<endl;
 }
}
