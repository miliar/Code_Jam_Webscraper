#include <cstdio>
#include <iostream>
using namespace std;
int main(){
    int t;
    scanf("%d",&t);
    for(int count =1; count <=t; count++){
        double C, F, X;
        scanf("%lf %lf %lf",&C,&F,&X);
        double t, prod = 2.0, c=0;
        double likethis=X/prod;
        double ifch;
        t=0;
        while(true){
            likethis= t + X/prod;
            double nextfab=C/prod;
            ifch = t + nextfab + X/(prod + F);
            if(likethis < ifch){
                t=likethis;
                break;
            }
            else{
                t = t+nextfab;
                prod = prod + F;
            }
            
        }
        printf("Case #%d: %.8lf\n", count, t);
    }
    return 0;
}
