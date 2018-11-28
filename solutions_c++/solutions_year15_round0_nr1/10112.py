#include<bits/stdc++.h>
using namespace std;

int A[10010];
int S;
int n;

int main()
{
    #ifdef akid
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    #endif // akid

    int t,cas=1;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&S);
        n=S+1;
        for(int i=0;i<n;i++)
            scanf("%1d",&A[i]);
        int ans=0,sum=0;
        for(int i=0;i<n;i++)
        {
            if(A[i]==0)
                continue;
            if(i==0)
            {
                sum+=A[i];
                continue;
            }

            if(sum>=i)
            {
                sum+=A[i];
            }
            else
            {
                ans+=abs(sum-i);
                sum+=(ans+A[i]);
            }
        }
        printf("Case #%d: %d\n",cas++,ans);
    }
    return 0;
}
