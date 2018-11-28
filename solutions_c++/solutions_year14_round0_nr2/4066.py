#include <iostream>

using namespace std;

int main()
{
    int tc,t;
    double c,f,x,ans,rate=2.0,f1,f2;
    freopen("input.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&tc);
    for(t=1;t<=tc;t++)
    {
        ans=0.0;
        rate=2.0;
        scanf("%lf %lf %lf",&c,&f,&x);
        if(x<=c)
        {
            ans=x/rate;
            //printf("%lf %lf\n",x,rate);
            printf("Case #%d: %0.7lf\n",t,ans);
            continue;
        }
        else
        {
            while(1)
            {
                f1=(c/rate)+(x/(rate+f));
                f2=x/rate;
                //printf("%lf %lf\n",f1,f2);
                if(f2>=f1)
                {
                    //flag=1;
                    ans+=c/rate;
                    rate+=f;
                    //printf("Case #%d: %0.7lf\n",t,ans);
                }
                else
                {
                    ans+=x/rate;
                    //printf("Case #%de: %0.7lf\n",t,ans);
                    break;
                }
            }
        }
        printf("Case #%d: %0.7lf\n",t,ans);
    }
    return 0;
}
