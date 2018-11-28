#include<stdio.h>

int main(int argc, char **argv) {
    int t, cas;
    double ans, cp, c, f, x;
    
    //freopen(argv[1],"r",stdin);
    scanf("%d",&t);
    
    for (cas=1; cas<=t; cas++) {
        scanf("%lf%lf%lf",&c,&f,&x);
        
        ans = 0;
        cp = 2;
        while (c/cp + x/(cp+f) <= x/cp) {
              ans = ans + c/cp;
              cp = cp + f;
        }
        ans = ans + x/cp;
        
        printf("Case #%d: %.7f\n", cas, ans);
    }
        
    return 0;
}
