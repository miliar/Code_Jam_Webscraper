#include <iostream>
#include <cstdio>

using namespace std;

double rate(double cspeed, double target){
    return target/cspeed;
}
int main()
{
    int T;
    scanf("%d",&T);
    int z = 1;
    while(T--){
    double C, F, X;
    scanf("%lf%lf%lf",&C,&F,&X);
    double c = 2.0;
    double time = 0.0;
    double Cspeed, Xspeed, Xspeed2;
    while(1){
     Cspeed = rate(c,C);
     Xspeed = rate(c,X);
     if(Xspeed<=Cspeed){
        time = Xspeed;
        break;
     }
     c = c+F;
     Xspeed2 = rate(c,X);
     if(Cspeed+Xspeed2<Xspeed){
        time += Cspeed;
     }
     else{
        time+=Xspeed;
        break;
     }

    }
    printf("Case #%d: %.7lf\n",z,time);

    z++;
   }
    return 0;
}
