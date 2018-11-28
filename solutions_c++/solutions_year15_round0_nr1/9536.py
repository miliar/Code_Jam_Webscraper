#include<bits/stdc++.h>
using namespace std;
int main()
   {
   freopen("A-large.in","r",stdin);
   freopen("A-large.out","w",stdout);
   int t,people,n;
   char s[1024];
   scanf("%d",&t);
   for(int T=0;T<t;T++)
      {
      scanf("%d",&n);
      scanf("%s",s);
      people=s[0]-48;
      int ans=0;
      for(int i=1;i<=n;i++)
         {
         if(s[i]>'0')
            if(people>=i)
               {
               people += s[i]-'0';
               }
            else
               {
               ans += i-people;
               people=i+s[i]-'0';
               }
         }
      printf("Case #%d: %d\n",T+1,ans);
      }
   return 0;
   }
