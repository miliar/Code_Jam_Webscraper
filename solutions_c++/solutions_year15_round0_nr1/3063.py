#include <bits/stdc++.h>

using namespace std;
char s[1010];
int main()
{
   int t;
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
   scanf("%d",&t);
   for(int l=0;l<t;l++)
   {
       int n;
       scanf("%d",&n);
       scanf("%s",s);
       int curx=0,sol=0;
       for(int i=0;i<=n;i++)
       {
           if(curx>=i)
               curx+=(s[i]-'0');
           else
           {
               sol+=(i-curx);
               curx+=(i-curx);
               curx+=(s[i]-'0');
           }
       }
       printf("Case #%d: %d\n",l+1,sol);
   }

   return 0;
}
