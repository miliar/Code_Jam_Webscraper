#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int t,len;
char A[1005];
char ans[1005];
int rtans;
int ltans;
int rt;
int lasts;
char maxs;
int atmaxs;
main()
{
 freopen("A-large.in","r",stdin);
 freopen("A-large.out","w",stdout);
 scanf("%d\n",&t);
 for(int tests=1;tests<=t;tests++)
 {
  scanf("%s",A);
  len=strlen(A);
  rt=len-1;
  rtans=len-1;
  ltans=0;
  printf("Case #%d: ",tests);
  while(rt>=0)
  {
   maxs='A'-1;
   lasts=rt;
   for(int i=lasts;i>=0;i--)
   {
    if(A[i]>maxs){maxs=A[i];atmaxs=i;rt=i-1;}
   }
  // printf("maxs = %d : %c\n",atmaxs,A[atmaxs]);
   ans[ltans]=A[atmaxs];
  // printf("set %d : %c\n",ltans,A[atmaxs]);
   ltans++;
   for(int i=lasts;i>atmaxs;i--)
   {
    ans[rtans]=A[i];
   // printf("set2 %d : %c\n",rtans,A[i]);
    rtans--;
   }
  }
  ans[len]=0;
  printf("%s\n",ans);
 }
 
 return 0;
}
