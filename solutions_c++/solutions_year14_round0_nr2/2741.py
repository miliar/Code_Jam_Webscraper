#include <cstdio>

#define REP(n,i) for(int i=0;i<n;i++)

int main(){
    int T,c=0;
    freopen("B-large.in","r",stdin);
    freopen("b.out","w",stdout);
    scanf("%d",&T);
    double C,F,X;
    
    while((c++)<T){
        scanf("%lf %lf %lf",&C,&F,&X);
        double r=2;
        double t=(C/r);
        //printf("t %lf",t);
        
        for(;r<(X-C)*F/C;r+=F){
            t+=C/(r+F);
        }
        //printf("%lf\n",r);
        if(r==2)t+=(X-C)/r;
        else t+=(X-C)/(r);
        printf("Case #%d: %.7lf\n",c,t);
    }
}
