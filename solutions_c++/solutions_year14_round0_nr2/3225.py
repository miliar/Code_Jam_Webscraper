#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include <algorithm>

using namespace std;

int main()
{
    freopen("1.in","r",stdin);
    freopen("2.txt","w",stdout);
    int T;
    cin>>T;
    for(int l=1; l<=T; l++)
    {
        double c,f,x,sec=0,sum=0;
        cin>>c>>f>>x;
        double t1,t2,t3,t=0,f1=2.0,f2,f3;
        int ll=0;
        while(1)
        {
            t1=c/f1;
            f2=f1+f;
            t2=x/f2;
            t3=x/f1;
            if(t3>t2+t1)
            {
                f1+=f;
                t+=t1;
            }
            else
            {
                t+=t3;
                sec=t;
                break;
            }
        }
        printf("Case #%d: %.7lf\n",l,sec);
    }
    return 0;
}
