#include <iostream>
#include <cstdio>
#include <algorithm>
#define eps 1e-9
using namespace std;
double aa[1005];
double bb[1005];
int cc[1005],dd[1005];
int main()
{
    freopen ("D-large.in", "r", stdin);
    freopen ("D-large.out", "w", stdout);
    int t;
    scanf("%d",&t);
    for(int ii=1;ii<=t;ii++)
    {
        int tt;
        scanf("%d",&tt);
        for(int i=1;i<=tt;i++)
        {
            scanf("%lf",&aa[i]);
            cc[i]=(aa[i]*100000+eps);
        }
        for(int i=1;i<=tt;i++)
        {
            scanf("%lf",&bb[i]);
            dd[i]=(bb[i]*100000+eps);
        }
        sort(cc+1,cc+tt+1);
        sort(dd+1,dd+tt+1);
        int a1=1,b1=1;
        int an1=0,an2=0;
        while(a1<=tt)
        {
            if(cc[a1]>dd[b1])
            {
                an1++;
                a1++;
                b1++;
            }
            else a1++;
        }
        a1=1,b1=1;
        while(b1<=tt)
        {
            if(dd[b1]>cc[a1])
            {
                an2++;
                a1++;b1++;
            }
            else b1++;
        }
        printf("Case #%d: %d %d\n",ii,an1,tt-an2);
    }
}
