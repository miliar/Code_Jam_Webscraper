#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
   int test_case;
   scanf("%d",&test_case);
   int ca=1;
   while(test_case--)
   {
      int ma;
      scanf("%d",&ma);
      string inp;
      cin>>inp;
        int ans=0;
        int cum=0;
      for(int i=0;i<=ma;i++)
      {
         if(cum>=i)cum+=inp[i]-48;
         else if(inp[i]!='0')
         {
           ans+=(i-cum);
           cum+=inp[i]-48+(i-cum);
         }
      }
      printf("Case #%d: %d\n",ca,ans);
      ca++;
   }
   return 0;
}
