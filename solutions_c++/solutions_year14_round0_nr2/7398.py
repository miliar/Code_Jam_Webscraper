#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;
const double sp = 2.0;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B.out", "w", stdout);
    double c, f, x, lef, rig, mid, cnt, m;
    int ks, ts;
    scanf("%d", &ts);
    for (ks = 0; ks < ts; ks++){
        scanf("%lf %lf %lf", &c, &f, &x);
        if (x + 1e-9 < c) {
              printf("Case #%d: %.7lf\n", ks + 1, x / 2);
              continue;
        }
        lef = 0.0; rig = x / sp;
        while (lef + 1e-9 < rig){
              mid = (lef + rig) / 2;
              m = mid;
              cnt = sp;
              while (mid * cnt + 1e-9 > c){
                    if (mid * cnt + 1e-9 > x) break;
                    double pt = c / cnt;
             //       if ((mid - pt) * sp < c) break;
                    mid -= pt;
                    cnt += f;
              }
              if (mid * cnt + 1e-9 < x)
                 lef = m;
              else rig = m;
        }
        printf("Case #%d: %.7lf\n", ks + 1, lef);
    }
    return 0;
}
