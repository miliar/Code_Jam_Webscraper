#include <iostream>
#include <string.h>
#include <algorithm>
#include <stdio.h>
#include <math.h>
using namespace std;
double a[1010],b[1010];
int main()
{
    freopen("dd.in","r",stdin);
    freopen("out.txt","w+",stdout);
    int ncase,T=0;
    scanf("%d",&ncase);
    while(ncase--)
    {
        printf("Case #%d: ",++T);
        int n;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        scanf("%lf",&a[i]);
        for(int i=0;i<n;i++)
        scanf("%lf",&b[i]);
        sort(a,a+n);
        sort(b,b+n);
        int n1=0,n2=0;
        int now=0;
        for(int i=0;i<n;i++)
        {
            while(now<n&&b[now]<a[i])
            now++;
            if(now>=n)
            {
                n2=n-i;
                break;
            }
            now++;
        }
        int l=0,r=n-1;
        for(int i=0;i<n;i++)
        {
            if(a[i]<b[l])
            {
                if(a[i]<b[r])
                r--;
                else
                {
                    n1++;
                    l++;
                }
            }
            else
            {
                n1++;
                l++;
            }
        }
        printf("%d %d\n",n1,n2);
    }
    return 0;
}
