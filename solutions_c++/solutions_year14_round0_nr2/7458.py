#include <stdio.h>

int main()
{
    int n;
    double time[100];
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        time[i]=0.0;
        int j;
        double c;
        double f;
        double x;
        scanf("%lf%lf%lf",&c,&f,&x);
        double num1;
        int num;
        num1=((x-c)/c-2.0/f);
        num=(int)num1;
        if(num1<0)
            time[i]=x/2.0;
        else
        {
            for(j=0;j<(num+1);j++)
                time[i]+=c/(2.0+j*f);
            time[i]+=x/(2.0+j*f);
        }

    }
    for(int x=0;x<n;x++)
        printf("Case #%d: %.7lf\n",x+1,time[x]);
    return 0;

}
