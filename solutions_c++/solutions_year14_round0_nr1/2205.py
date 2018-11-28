#include <stdio.h>

int main()
{
freopen("A-small-attempt0.in","r",stdin);
freopen("A-small-attempt0.out","w",stdout);
int cas=1,t;
scanf("%d",&t);
while(t--)
{
int r,to,b[4][4],a[4][4],i,j,ro1,ro2,match=0;
scanf("%d",&ro1);
for(i=0;i<4;i++)
for(j=0;j<4;j++)
scanf("%d",&a[i][j]);
scanf("%d",&ro2);
for(i=0;i<4;i++)
for(j=0;j<4;j++)
scanf("%d",&b[i][j]);
for(i=0;i<4;i++)
{
  to=a[ro1-1][i];
  for(j=0;j<4;j++)
  {
  if(b[ro2-1][j]==to)
  {match++;         
  r=b[ro2-1][j];}    
  }         
}
if(match==1)
printf("Case #%d: %d\n",cas,r);
else if(match>1)
printf("Case #%d: Bad magician!\n",cas);
else
printf("Case #%d: Volunteer cheated!\n",cas);
cas++;
}
return 0;    
}
