#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
   int t; scanf("%d", &t);
   vector<int> ans;
   for(int tc=1;tc<=t;tc++)
   {
      int x, r, c; scanf("%d%d%d", &x, &r, &c);
      if(x==1) ans.push_back(1);
      else if(x==2)
      {
         if((r*c)%2==0) ans.push_back(1);
         else ans.push_back(0);
      }
      else if(x==3)
      {
         if((r*c)%3==0)
         {
            if(r==1 || c==1) ans.push_back(0);
            else ans.push_back(1);
         }
         else ans.push_back(0);
      }
      else if(x==4)
      {
          if((r*c)%4==0)
          {
             if(r==1 || c==1) ans.push_back(0);
             else if(r==2 || c==2) ans.push_back(0);
             else if(r==3 || c==3) ans.push_back(1);
             else ans.push_back(1);
          }
          else ans.push_back(0);
      }
   }
   for(int tc=1;tc<=t;tc++) 
   {
     if(ans[tc-1]==0) printf("Case #%d: RICHARD\n", tc);
     else printf("Case #%d: GABRIEL\n", tc);
   }
   //system("pause");
   return 0;
}
