#include<stdio.h>
#include<string.h>
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int n,Case = 1;
    double c,f,x;
    scanf("%d",&n);
    while(n--)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        printf("Case #%d: ",Case++);
        if(x < c) printf("%.7lf\n",x/2.0);
        else
        {
            double a = x / 2.0;
            double num = c / 2.0;
            double k = 2.0 + f;
            double b = num + x / k;
            while(a > b)
            {
                a = b;
                num += c / k;
                k += f;
                b = num + x / k;
            }
            printf("%.7lf\n",a);
        }
    }
}
