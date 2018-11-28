#include <bits/stdc++.h>
using namespace std;
int main()
{
   int t,c,s,i,j,k;
   freopen("D-small-attempt0.txt","rt",stdin);
   freopen("output.txt","wt",stdout);
   scanf("%d",&t);
   for(j=0;j<t;j++)
   {
      scanf("%d%d%d",&k,&c,&s);
      printf("Case #%d: ",j+1);
      for(i=1;i<=s;i++)
      {
          printf("%d ",i);
      }
      printf("\n");
       //cout<<sn<<endl;
      // printf("Case #%d: %d\n",i+1,ans);
   }
   return 0;
}
