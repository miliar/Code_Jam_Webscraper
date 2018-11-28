#include<iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
double a[1001];
double b[1001];
int ans1,ans2;
int n;
void gao1()
{
    ans1=0;
    int ip1=0,ip2=0;
    while(ip1!=n)
    {
        if(b[ip1]>a[ip2])
        {
            ans1++;
            ip1++;
            ip2++;
        }
        else
        ip1++;

    }
    return;
}
void gao2()
{
    ans2=0;
    int ip1=0,ip2=0;
    while(ip1!=n)
    {
        if(a[ip1]>b[ip2])
        {
            ans2++;
            ip1++;ip2++;
        }
        else
            ip1++;
    }
    return ;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cs=1;cs<=T;cs++)
    {
        scanf("%d",&n);
        for(int t=0;t<n;t++)
        {
            scanf("%lf",&a[t]);
        }
         for(int t=0;t<n;t++)
        {
            scanf("%lf",&b[t]);
        }
        sort(a,a+n);
        sort(b,b+n);
        gao1();
        gao2();
        printf("Case #%d: %d %d\n",cs,ans2,n-ans1);
    }
    return 0;
}
