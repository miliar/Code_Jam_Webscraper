#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    double c, f, x, p, fp, tp;
    int t, count = 0;
    scanf("%d",&t);
    while(t--)
    {
        p = 0;
        count++;
        scanf("%lf %lf %lf",&c,&f,&x);
        fp = 2.0;
        tp = x / 2.0;
        if(x!=2)
        {
            while(1)
            {
                p += (c/fp);
                fp += f;
                if(tp >= p + (x/fp))
                    tp = p + (x/fp);
                else
                    break;
            }
        }
        printf("Case #%d: %.7lf\n",count,tp);
    }
    return 0;
}
