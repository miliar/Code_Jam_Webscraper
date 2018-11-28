//BISMILLAHIR RAHMANIR RAHIM
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<string>
#include<map>
#include<queue>
#include<vector>
#include<iostream>
using namespace std;
#define inf 1<<25
#define sz 2000
double mm;

int main()
{
    int t,i;
    double x,f,c,tt,nt,p;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        tt=0;nt=inf;
        p=2;
        mm=0;
        scanf("%lf %lf %lf",&c,&f,&x);
        while(1)
        {
            nt=x/p;
            tt=c/p;
            if(tt+(x/(p+f))>nt)
            {
                mm+=nt;
                break;
            }
            mm+=tt;
            p+=f;
        }
        printf("Case #%d: %.6lf\n",i,mm);
    }
    return 0;
}


