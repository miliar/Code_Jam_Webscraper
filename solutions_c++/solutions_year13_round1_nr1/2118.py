#include<stdio.h>
#include<stdlib.h>
#include<string.h>
main()
{
    int n;
    scanf("%d",&n);
    for(int k=1;k<=n;k++)
    {
        double r,R;
        double t;
        scanf("%lf %lf",&r,&t);
        R=r+1;
        int count=0;
        double area=(r+R)*(R-r);
        while(area<=t)
        {
            t-=area;
            count++;
            r=R+1;
            R=R+2;
            area=(r+R)*(R-r);
        }
        printf("Case #%d: ",k);
        printf("%d\n",count);
    }
}