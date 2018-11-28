#include <iostream>
#include <cstdio>
#include <math.h>
#include <vector>
#include <string.h>
#include <algorithm>
#include <climits>
using namespace std;
int main()
{
    int i,a1=0,a2=0,b1=0,b2=0,t,n=0,c1=0,c2=0,c=1;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        float a[11]={0},b[11]={0};
        c1=0;
        c2=0;
        a1=0;
        a2=n-1;
        b1=0;
        b2=n-1;
        for(i=0;i<n;i++)
        {
            scanf("%f",&a[i]);
        }
        for(i=0;i<n;i++)
        {
            scanf("%f",&b[i]);
        }
        sort(a,a+n);
        sort(b,b+n);
        for(i=0;i<n;i++)
        {
            if(a[a2]>b[b2])
            {
                a2--;
                b2--;
                c1++;
            }
            else
            {
                a1++;
                b2--;
            }
        }
        a1=0;
        a2=n-1;
        b1=0;
        b2=n-1;
        for(i=0;i<n;i++)
        {
            if(a[a2]>b[b2])
            {
                a2--;
                b1++;
                c2++;
            }
            else
            {
                a2--;
                b2--;
            }
        }
        printf("Case #%d: %d %d\n",c,c1,c2);
        c++;
    }
    return 0;
}
