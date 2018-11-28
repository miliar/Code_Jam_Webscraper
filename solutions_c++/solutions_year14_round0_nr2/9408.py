#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
using namespace std;

int main(){
    //freopen("input2.in", "r", stdin);
    //freopen("output.txt", "w", stdout);
    double C, F, X;
    int T, _case = 0;
    scanf("%d", &T);
    while(T--){
        double ans = 0;
        scanf("%lf%lf%lf", &C, &F, &X);
        double v = F * X / C;
        //int n = floor((v - 2) / F);
        v = v < 2 ? 2 : v;
        double vc = 2;
        while(vc + F < v){
            ans += C / vc;
            vc += F;
        }
        ans += X / vc;
        printf("Case #%d: %.7lf\n", ++_case, ans);
    }
    return 0;
}
