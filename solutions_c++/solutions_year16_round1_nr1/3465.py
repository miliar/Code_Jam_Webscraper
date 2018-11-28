#include<stdio.h>
int main(void)

{
	int t,i,len,j,k,l;
	char s[1001],sq[20001];
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		printf("Case #%d: ",i);
		scanf("%s",&s);
		len=0;
		for(;s[len]!='\0';++len);
		k=len*2;
		l=len*2;
		sq[k]=s[0];
		for(j=1;j<len;j++)
		{
			if(s[j]>=sq[k])
			
			{
				--k;
				sq[k]=s[j];
			}
			else
			{
			++l;
			sq[l]=s[j]	;
			}
		}
		for(j=k;j<=l;j++)
		printf("%c",sq[j]);
		printf("\n");
	}
	return 0;
}
