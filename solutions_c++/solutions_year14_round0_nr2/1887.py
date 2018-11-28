#include <iostream>
#include <stdlib.h>
#include <cstdio>
#include <fstream>
using namespace std;
int main()
{
    int i,j,k,l;
    int t;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
            double c,f,x,g,p,time=0.0,r;int ter=1;
            scanf("%lf",&c);
            scanf("%lf",&f);
            scanf("%lf",&x);
            g=x/2.0;
            p=(c/2.0)+(x/(2.0+f));
            {
                if(g>p)
                    {ter=1;time+=c/2.0;}
                else
                    {ter=0;time+=g;}
            }

            r=2.0+f;
            while(ter==1)
            {
                g=x/r;
                p=(c/r)+(x/(r+f));
                if(g>p)
                {

                    time+=c/r;

                    ter=1;
                    r=r+f;
                }
                else
                {
                    time+=g;
                    ter=0;
                }

            }
            printf("Case #");printf("%d",k);printf(": ");printf("%.7lf\n",time);

    }
}
