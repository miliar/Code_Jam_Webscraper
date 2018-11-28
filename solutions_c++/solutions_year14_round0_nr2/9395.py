#include<stdio.h>

int main(){
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int i, j, T, abc;
    double ans, C, F, X;
    scanf("%d", &T);
    for(abc=0;abc<T;abc++){
        scanf("%lf %lf %lf", &C, &F, &X);
        ans = X/2.0;
        for(i=0;i<100000;i++){
            double tmp = ((double)X)/(F*i+2);
            for(j=0;j<i;j++)
                tmp += ((double)C)/(2+F*j);
            if(tmp > ans)break;
            ans = tmp;
        }
        printf("Case #%d: %.7lf\n", abc+1, ans);

    }
}
