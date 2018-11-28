#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <iostream>
using namespace std;
double s1[1002],s2[1002];
int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
    int t,n;
    int ans;
    double c,f,x;
    while(~scanf("%d",&t))
    {
        ans = 1;
        while(t--)
        {
            scanf("%d",&n);
            for(int i = 0;i<n;i++)
                scanf("%lf",&s1[i]);
            for(int i=0; i<n; i++)
                scanf("%lf",&s2[i]);
            sort(s1,s1+n);
            sort(s2,s2+n);
            int num1=0;
            int j = 0;
            for(int i=0;i<n;i++)
            {
                for(;j<n;j++)
                {
                    if(s1[j] - s2[i] > 1e-6)
                    {
                        num1++;
                        j++;
                        break;
                    }
                }
            }
            int num2 = 0;
             j = 0;
            for(int i = 0;i<n;i++)
            {
                for(;j<n;j++)
                {
                    if(s2[j] - s1[i] > 1e-6)
                    {
                        num2++;
                        //printf("num2:%d %d %d\n",i,j,num2);
                        j++;
                        break;
                    }
                }
            }
            printf("Case #%d: %d %d\n",ans++,num1,n-num2);
        }
    }
    return 0;
}

