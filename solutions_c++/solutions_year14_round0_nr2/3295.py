#include<stdio.h>

void solve()
{
    double C, F, X;
    scanf("%lf %lf %lf", &C, &F, &X);

    double rate = 2, ans = 0;

    while(true)
    {
        if(X/rate > C/rate + X/(rate+F))
        {
            ans += C/rate;
            rate += F;
        }
        else
        {
            ans += X/rate;
            break;
        }
    }
    printf("%.7lf\n", ans);
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("data.txt","r",stdin);
    freopen("out.txt","w",stdout);
#endif

    int T;

    scanf("%d", &T);
    for(int i = 1; i <= T; i++)
    {
        printf("Case #%d: ", i);
        solve();
    }

     return 0; 
}
