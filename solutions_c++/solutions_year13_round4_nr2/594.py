#include<stdio.h>
#include<iostream>
using namespace std;
long long a,b,c,d,e,f,g,h,i,bil,jum;
long long zz[55];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    a=2;
    zz[0]=0;
    for (b=1;b<=52;b++)
    {
        zz[b]=a-1;
        a*=2;
    }
    scanf("%I64d",&a);
    for (b=1;b<=a;b++)
    {
        scanf("%I64d %I64d",&c,&d);
        bil=2;
        for (e=2;e<=c;e++)
            bil*=2;
        f=bil-d;
        for (e=0;e<=51;e++)
        {
            if (f<=zz[e]) {g=e; break;}
        }
        for (e=0;e<=51;e++)
        {
            if (d<=zz[e]) {h=e;break;}
        }
        //printf("%I64d\n",h);
        printf("Case #%I64d: %I64d %I64d\n",b,min(bil-1,zz[c-g+1]-1),bil-zz[c-h+1]-1);
    }
    return 0;
}

