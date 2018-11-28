#include<cstdio>
#include<cmath>
#include<stdlib.h>
#include<map>
#include<set>
#include<time.h>
#include<vector>
#include<queue>
#include<string>
#include<string.h>
#include<iostream>
#include<algorithm>
using namespace std;
#define eps 1e-8
#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
int num[1005],n;
int main()
{
    int cas;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&cas);
    for(int c=1;c<=cas;c++)
    {
        memset(num,0,sizeof(num));
        scanf("%d",&n);
        int up=0;
        for(int i=0;i<n;i++)
        {
            scanf("%d",&num[i]);
        }
        sort(num,num+n);
        int ans=99999999;
        for(int i=1;i<=num[n-1];i++)
        {
            int t=0;
            for(int j=0;j<n;j++)
            {
                if(num[j]>i)
                {
                    t+=num[j]/i;
                    if(num[j]%i==0)
                        t--;
                }
            }
            t+=i;
            ans=min(ans,t);
        }
        printf("Case #%d: %d\n",c,ans);
    }
    return 0;
}
