#include<stdio.h>
int main()
{
int t,c,count,i,m,j;
char s[10];
scanf("%d",&t);
for(j=1;j<=t;j++)
{
  scanf("%d",&m);
  scanf("%s",s);
  count=c=0;
  for(i=0;i<=m;i++)
  {
	  count+=(s[i]-'0');
	  //printf("i=%d %d ",i,count);
	  if((i!=m)&&count<i+1&&s[i+1]!='0')
	  {
		  
		  
		//  printf("Inside if");
		  c+=(i+1-count);
		  count+=c;
		  
	  }
	  
  }
  printf("Case #%d: %d\n",j,c);
}
return 0;
}