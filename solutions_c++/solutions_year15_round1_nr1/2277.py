#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int test,mx,n,ans1,ans2;
    int arr[1000+5]={0};
    scanf("%d",&test);
    for(int t=1;t<=test;t++)
    {
        mx=-10,ans1=0,ans2=0;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        {
            scanf("%d",&arr[i]);
            if(i!=0)
               mx=max(mx,arr[i-1]-arr[i]);
        }
         for(int i=0;i<n-1;i++)
         {
             if(arr[i+1]-arr[i] < 0)
                ans1+=arr[i]-arr[i+1];
         }
         for(int i=0;i<n-1;i++)
         {
             if(arr[i]<=mx)
               ans2+=arr[i];
              else
                ans2+=mx;
         }
         printf("Case #%d: %d %d\n",t,ans1,ans2);
    }
    return 0;
}
