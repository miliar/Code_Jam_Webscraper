#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<queue>
#include<stack>
#include<vector>
using namespace std;

  int a[10][10];
  int b[20];


  int main()
  {
      freopen("A.in","r",stdin);
      freopen("out.txt","w",stdout);
      int t;
      int tt,i,j;
      int k1,k2,x;
      int sum,sumj;
      scanf("%d",&t);

      for (tt=1;tt<=t;tt++)
      {
          scanf("%d",&k1);
          for (i=1;i<=4;i++)
          for (j=1;j<=4;j++)
            scanf("%d",&a[i][j]);

          scanf("%d",&k2);
          for (i=1;i<=4;i++)
          for (j=1;j<=4;j++)
            scanf("%d",&x),b[x]=i;

          sum=0;

          for (i=1;i<=4;i++)
            if(b[a[k1][i]]==k2) sum++,sumj= a[k1][i];

          if (sum==0) printf("Case #%d: Volunteer cheated!\n",tt);
          else if (sum==1) printf("Case #%d: %d\n",tt,sumj);
          else printf("Case #%d: Bad magician!\n",tt);

      }





      return 0;
  }
