#include <cstdio>
#include <cstring>
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T,pos = 0;
    double C,F,X,ans,time,now;
    scanf("%d",&T);
    while(T --)
    {
        time = 0;
        now = 2;
        printf("Case #%d: ",++ pos);
        scanf("%lf %lf %lf",&C,&F,&X);
        while(1)
        {
            if(X / now  <= (C / now) + (X / (now + F)))
                {
                    time += (X / now);
                    break;
                }
            else
            {
                    time += (C / now);
                    now += F;
            }
        }
        printf("%0.7lf\n",time);
    }
    return 0;
}
