#include <iostream>
#include <cstring>
#include <cstdio>
#include <queue>
#include <stack>
#include <string>
using namespace std;
int arr[2000];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    int n;
    int big;
    int ans;
    cin>>T;
    for(int i=1;i<=T;i++)
    {
        scanf("%d",&n);
        big=0;
        for(int j=1;j<=n;j++)
        {
            scanf("%d",&arr[j]);
            big=max(big,arr[j]);
        }
        ans=big;
        for(int j=2;j<=big;j++)
        {
            int ans1=j;
            for(int k=1;k<=n;k++)
            {
                ans1+=(arr[k]-1)/j;
            }
            ans=min(ans,ans1);
        }
        printf("Case #%d: %d\n",i,ans);
    }
    return 0;
}
