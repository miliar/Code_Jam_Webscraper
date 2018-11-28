#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int test,d,mx,ans,sum;
    scanf("%d",&test);
    for(int t=1;t<=test;t++)
    {
        int arr[1005]={0},mx=0;
        scanf("%d",&d);
        for(int i=1;i<=d;i++)
        {
            scanf("%d",&arr[i]);
            mx=max(mx,arr[i]);
        }
        ans=10000000;
        for(int i=1;i<=mx;i++)
        {
            sum=0;
            for(int j=1;j<=d;j++)
            {
                if(arr[j]>i)
                {
                    sum+=((arr[j]+i-1)/i)-1;
                }
            }
            ans=min(ans,sum+=i);
        }

        printf("Case #%d: %d\n",t,ans);

    }
    return 0;
}
