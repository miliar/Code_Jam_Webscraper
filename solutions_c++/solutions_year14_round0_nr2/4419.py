#include<iostream>
#include<string>
#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#include<math.h>
#include<set>
#include<map>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large-0.out","w",stdout);
    int ti,t;
    cin>>ti;
    for(t=1;t<=ti;t++)
    {
        double c,f,x,a,tim;
        cin>>c>>f>>x;
        if(x<=c)
        {
           printf("\nCase #%d: %0.7Lf",t,x/2);
           //continue;
        }
        else
        {
            a=0;
            double sp=2.0;
            tim=0;
            while(1)
            {
                tim+=c/sp;
                a+=c;
                if( x/(sp+f) < (x-a)/sp )
                {
                    sp+=f;
                    a-=c;
                }
                else
                {
                    tim+= (x-a)/sp;
                    break;
                }
            }
              printf("\nCase #%d: %0.7Lf",t,tim);
        }
    }
   return 0;
}
