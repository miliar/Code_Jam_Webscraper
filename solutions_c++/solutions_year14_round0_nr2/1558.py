#include <cstdio>
#include <vector>

int T;

int main() {
    int T;
    scanf("%d", &T);
    for (int x = 0; x < T; x++) {
        double C, F, X;
        scanf("%lf%lf%lf\n", &C, &F, &X);
        int k = 0;
        double ans = 0;
        while ((X-C)/(2+k*F) > X/(2+(k+1)*F)) {
            ans += C/(2+k*F);
            k++;    
        }
        ans += X/(2+k*F);
        printf("Case #%d: %.8lf\n", x+1, ans);
    }
    return 0;
}
