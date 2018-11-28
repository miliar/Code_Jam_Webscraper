#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int main(){
    int T;
    freopen("B-large.in", "r", stdin);
    freopen("b1.txt", "w", stdout);
    scanf("%d", &T);
    for(int t = 0; t < T; t++){
        double c,f,x;
        scanf("%lf %lf %lf", &c, &f, &x);
        if(x / 2 < c / 2 + x / (2 + f)) printf("Case #%d: %.7lf\n", t + 1, x / 2);
        else {
            int tmp =(int)((x * f - 2 * c) / (c * f));
            double ans = 0;
            int i;
            for(i = 0; i < tmp; i++) ans += c / (2 + i * f);
            ans += x / (2 + i * f);
            printf("Case #%d: %.7lf\n", t + 1, ans);
        }
    }
    return 0;
}
