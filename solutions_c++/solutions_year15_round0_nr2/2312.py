#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<iostream>
#include<string>
#include<map>
#include<set>
#include<algorithm>
#include<queue>
#include<vector>
#include<time.h>
using namespace std;
int p[1005];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.out","w",stdout);
    int t,ca=0;
    scanf("%d",&t);
    while(t--)
    {
        int d,ma=0;
        scanf("%d",&d);
        for(int i=0;i<d;++i)
        {
            scanf("%d",p+i);
            ma=max(p[i],ma);
        }
        int ans=1<<30;
        for(int i=1;i<=ma;++i)
        {
            int cnt=i;
            for(int j=0;j<d;++j)
                if(p[j]>i)
                    cnt+=(int)ceil(p[j]*1.0/i)-1;
            //printf("%d:%d\n",i,cnt);
            ans=min(ans,cnt);
        }
        printf("Case #%d: %d\n",++ca,ans);
    }
}
