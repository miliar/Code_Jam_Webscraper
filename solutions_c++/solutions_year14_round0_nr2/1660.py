#include <cstdio>
#include <cstdlib>
#include <vector>
#include <iostream>
using namespace std;

#define debug(v) cerr << #v << ": " << (v) << endl

double solve(double C, double F, double X){
    double ans = X;
    double basetime = 0;
    int farm = 0;
    while(basetime <= ans){
        double ratio = farm * F + 2;
        double t1 = C / ratio;
        double t2 = X / ratio;
        if(basetime + t2 < ans){
            ans = basetime + t2;
        }
        basetime += t1;
        farm ++;
    }
    return ans;
}

int main(){
    int T;
    scanf("%d", &T);
    for(int t = 0; t < T; ++t){
        double C,F,X;
        scanf("%lf%lf%lf", &C,&F,&X);
        printf("Case #%d: %.7lf\n", t + 1, solve(C,F,X));
    }
    return 0;
}
