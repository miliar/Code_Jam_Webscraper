#include <stdio.h>
#include <stdlib.h>

int t,n,caps;
int buc[701];
int tmp;
int ans;
int at;
int st;
main()
{
 freopen("A-large.in","r",stdin);
 freopen("A-large.out","w",stdout);
 scanf("%d",&t);
 for(int tests=1;tests<=t;tests++)
 {
  scanf("%d%d",&n,&caps);
  for(int i=1;i<=caps;i++)
  {
   buc[i]=0;
  }
  for(int i=1;i<=n;i++)
  {
   scanf("%d",&tmp);
   buc[tmp]++;
  }
  ans=0;
  at=caps;
  while(at>0)
  {
   if(buc[at]>0)
   {
    buc[at]--;
    ans++;
    if(caps-at>at){st=at;}
    else{st=caps-at;}
    for(int i=st;i>0;i--)
    {
     if(buc[i]>0){buc[i]--;break;}
    }
   }
   else
   {
    at--;
   }
  }
  printf("Case #%d: %d\n",tests,ans);
 }
 
 return 0;
}
