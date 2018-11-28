#include<cstdio>
int main(){
int test;
freopen("B-large.in","r",stdin);
freopen("outB.txt","w",stdout);
scanf("%d",&test);
for(int n=1;n<=test;n++)
{
    double C,F,X,eff=2.0;
    scanf("%lf%lf%lf",&C,&F,&X);
    double time=X/eff,now=0.0;
    while(1){
        now+=C/eff;
        eff+=F;
        double tmp=now+X/eff;
        if(time<tmp)    break;
        time=tmp;
    }
    printf("Case #%d: %.7f\n",n,time);
}
return 0;
}
