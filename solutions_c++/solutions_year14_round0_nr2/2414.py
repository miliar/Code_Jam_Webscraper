#include <cstdio>

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int n, cc = 0;
    double C, F, X, ans;
    scanf("%d", &n);

    while ( n --){
        scanf("%lf%lf%lf", &C, &F, &X);
        ans = 0;
        double get[2] = { 2.000000, 0};
        if ( ( X / get[0]) < ( C / get[0] + X / ( F + get[0]))){
            ans = X / get[0];
        }
        else{
            get[1] = get[0] + F;
            while ( (  X / get[0]) > ( C / get[0] + X / ( get[1]))){
                ans += C / get[0];
                get[0] = get[1];
                get[1] = get[0] + F;
            }
            ans += X / get[0];
        }

        cc ++;
        printf("Case #%d: %.7lf\n", cc, ans);
    }

    return 0;
}
