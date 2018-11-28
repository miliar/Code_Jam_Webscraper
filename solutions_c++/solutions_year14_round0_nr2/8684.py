#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("out1.txt","w",stdout);
    int a,i,co;
    double c,f,x,out,min=99999999,max,start,ptr;
     cin>>a;
    for(i=1;i<=a;i++)
    {
        co=0;
        min=99999999;
        out=0.00000000000;
        ptr=0.0000000000;
        start=2.000000000;
        scanf("%lf %lf %lf",&c,&f,&x);
        do
        {
            out=ptr+x/start;


            if(min>out)
            {
                co=0;

                min=out;
                 ptr=ptr+c/start;

                start=start+f;

            }

            else
            {
                if(co==20)
                {
                    break;
                }
                co++;
                 ptr=ptr+c/start;

                start=start+f;
            }

        }
        while(x<(c+(start*x)/start+f));

        printf("Case #%d: %.7lf\n",i,min);


    }
}
