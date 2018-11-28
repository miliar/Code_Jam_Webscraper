#include<bits/stdc++.h>
using namespace std;
int main(){

    freopen("B-small-attempt3.in","r",stdin);
    freopen("out","w",stdout);
    int t,C=0,n,m,i,j;
    double a1,b1,c1,a2,b2,c2,V,X,q,w;
    scanf("%d",&t);
    while(t--){
        scanf("%d%lf%lf",&n,&V,&X);
        //if(C==31) printf("(%d,%lf,%lf)\n",n,V,X);
        b1=0;
        for(i=0;i<n;i++){
            scanf("%lf%lf",&q,&w);
            //if(C==31) printf("(%lf,%lf)\n",q,w);
            if(i==0) a1=q,a2=q*(w-X);
            if(i==1) b1=q,b2=q*(w-X);
        }
        printf("Case #%d: ",++C);
        c1=V,c2=0;
        if(n==1){
            if(w!=X) puts("IMPOSSIBLE");
            else printf("%.10lf\n",V/q);
            continue;
        }
        if(a2==0 || b2==0){
            if(a2!=0) a1=0;
            if(b2!=0) b1=0;
            printf("%.10lf\n",V/(a1+b1));
            continue;
        }
        else if(a2<0 && b2>0 || a2>0 && b2<0){
            double dx,dy,dd;
            dd=a1*b2-a2*b1;
            dx=c1*b2-c2*b1;
            dy=a1*c2-a2*c1;
            printf("%.10lf\n",max(dx/dd,dy/dd));
        }
        else puts("IMPOSSIBLE");

    }
}

