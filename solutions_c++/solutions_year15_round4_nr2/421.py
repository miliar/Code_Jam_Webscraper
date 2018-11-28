#include <bits/stdc++.h>

using namespace std;
double eps=0.00001;
int main()
{
    int t;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int idx=1;
    scanf("%d",&t);
    while(t--)
    {
        int n;
        scanf("%d",&n);
        double V,T;
        scanf("%lf%lf",&V,&T);
        if(n==1)
        {
            double R,C;
            scanf("%lf%lf",&R,&C);
            if(fabs(C-T)<eps)
            {
                double x=V/R;
                printf("Case #%d: %.8lf\n",idx++,x);
                continue;
            }
            else
            {
                printf("Case #%d: IMPOSSIBLE\n",idx++);
                continue;
            }
        }
        else
        {
            double R1,C1,R2,C2;
            scanf("%lf%lf",&R1,&C1);
            scanf("%lf%lf",&R2,&C2);

            if(fabs(C1-C2)<eps)
            {
                if(fabs(C1-T)<eps)
                {
                    double out=V/(R1+R2);
                    printf("Case #%d: %.8lf\n",idx++,out);
                    continue;
                }
                else
                {
                    printf("Case #%d: IMPOSSIBLE\n",idx++);
                    continue;
                }
            }
            double x=V*(T-C2)/(C1-C2);
            double y=V-x;
            if(x<0.00||y<0.00)
            {
                printf("Case #%d: IMPOSSIBLE\n",idx++);
                continue;
            }
            double out=max(x/R1,y/R2);
            printf("Case #%d: %.8lf\n",idx++,out);
        }
    }
    return 0;
}
