#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<string.h>
#include<math.h>
#include<vector>
#define LL long long
#define DEBUG if(0)

int main()
{
    int t;
    scanf("%d",&t);
    double c,f,x;
    for (int casen=1;casen<=t;casen++)
    {
        scanf("%lf%lf%lf",&c,&f,&x);

        double time, timespent=0,answer, cookies;
        int farms=0;
       /* time = c/2;
        farms=1;*/
        //if (if c>x)
       // answer=f/2;

        timespent=0;
        cookies=c;

        while(1)
        {
            if( ((x-c)/(2 + farms*f)) > (x/(2 + (farms+1)*f)) )
            farms++;
            else
            break;
        }

        for (int i=0;i<farms;i++)
        {
            timespent= timespent + c/(2 + i*f);
        }

        timespent = timespent + x/(2 + farms*f);


        printf("Case #%d: %.7lf\n",casen,timespent);
       //  printf("Case #%d: %d\n",casen,farms);




    }


}
