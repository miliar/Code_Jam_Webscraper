#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <map>
using namespace std;

int main(){
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);

    int __tt, T;
    double C, F, X, speed, time;
    int i, j, k;

    while(EOF != scanf("%d", &T)){
        for(__tt = 1; __tt <= T; __tt++){
            speed = 2.0;
            time = 0.0;
            scanf("%lf%lf%lf", &C, &F, &X);
            while(X / speed > (C / speed + X / (speed + F))){
                time += C / speed;
                speed += F;
            }
            time += X / speed;
            printf("Case #%d: %.7lf\n", __tt, time);
        }
    }
    return 0;
}
