#include <cstdlib>
#include <cstdio>
#include <iostream>
using namespace std;

int main(){
    int cn;
    double C, F, X;
    scanf("%d", &cn);
    for(int ci = 0; ci < cn; ci++){
        scanf("%lf %lf %lf", &C, &F, &X);
        double tmp = X/C - 2/F - 1;
        int n = (int)tmp;
        double t = 0;
        if(tmp >= 0)
        {
            for(int i = 0; i <= n; i++){
                t += C/(2+i*F);
            }
            t += X/(2+(n+1)*F);
        }
        else{
            t += X/2;
        }
        printf("Case #%d: %lf\n", ci+1, t);
    }
}
