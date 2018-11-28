#include<stdio.h>

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("b_out.txt","w",stdout);
    double C,F,X;
    int T,n;
    int id = 1;
    double ans;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%lf%lf%lf",&C,&F,&X);
        printf("Case #%d: ", id);
        if(F*X <= 2*C)
        {
            printf("%.7lf\n", X/2);
        }
        else
        {
            n = (X/C) - (2/F);
            ans = X/2;
            if(n >= 1)
            {
                ans = X / (2 + n*F);
                for(int i=0; i<=n-1; ++i) ans += C / (2 + i*F);
                if(ans > X/2) ans = X/2;
            }
            printf("%.7lf\n", ans);
        }
        id++;
    }
    return 0;
}