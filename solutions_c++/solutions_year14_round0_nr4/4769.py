#include <iostream>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <limits.h>
#include <set>
#include <stack>
#include <vector>
#include <map>
using namespace std;

int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
    int t;
    scanf("%d",&t);
    int z=1;
    while(t--)
    {
        int n;
        scanf("%d",&n);
        double a[n],b[n];
        bool t1[100]={false};
        bool t2[100]={false};
        for(int i =0;i<n;i++)
            scanf("%lf",&a[i]);
        for(int i=0;i<n;i++)
            scanf("%lf",&b[i]);
        sort(a,a+n);
        sort(b,b+n);
        int w1=0,w2=0;
        for(int  i=n-1;i>=0;i--)
        {
            bool found=false;

            for(int j=0;j<n;j++)
            {
                if(b[j]>a[i]&&!t2[j])
                {
                    t2[j]=true;
                    found=true;
                    break;
                }
            }
            if(!found)
            {
                for(int j=0;j<n;j++)
                {
                    if(!t2[j])
                    {
                        w2++;
                        t2[j]=true;
                        break;
                    }
                }
            }
        }
        for(int i =n-1;i>=0;i--)
        {
            bool found=false;
            for(int j=0;j<n;j++)
            {
                if(a[j]>b[i]&&!t1[j])
                {
                    w1++;
                    t1[j]=true;
                    found=true;
                    break;
                }
            }
            if(!found)
            {
                for(int j=0;j<n;j++)
                {
                    if(!t1[j])
                    {
                        t1[j]=true;
                        break;
                    }
                }
            }
        }
        printf("Case #%d: ",z++);
        printf("%d %d\n",w1, w2);
    }
    return 0;
}
