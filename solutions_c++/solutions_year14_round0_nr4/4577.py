#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;
int n;
double a[1010];
double b[1010];
bool va[1010];
bool vb[1010];
int ami()
{
    for(int i=0;i<n;i++)
        if(va[i])
            return i;
}
int bmi()
{
    for(int i=0;i<n;i++)
        if(vb[i])
            return i;
}
int amx()
{
    for(int i=n-1;i>=0;i--)
        if(va[i])
            return i;
}
int bmx()
{
    for(int i=n-1;i>=0;i--)
        if(vb[i])
            return i;
}
int main()
{
    freopen("D-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    int k = 1;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        memset(va,true,sizeof(va));
        memset(vb,true,sizeof(vb));
        for(int i=0;i<n;i++)
            scanf("%lf",&a[i]);
        for(int i=0;i<n;i++)
            scanf("%lf",&b[i]);
        sort(a,a+n);
        sort(b,b+n);
        int ans1=0;
        for(int i=0;i<n;i++)
        {
            int ta = amx();
            int tb = bmx();
            int na = ami();
            int nb = bmi();
            if( a[ta] > b[tb])
            {
                for(int j=na;j<n;j++)
                    if(va[j] && a[j] > b[tb])
                    {
                        ans1++;
                        va[j] = false;
                        vb[tb] = false;
                        break;
                    }
            }
            else
            {
                va[na] = false;
                vb[tb] = false;
            }
        }
        int ans2 = 0;
        memset(vb,true,sizeof(vb));
        for(int i=n-1;i>=0;i--)
        {
            int tmp=-1;
            for(int j=0;j<n;j++)
            {
                if(vb[j]&&b[j]>a[i])
                {
                    tmp = j;
                    ans2++;
                    break;
                }
            }
            if(tmp!=-1)
                vb[tmp] = false;
            else
            {
                for(int j=0;j<n;j++)
                    if(vb[j])
                    {
                        vb[j] = false;
                        break;
                    }
            }

        }
        printf("Case #%d: %d %d\n",k++,ans1,n-ans2);

    }
    return 0;
}
