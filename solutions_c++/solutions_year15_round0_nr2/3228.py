#include<iostream>
#include<cstdio>
#include<memory.h>
#include<algorithm>
#include<math.h>
#include<limits.h>
#define s(n) scanf("%d",&n)
using namespace std;
#define lint unsigned long long int
#define mod 1000000007
int arr[1000001];
int maxm(int a,int b)
{
    if(a>b)
    return a;
    return b;
}
int main()
{
   freopen("B-large.in","r",stdin);
  freopen("output2blarge.txt","w",stdout);
    int t,i;
    s(t);
    for(int j=1;j<=t;j++)
    {
        int n;
        s(n);
      //  int arr[n];
        int max=0,temp;
        int ind=-1,cnt=0;
        for( i=1;i<=n;i++)
        {
            s(arr[i]);
            if(arr[i]>max)
            {
                max=arr[i];
                ind=i;
            }
        }
        int ans=max;
        for(int k=max;k>=1;k--)
        {
            cnt=0;
            for(i=1;i<=n;i++)
            {
                if(arr[i]>k)
                {
                    cnt=cnt+arr[i]/k;
                if(arr[i]%k ==0)
                   cnt--;
                    ind=i;
                    temp=arr[i];
                    max=maxm(arr[i]/k,arr[i]%k);
                    //arr[i]=maxm(arr[i]/k,arr[i]%k);
                }
            }
          //  cout<<"k"<<k<<"cnt"<<cnt<<endl;
            //max=0;
         /*   for(i=1;i<=n;i++)
            {
                if(arr[i]>max && i!=ind)
                max=arr[i];
            }*/
            ans=min(ans,k+cnt);
          //  cout<<ans<<endl;
        }



       printf("Case #%d: %d\n",j,ans);
    }
return 0;
}
