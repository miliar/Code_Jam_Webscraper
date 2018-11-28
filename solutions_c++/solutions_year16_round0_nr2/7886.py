#include<stdio.h>
#include<string.h>

int main()
{
	int t,i,count,len,j;
	char s[107];
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		scanf("%s",&s);
		count=0;
		len=strlen(s);
		for(j=1;j<len;j++)
		{
			if(s[j]!=s[j-1])
				count+=1;
		}
		if(s[len-1]=='-')
			count+=1;
		printf("Case #%d: %d\n",i,count);
	}
	return 0;
}
