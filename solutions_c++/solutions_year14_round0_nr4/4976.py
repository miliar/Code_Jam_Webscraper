#include<stdio.h>
#include<algorithm>
#include<fstream>
using namespace std;
int main()
{
 int t,n,i,j,k;
 double nao[20],ken[20];
 freopen("D-small-attempt0.in","r",stdin);
 freopen("gcj4.txt","w",stdout);
 scanf("%d",&t);
 for(k=1;k<=t;k++)
 {
  scanf("%d",&n);
  for(i=0;i<n;i++)
  scanf("%lf",&nao[i]);          
  for(i=0;i<n;i++)
  scanf("%lf",&ken[i]);
  int war=0,dwar=0,used[20];
  for(i=0;i<n;i++)
  used[i]=0;
  sort(nao,nao+n);
  sort(ken,ken+n);
  //dwar
  for(i=n-1;i>=0;i--)
  {
   for(j=0;j<n;j++)
   {
    if(ken[i]<nao[j]&&used[j]==0) {used[j]=1;break;}                
   }
   if(j<n) dwar++;
  }
  printf("Case #%d: %d ",k,dwar); 
  //war
  for(i=0;i<n;i++)
  used[i]=0;
  for(i=0;i<n;i++)
  {
   for(j=0;j<n;j++)
   {
    if(nao[i]<ken[j]&&used[j]==0) {used[j]=1;break;}                
   }            
   if(j==n) war++;    
  }
  printf("%d\n",war);
 }
 return 0;    
}
