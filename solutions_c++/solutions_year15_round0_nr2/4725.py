#include<cstdio>
#include<vector>
#include<functional>
#include<cmath>
#include<algorithm>
using namespace std;

int main()
{
   int t; scanf("%d", &t);
   vector<int> ans;
   for(int tc=1;tc<=t;tc++)
   {
      int d; scanf("%d", &d);
      int in[1005]; 
      for(int i=0;i<d;i++) scanf("%d", &in[i]);
      sort(in,in+d,greater<int>());
      int mx=in[0], an=in[0];
      for(int i=1;i<=mx;i++)
      {
         int tmp=0;
         for(int j=0;j<d;j++)
         {
            if(in[j]<=i) break;
            if(in[j]%i==0) { tmp+=(in[j]/i)-1; }
            else { tmp+=in[j]/i;}
            //printf("%d\n", tmp);
         }
         if((tmp+i) < an) an=tmp+i;
      }
      ans.push_back(an);
   }
   for(int tc=1;tc<=t;tc++) printf("Case #%d: %d\n", tc, ans[tc-1]);
   //system("pause");
   return 0;
}
