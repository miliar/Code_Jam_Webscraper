#include <cstring> 
#include <cstdio>
using namespace std;

int main() {
    freopen("B-large.in","r",stdin);
    freopen("B.out","w",stdout);
    double C, F, X, ans, per, now;
    int T, cas=1;
    scanf("%d", &T);
    while(T--) {
        scanf("%lf %lf %lf", &C, &F, &X);
        per = 2.0;
        now = 0.0;
        ans = 0.0;
        while(1) {
            if(X/per > C/per+X/(per+F)){
                ans += C/per;
                per += F;
            }else {
                ans += X/per;
                break;
            }
        }
        printf("Case #%d: %.7lf\n", cas++, ans);
    }
    return 0;
}
