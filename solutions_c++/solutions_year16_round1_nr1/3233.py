#include<stdio.h>
#include<string.h>
int main()
{
	int t,i,j,start,mid,end,len;
	char s[1007],s1[3000];
	scanf("%d",&t);
	for(j=1;j<=t;j++)
	{
		scanf("%s",&s);
		len=strlen(s);
		memset(s1,0,sizeof(s1));
		start=1500;
		end=1500;
		mid=1500;
		s1[mid]=s[0];
		for(i=1;i<len;i++)
		{
			if(s[i]>=s1[start])
			{
				start--;
				s1[start]=s[i];
			}
			else
			{
				end++;
				s1[end]=s[i];
			}
		}
		printf("Case #%d: ",j);
		for(i=start;i<=end;i++)
			printf("%c",s1[i]);
		printf("\n");
		
	}
	return 0;
}
