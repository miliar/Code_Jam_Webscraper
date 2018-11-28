#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;

int main()
{
   int t; scanf("%d", &t);
   for(int tc=1;tc<=t;tc++)
   {
      int n; scanf("%d", &n); n++;
      char inp[1005]; scanf("%s", inp);
      int in[1005]; in[0]=0;
      for(int i=1;i<=n;i++) in[i]=inp[i-1]-'0';
      int ans=0;
      for(int i=1;i<=n;i++)
      {
         if(in[i-1]<i-1) { ans+=(i-1-in[i-1]); in[i]+=i-1; }
         else in[i]+=in[i-1];
      }
      printf("Case #%d: %d\n", tc, ans);
   }
   //system("pause");
   return 0;
}
