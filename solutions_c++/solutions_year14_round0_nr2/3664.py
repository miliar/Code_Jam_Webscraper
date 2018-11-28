#include<stdio.h>
#include<algorithm>
int main(void){
#ifdef _DEBUG
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int T;
    scanf("%d", &T);
    for(int i = 1; i <= T; i++){
        double c, farmProd, x;
        scanf("%lf%lf%lf", &c, &farmProd, &x);
        double res = x/2, mres = x/2, mn = 0;
        int n;
        for(n = 0; res > res + c/(2+farmProd*n) + x/(2+farmProd*(n+1)) - x/(2+farmProd*n); n++)
            res += c/(2+farmProd*n) + x/(2+farmProd*(n+1)) - x/(2+farmProd*n);
        //for(n = 0; n < 1000000; n++)
        //    res += c/(2+farmProd*n) + x/(2+farmProd*(n+1)) - x/(2+farmProd*n),
        //        mres = res > mres ? mres : res;
        //printf("Case #%d: %.8lf\n", i,  res);
        int n10 = n + 10;
        for(n = std::max(0, n-10); n < n10; n++){
            res = 0;
            for(int i = n-1; i >= 0; i--)
                res += c/(2+farmProd*i);
            res += x/(2+farmProd*n);
            if(res < mres)
                mres = res, mn = n;
        }

        printf("Case #%d: %.8lf\n", i,  mres);
    }
    return 0;
}
