#include<cstdlib>
#include<cstdio>
#include<iostream>
#include<cstring>
#include<vector>
#include<algorithm>

using namespace std;

double c, f, x;
int t;

int main() {
    freopen("/Users/dong/Downloads/B-large.in", "r", stdin);
    freopen("/Users/dong/Downloads/out4.txt", "w", stdout);
    scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        scanf("%lf%lf%lf", &c, &f, &x);
        double ans = x / 2.0;
        double cnt = 0;
        
        for (int j = 1; j <= 1000000; ++j) {
            double speed = (j-1) * f + 2.0;
            double time = c / speed;
            speed = j * f + 2.0;
            cnt += time;
            if (cnt + x / speed < ans)
                ans = cnt + x / speed;
        }
        
        printf("Case #%d: %.7lf\n", i + 1, ans);
    }
    return 0;
}
