#include<iostream>
#include<algorithm>
#include<cstring>
#include<ctime>
#include<cmath>
#include<string>
#include<cstdio>
#include<vector>
using namespace std;


int main() {
//    freopen("B1.in", "r", stdin);
//    freopen("B1.out", "w", stdout);
    int t;
    double c, f, x;
    scanf("%d", &t);
    for(int cas = 1; cas <= t; ++cas) {
        scanf("%lf%lf%lf", &c, &f, &x);
        double s = 0, sf = 0;
        double t1 = 0;
        double t2 = 0;
        while(1) {
            t2 = t1 + x / (sf + 2);
            t1 += c / (sf + 2);
            sf += f;
            if(t2 <= t1 + x / (sf + 2)) break;
        }
        printf("Case #%d: %.7lf\n", cas, t2);
    }
    return 0;
}
