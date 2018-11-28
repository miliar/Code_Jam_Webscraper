#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>

using namespace std;

int t,n,k,cases=0,num[1005];
int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("fxxk.out","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        memset(num,0,sizeof(num));
        scanf("%d",&n);
        int maxt=0;
        for(int i=1;i<=n;i++)
        {
            scanf("%d",&k);
            num[k]++;
            maxt=max(maxt,k);
        }
        int ans=maxt;
        for(int i=1;i<maxt;i++)
        {
            int tmpans=i;
            for(int j=maxt;j>i;j--)
                if(num[j]>0)
                {
                    if((j-i)%i==0)
                        tmpans+=(num[j]*((j-i)/i));
                    else
                       tmpans+=(num[j]*((j-i)/i+1));
                }
            ans=min(ans,tmpans);
        }
        printf("Case #%d: %d\n",++cases,ans);
    }
    return 0;
}
