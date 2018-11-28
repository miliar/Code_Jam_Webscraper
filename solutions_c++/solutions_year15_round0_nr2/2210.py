#include <iostream>
#include <stdlib.h>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <string>
#include <vector>
#include <queue>
#define lson l,m,rt<<1
#define rson m+1,r,rt<<1|1
#define MAXN 100010
#define eps 1e-5
#define pi acos(-1.0)
using namespace std;
int cnt[2000];
vector<int> q;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output2.txt","w",stdout);
    int t,T,n,a[2000];
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        scanf("%d",&n);
        for(int i=0;i<n;i++)
            scanf("%d",&a[i]);
        sort(a,a+n);
        int time=a[n-1];
        for(int i=a[n-1];i>=1;i--)
        {
            int mm=0;
            for(int j=n-1;j>=0;j--)
            {
                if(a[j]<=i)
                    break;
                if(a[j]%i==0)
                    mm+=a[j]/i-1;
                else
                    mm+=a[j]/i;
            }
            time=min(time,mm+i);
        }
        printf("Case #%d: %d\n",t,time);
    }
    return 0;
}
