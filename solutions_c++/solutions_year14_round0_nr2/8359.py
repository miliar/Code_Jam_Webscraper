/// Google Code Jam 2014 Quals
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <map>
#include <cstring>
#include <string>
#include <cstdio>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B_answer.txt","w",stdout);
    int t,T,i,n,m;
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        double c,f,x;
        scanf("%lf %lf %lf",&c,&f,&x);
        double time = 0.0, cps=2.0;
        double cookies = 0;
        while(1)
        {
            double bnw = c/cps;
            double w8 = x/cps;
            double bl8r = x/(cps+f);
//            printf("%lf %lf %lf\n",w8,bnw,bl8r);
            if(bnw+bl8r<w8)
            {
                time+=bnw;
                cps+=f;
            }
            else
            {
                time+=w8;
                break;
            }
        }
        printf("Case #%d: %.7lf\n",t,time);
    }

}
