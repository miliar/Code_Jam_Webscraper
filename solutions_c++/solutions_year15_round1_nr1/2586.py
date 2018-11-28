#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
 int main()
 {
 int t,n,j,ans,ans2,A[10000],i,prev,mx=-1909;
 scanf("%d",&t);
 for(j=1;j<=t;j++)
 {
     scanf("%d",&n);
     for(i=0;i<n;i++)
     {
         scanf("%d",&A[i]);
     }
     prev=A[0];
     ans2=0;
     mx=-1000;
     ans=0;
     for(i=1;i<n;i++)
     {
         mx=max(mx,A[i-1]-A[i]);
         if(A[i]>=prev)
            {
                prev=A[i];
                continue;
            }
         else
            {
                ans=ans+prev-A[i];
                prev=A[i];
            }
     }
     for(i=0;i<n-1;i++)
     {
         if(A[i]>mx)
            ans2=ans2+mx;
         else
            ans2=ans2+A[i];
     }
     if(ans2<0)
        ans2=0;
     printf("Case #%d: %d %d\n",j,ans,ans2);
 }
 }
