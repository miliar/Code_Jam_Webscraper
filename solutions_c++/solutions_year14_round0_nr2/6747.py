#include <iostream>
#include <cstdio>
using namespace std;


double tempans, ans, temp, current;
double C, F, X;
int N, n;

int main()
{
    freopen("B_small.in", "r", stdin);
//    freopen("B_small.out", "w", stdout);
    scanf("%d", &N);
    for(int n = 1;n <= N;n++){
        scanf("%lf %lf %lf", &C, &F, &X);
        int num = (int)(X/2.0) + 1;
//            printf("num : %d\n", num);
        ans = X/2.0;
        current = 0.0;
        for(int i = 0;i <= num;i++){
                printf("i: %d\n", i);
            temp = C / (2.0 + i*F);
                printf("temp: %lf\n", temp);
            tempans = current + X / (2.0 + i*F);
                printf("tempans: %lf\n", tempans);
                printf("current: %lf\n", current);
            current += temp;
            ans = ans > tempans ? tempans : ans;
                printf("ans: %lf\n", ans);
        }
        printf("Case #%d: %.7lf\n", n, ans);
    }
    return 0;
}

