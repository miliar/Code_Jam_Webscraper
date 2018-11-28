#include<stdio.h>
#include<string.h>
#include<fstream>
using namespace std;
int main()
{
 int t,n,i,j;
 char s[1003];
 freopen("A-large.in","r",stdin);
 freopen("gcoj1_big.txt","w",stdout);
 scanf("%d",&t);
 for(j=1;j<=t;j++)
 {
  int ans=0,sum=0;
  scanf("%d",&n);
  scanf("%s",s);
  for(i=0;i<=n;i++)
  {
   if(sum<i) {ans+=i-sum;sum=i;}
   sum+=s[i]-'0';                 
  }
  printf("Case #%d: %d\n",j,ans);          
 }
 return 0;    
}
