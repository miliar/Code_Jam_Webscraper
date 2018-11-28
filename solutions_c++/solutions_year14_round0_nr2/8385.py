#include <iostream>
#include <fstream>
#include <cstdio>

using namespace std;

int main() {
    int t;
    freopen("1.txt", "r", stdin);
    freopen("2.txt", "w", stdout);
    scanf("%d", &t);
    for(int i = 1; i <= t; i++) {
        double c, f, x;
        cin >> c >> f >> x;
        if(x <= c) {
            double res = (double)x/(double)2;
            printf("Case #%d: %.7lf\n", i, res);
        }else {
            double p = (double)c / (double)2;
            double mn1 = p;
            double cf = 2;
            int ct = 1;
            double xx = x;
            double ans = x/2.0;
            while(xx>=c) {
                cf = cf + f;
                xx -= c;
                if((mn1+x/cf) < ans) {
                    ans = mn1 + x/cf;
                }
                mn1 += c/cf;
            }
            printf("Case #%d: %.7lf\n", i, ans);
        }
    }
    return 0;
}
