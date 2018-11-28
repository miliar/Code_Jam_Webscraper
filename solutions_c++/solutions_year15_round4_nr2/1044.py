#include<bits/stdc++.h>
typedef long long int uli;
using namespace std;
const double eps=1e-10;
int main(){
   freopen("bs2.in","r",stdin);   
   freopen("bs2.out","w",stdout);   
   int t;
   scanf("%d",&t);
   for(int tt=1;tt<=t;tt++){
      int n;
      double v,x;
      double r0,x0,r1,x1;
      double ans;
      bool possible=true;
      cin>>n>>v>>x;
      if(n==1){
         cin>>r0>>x0;
         if(x==x0){
            ans=v/r0;
         }
         else possible=false;
      }
      else if(n==2){
         cin>>r0>>x0>>r1>>x1;
         if(x0==x1){
            if(x0==x){
               ans=v/(r0+r1);
            }
            else possible=false; 
         }
         else{
            double v0=(v*x-v*x1)/(x0-x1);
            double v1=v-v0;
            if(x0>x && x1>x)possible=false;
            else if(x0<x && x1<x)possible=false;
            else{
               if(v0<0)v0=0;
               if(v1<0)v1=0;

               double t0=v0/r0;
               double t1=v1/r1;
               ans=max(t0,t1);
            }
         }
      }
      else cout<<"no2"<<endl;
      if(possible) printf("Case #%d: %.9lf\n",tt,ans);
      else printf("Case #%d: IMPOSSIBLE\n",tt);

   }
   return 0;
}
