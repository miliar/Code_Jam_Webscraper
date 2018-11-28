#include <cstdio>
int t,times;
double C,F,X;

int main(){
freopen ("B-large.in","r",stdin);
freopen ("B-large.out","w",stdout);
t = times = 0;
C = F = X = 0;
    scanf ("%d",&times);
    for (t=1;t<=times;t++){
        double sum=0,curpro=2;
        scanf ("%lf%lf%lf",&C,&F,&X);
        while (C/curpro+X/(F+curpro)<X/curpro){
            sum += C/curpro;
            curpro += F;
        }
        sum += X/curpro;
        printf ("Case #%d: %.7lf\n",t,sum);
    }

return 0;
}
