#include <stdio.h>
#include <stdlib.h>

int t;
int len;
int nows;
int ans;
char A[1005];
main()
{
 freopen("A-large.in","r",stdin);
 freopen("A-large.out","w",stdout);
 scanf("%d",&t);
 for(int i=1;i<=t;i++)
 {
  ans=0;nows=0;
  scanf("%d",&len);
  scanf(" %s",&A);
  for(int j=0;j<=len;j++)
  {
   if(nows<j){ans+=j-nows;nows=j;}
   nows+=(A[j]-'0');
  }
  printf("Case #%d: %d\n",i,ans);
 }
 return 0;
}
