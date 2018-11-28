#include <iostream>
#include <cstdio>
using namespace std;
#define EPS 1e-8

int main(){
    int t;
    cin >> t;
    for(int i = 1; i <= t; i ++){
        double C, F, X, V, ans=0.0;
        cin >> C >> F >> X;
        V = 2.0;
        while(1) {
            double t1 = X/V;
            double t2 = C/V + X/(V+F);
            if (t1 > t2){
                ans += C/V;
                V += F;
            } else {
                ans += t1;
                break;
            }
        }
        printf("Case #%d: %.7f\n", i, ans);

    }
    return 0;
}
