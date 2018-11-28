#include <iostream>
#include <stdlib.h>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <vector>
#include <queue>
using namespace std;
int cnt[15];
int main()
{
   freopen("B-small-attempt0.in","r",stdin);
   freopen("out.txt","w",stdout);
    int t,T,n,a[15];
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        scanf("%d",&n);
        for(int i=0;i<n;i++)
            scanf("%d",&a[i]);
        sort(a,a+n);
        int ant=a[n-1];
        for(int i=a[n-1];i>=1;i--)
        {
            int mm=0;
            for(int j=n-1;j>=0;j--)
            {
                if(a[j]<=i)
                    break;
                if(a[j]%i!=0)
                	mm+=a[j]/i;
                else
                    mm+=a[j]/i-1;
            }
            ant=min(ant,mm+i);
        }
        printf("Case #%d: %d\n",t,ant);
    }
    return 0;
}
