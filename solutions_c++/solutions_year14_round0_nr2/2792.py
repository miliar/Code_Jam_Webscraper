#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <cstring>
using namespace std;

int main() {
//    freopen("D:\\B-large.in", "r", stdin);
//    freopen("D:\\B-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int z = 1; z <= T; z++) {
        double c, f, x;
        scanf("%lf %lf %lf", &c, &f, &x);
        double temp = 0.0;
        double time = 0.0;
        while (1) {
            if (c/(2.0+(temp*f))+x/(2.0+temp*f+f) >= x/(2+temp*f))
                break;
            else temp += 1.0;
        }
//        printf("%.7lf\n", temp);
        int i = (int)temp;
        for (int j = 0; j < i; j++) {
            time += (c/(2.0+(j*f)));
//            printf("%.7lf\n", time);
        }
        time += x/(2+i*f);
        printf("Case #%d: ", z);
        printf("%.7lf\n", time);
    }
//    printf("%.5lf", 2000.0/16);
    return 0;
}
