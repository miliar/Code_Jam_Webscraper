#include<cstdio>
using namespace std;
double c,f,x,sum,d;
int X;
int main()
{int t;
    scanf("%d",&t);
    while(t--)
    {X++;
        sum=0.0;
        scanf("%lf %lf %lf",&c,&f,&x);
        d=2.0;
        while((x/d)>((c/d)+(x/(d+f))))
        {
            sum+=(c/d);
            d=d+f;
        }
        sum+=(x/d);
        printf("Case #%d: %.7lf\n",X,sum);
    }
return 0;
}
