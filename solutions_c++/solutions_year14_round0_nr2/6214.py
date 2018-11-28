#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    freopen("A-big-practice.in", "r", stdin);
    freopen("A-big-practice.out", "w", stdout);

    int T;
    double C,F,X,curr,time;
    while(scanf("%d",&T)!=EOF)
    {
        for(int k=1;k<=T;k++)
        {
            scanf("%lf%lf%lf",&C,&F,&X);
            curr=2.0;
            time=0.0;
            while(true)
            {
                if(X/curr>C/curr+X/(curr+F))
                {
                    time+=C/curr;
                    curr+=F;
                }
                else
                {
                    time+=X/curr;
                    break;
                }
            }
            printf("Case #%d: %.7f\n",k,time);
        }
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
