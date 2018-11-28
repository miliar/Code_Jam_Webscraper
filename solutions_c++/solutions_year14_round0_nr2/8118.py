#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

int main()
{
    FILE *fp;
    fp=fopen("xyz.txt","w");
    int t;
    scanf("%d",&t);
    int l=0;
    while(t--)
    {

    l++;
    double  c,f,x;
    scanf("%lf%lf%lf",&c,&f,&x);
    double  s=2;
    double  ans=0;
    while(1)
    {
        double  t1=x/s;

        double  t2=(c/s)+(x/(s+f));

        if(t1<t2)
        {
            ans+=t1;

            break;

        }
        else
        {
            ans=ans+(c/s);
        }
        s=s+f;
    }
    fprintf(fp,"Case #%d: %.7lf\n",l,ans);
    }
}
