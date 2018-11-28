#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int T,n;

double v,x,r[233],c[233];

int main(){
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    scanf("%d",&T);
for(int t=1;t<=T;t++){
    scanf("%d",&n);
    scanf("%lf%lf",&v,&x);
    for(int i=1;i<=n;i++)scanf("%lf%lf",&r[i],&c[i]);

      printf("Case #%d: ",t);
    if(n==1){
        if(x!=c[1])printf("IMPOSSIBLE\n");
        else printf("%.9lf\n",v/r[1]);
    }

    if(n==2){
    if(c[2]>x && c[1]>x){printf("IMPOSSIBLE\n");continue;}
    if(c[2]<x && c[1]<x){printf("IMPOSSIBLE\n");continue;}
    double ne1,ne2;
    ne2=(x*v-c[1]*v)/(c[2]-c[1]);
    ne1=v-ne2;
    double ans;
    ans=max(ne1/r[1],ne2/r[2]);
    if(c[2]==c[1])ans=v/(r[1]+r[2]);
   // printf("v=%.9lf x=%.9lf\n c1=%.9lf  c2=%.9lf\n ne1=%.9lf ne2=%.9lf\n",v,x,c[1],c[2],ne1,ne2,ans);
   printf("%.9lf\n",ans);
    }
}
    return 0;
}
