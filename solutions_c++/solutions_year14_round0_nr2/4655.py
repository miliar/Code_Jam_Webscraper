#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>

int main()
{

    int t;
    freopen("E:\\B-small-attempt0.in","r",stdin);
    freopen("E:\\B-small-attempt0.out","w",stdout);
    scanf("%d",&t);
    for(int l=1;l<=t;l++)
    {
        double c,f,x;
        scanf("%lf%lf%lf",&c,&f,&x);
        double sum=100000.0;
        double time=x/2;
        int e=1,r;
        while(sum>time)
        {
            r=e;
            sum=time;
            time=0;
            double s=2;
            e++;
            while(r--)
            {
                time+=c/s;
                s+=f;
            }
            time+=x/s;
        }
        if(sum>time)
        sum=time;
        printf("Case #%d: %.7lf\n",l,sum);
    }
    return 0;
}
