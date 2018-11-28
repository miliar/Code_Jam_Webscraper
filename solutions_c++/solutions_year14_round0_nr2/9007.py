#include<stdio.h>
#include<float.h>
int T;
double C,X,F;
double min(double a,double b){
   if(a<b)
       return a;
   return b;
}
int main(){
    scanf("%d",&T);
    for(int caso=1;caso<=T;caso++){
        scanf("%lf %lf %lf",&C,&F,&X);
        double ronda=(double)1;
        double NG=(double)2*ronda;
        double ANT=(C/NG),TXA=(X/NG);
        double TX=(X/NG);
        while(TXA>=TX){
            NG=(double)2+(F*ronda);
            TXA=TX;
            TX=(X/NG)+ANT;
            ANT+=(C/NG);
            ronda++;
        }
        printf("Case #%d: %.7lf\n",caso,TXA);
    }
    return 0;
}
