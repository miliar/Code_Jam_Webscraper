#include <bits/stdc++.h>

using namespace std;

int main()
{
   int t,n,i,s,e,ans,f;
   scanf("%d",&t);
   e=0;
   string a;
   while(t--)
   {
        s=0;
       e++;
       scanf("%d",&n);
   cin>>a;
        ans=0;
         if((a[0]-'0')==0)
           {
               ans=1;
               s=s+ans;
           }
           else
           {
               s=a[0]-'0';
           }
       for(i=1;i<n+1;i++)
       {
               if(i>s)
                {
               ans=ans+(i-s);
               f=i-s;
               s=s+(a[i]-'0')+f;
               }
           else
            {
            s=s+(a[i]-'0');
              }
           }

       printf("Case #%d: %d\n",e,ans);
   }
    return 0;
}
