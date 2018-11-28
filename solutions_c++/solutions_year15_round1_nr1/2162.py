#include<iostream>
#include<cstdio>
#include<memory.h>
#include<algorithm>
#define s(n) scanf("%d",&n)
using namespace std;
#define lint long long int
int arr[100001];
int main()
{
    freopen("A-large.in","r",stdin);
   freopen("op1smlarge.txt","w",stdout);
    int t,i,j,k;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        int n;
        s(n);
        int arr[n];
        for(i=0;i<n;i++)
        s(arr[i]);
        int ans1=0,ans2=0,max=0;
        for(i=1;i<n;i++)
        {
            int diff=arr[i-1]-arr[i];
            if(diff>0)
            ans1+=diff;
            if(diff>max)
            max=diff;
        }
        for(i=0;i<n-1;i++)
        {
            if(arr[i]<=max)
            ans2+=arr[i];
            else
            {
                ans2=ans2+max;
                //arr[i+1]=arr[i+1]+arr[i]-max;
            }
          //  printf("%d\n",ans2);
        }
        printf("Case #%d: %d %d\n",k,ans1,ans2);
    }
    return 0;
}
