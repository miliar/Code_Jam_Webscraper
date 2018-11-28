#include <stdio.h>
#include <stdlib.h>
int t,n;
int cnt[2505];
int tmp;
int pri;
void clear()
{
 for(int i=1;i<=2500;i++)
 {
  cnt[i]=0;
 }
 pri=0;
}
main()
{
 freopen("B-large.in","r",stdin);
 freopen("B-large.out","w",stdout);
 scanf("%d",&t);
 for(int tests=1;tests<=t;tests++)
 {
  scanf("%d",&n);
  clear();
  for(int i=1;i<(2*n);i++)
  {
   for(int j=1;j<=n;j++)
   {
    scanf("%d",&tmp);
    cnt[tmp]++;
   }
  }
  printf("Case #%d: ",tests);
  for(int i=1;i<=2500;i++)
  {
  // printf("cnt %d = %d\n",i,cnt[i]);
   if(cnt[i]%2==1)
   {
    if(pri){printf(" ");}
    printf("%d",i);
    pri=1;
   }
  }
  printf("\n");
 }
 //system("pause");
 return 0;
}
