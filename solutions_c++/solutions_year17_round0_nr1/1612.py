#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int t;
int k;
int len;
int cnt;
char A[1005];
main()
{
 freopen("A-large.in","r",stdin);
 freopen("A-large.out","w",stdout);
 scanf("%d\n",&t);
 for(int tests=1;tests<=t;tests++)
 {
  scanf("%s",A);
  scanf("%d\n",&k);
  //printf("%s, %d\n",A,k);
  len=strlen(A);
  cnt=0;
  for(int i=0;i<=len-k;i++)
  {
   if(A[i]=='-')
   {
   	cnt++;
   	for(int j=i;j<i+k;j++)
   	{
	 if(A[j]=='+')
	 {
	 	A[j]='-';
	 }
	 else
	 {
	 	A[j]='+';
	 }
	}
   }
  }
  printf("Case #%d: ",tests);
  //printf("%d %d\n",len,len-k);
  for(int i=len-k;i<len;i++)
  {
  // printf("in\n");
   if(A[i]=='-'){printf("IMPOSSIBLE\n");break;}
   else if(i==len-1){printf("%d\n",cnt);}
  }
  
 }
 return 0;
}
