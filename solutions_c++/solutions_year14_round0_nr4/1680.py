#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std;
bool cmp(double a,double  b)
{
    return (a>b);
}
int flag[150];
int main()
{
    freopen("D-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    double naomi[15000],ken[15000];
    int t,n;
    scanf("%d",&t);
    for(int cs=1; cs<=t; cs++)
    {
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        scanf("%lf",&naomi[i]);
        for(int i=0;i<n;i++)
        scanf("%lf",&ken[i]);
        sort(naomi,naomi+n);
        sort(ken,ken+n,cmp);
        int ct=0,large=n-1;
        for(int i=0;i<n;i++)
        {
            if( ken[i]>=naomi[large])
            continue;
            large--;
            ct++;

        }
        int in=n-1,war=0,sm=0;
        sort(ken,ken+n);
        for(int i=n-1;i>=0;i--)
        {
            if(naomi[i]>ken[in])
            {
                war++;

            }
            else
            {
               in--;
            }
        }
//        for(int i=0;i<n;i++)
//        printf("%lf %lf\n",naomi[i],ken[i]);
//        while(naomi[in]>ken[n-1])
//        {
//            in--;
//            ct++;
//
//        }
        printf("Case #%d: %d %d\n",cs,ct,war);


    }
return 0;
}
