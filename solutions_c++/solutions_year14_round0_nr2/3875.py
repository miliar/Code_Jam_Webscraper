#include<stdio.h>

int T;
double time,C,F,X;
double solve(){
    int n=(int)(X/C-2/F);
    double ret=0;
    double eff=2;
    for(int i=0;i<n;++i){
        ret+=C/eff;
        eff+=F;
    }
    ret+=X/eff;
    return ret;
}
main(){
    scanf("%d",&T);
    for(int num=1;num<=T;++num){
        scanf("%lf%lf%lf",&C,&F,&X);
        time=solve();
        printf("Case #%d: %-30.7f\n",num,time);
    }
}
