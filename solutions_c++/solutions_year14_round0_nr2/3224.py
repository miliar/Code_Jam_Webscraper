#include<cstdio>
#include<iostream>
using namespace std;

int main()
{
    freopen("bb.in","r",stdin);
    freopen("out.txt","w",stdout);
    int cas;
    double c, f, x, ans;
    scanf("%d",&cas);
    for(int t = 1 ;t <= cas; ++ t)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        double sum = 0;
        double now = 2;
        ans = 0;
        int cnt = 0;
        while(true)
        {
            if(sum + now >= c && ((x - sum) / now > (x - (sum >= c ? (sum - c): 0)) / (now + f) + (sum >= c ? 0 : (c - sum) / now)))
            {
                {
                    if(sum < c)
                    {
                        ans += (c - sum) / now;
                        sum = 0;
                    }
                    else
                    {
                        sum -= c;
                    }
                    now += f;
                }
            }
            else
            {
               if(sum + now >= x)
               {
                   ans += (x - sum)/now;
                   break;
               }

               else
               {
                   ans += 1;
                   sum += now;
               }
            }
        }
        printf("Case #%d: %.7lf\n",t,ans);

    }
    return 0;
}
