#include<iostream>
#include<math.h>
#include<string.h>
using namespace std;
int main()
{
 freopen("ma.txt","r",stdin);
 freopen("maa.txt","w",stdout);
 int t;
 cin>>t;
 for(int q=1;q<=t;++q)
 {
  int a;
  cin>>a;
  int ar[4][4];
  for(int i=0;i<4;++i)
  for(int j=0;j<4;++j)
  cin>>ar[i][j];
  int b;
  cin>>b;
  int arb[4][4];
  for(int i=0;i<4;++i)
  for(int j=0;j<4;++j)
  cin>>arb[i][j];
  int k=0,ans[4];
  for(int i=0;i<4;++i)
  {
   for(int j=0;j<4;++j)
   {
    if(ar[a-1][i]==arb[b-1][j])
    {ans[k++]=ar[a-1][i];}        
   }        
  }
  if(k==0)
  printf("Case #%d: Volunteer cheated!\n",q);
  else if (k==1)
  printf("Case #%d: %d\n",q,ans[0]);
  else if(k>1)        
  printf("Case #%d: Bad magician!\n",q);
 }    
}
