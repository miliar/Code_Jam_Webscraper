#include<stdio.h>
#include<fstream>
using namespace std;
int main()
{
 int t,n,m,a[5][5],b[5][5],i,j,k;
 freopen("A-small-attempt0.in","r",stdin);
 freopen("gcj1.txt","w",stdout);
 scanf("%d",&t);
 for(k=1;k<=t;k++)
 {
  scanf("%d",&n);
  for(i=1;i<=4;i++)
  for(j=1;j<=4;j++)
  scanf("%d",&a[i][j]);
  scanf("%d",&m);
  for(i=1;i<=4;i++)
  for(j=1;j<=4;j++)
  scanf("%d",&b[i][j]);
  int count=0,num=0;
  for(i=1;i<=4;i++)
  for(j=1;j<=4;j++)
  if(a[n][i]==b[m][j]) {count++;num=a[n][i];}
  if(count==1) printf("Case #%d: %d\n",k,num);
  else if(count>1) printf("Case #%d: Bad magician!\n",k);
  else printf("Case #%d: Volunteer cheated!\n",k);         
 }   
 return 0;    
}
