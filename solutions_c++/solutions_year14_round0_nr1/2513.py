#include <stdio.h>
#include <stdlib.h>

int t;
int ans[3];
int table[3][5][5];
int rows[3][17];
int cnt;
int pri;
main()
{
 freopen("A-small-attempt0.in","r",stdin);
 freopen("A-small-attempt0.out","w",stdout);
 scanf("%d",&t);
 for(int tests=1;tests<=t;tests++)
 {
  cnt=0;
  for(int i=1;i<=2;i++)
  {
   scanf("%d",&ans[i]);
   for(int j=1;j<=4;j++)
   {
    for(int k=1;k<=4;k++)
    {
     scanf("%d",&table[i][j][k]);
     rows[i][table[i][j][k]]=j;
    }
   }        
  }        
  for(int i=1;i<=16;i++)
  {
   if(rows[1][i]==ans[1]&&rows[2][i]==ans[2]){cnt++;pri=i;}
  }
  printf("Case #%d: ",tests);
  if(cnt==0){printf("Volunteer cheated!\n");}
  else if(cnt==1){printf("%d\n",pri);}
  else{printf("Bad magician!\n");}
 }
 return 0;
}
