#include<iostream>
#include<cstdio>
#include<string>
#include<algorithm>
#include<vector>
#include<cstring>

using namespace std;
int ar[101];
int main()
{
    int n,t,p,k,i,ans,dif;
    long long s,a;
    scanf("%d",&t);
    p=1;
    while(p<=t)
    {
               scanf("%lld %d",&a,&n);
               for(i=0;i<n;i++)
                       scanf("%d",&ar[i]);
               sort(ar,ar+n);
               s=a;
               for(i=0;i<n;i++)
               {
                       if(s>ar[i])
                       s+=ar[i];
                       else break;
               }
               ans=n-i;
               for(k=1;k<=ans;k++)
               {
                       dif=s-1;
                       s=dif+s;
                       for(;i<n;i++)
                       {
                       if(ar[i] < s)
                       {s=s+ar[i];}
                       else break;
                       }
                       if(ans >(k+n-i))
                       ans=k+n-i;
              // ans=min(ans,k+n-i);
               }
    printf("Case #%d: %d\n",p,ans);p++;
    }
    return 0;

   
}
