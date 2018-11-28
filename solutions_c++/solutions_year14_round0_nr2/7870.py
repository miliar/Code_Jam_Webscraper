#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    int t;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for(int cc=1;cc<t+1;cc++)
    {
        double c,f,x,rate=2,t=0;
        scanf("%lf%lf%lf",&c,&f,&x);
        while(1)
        {
            if(c/f<(x-c)/rate)
            {
                t+=c/rate;
                rate+=f;
            }
            else
            {
                t+=x/rate;
                break;
            }
        }
        printf("Case #%d: %.8lf\n",cc,t);
    }
    return 0;
}
