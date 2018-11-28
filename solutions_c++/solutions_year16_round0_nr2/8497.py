#include<stdio.h>
#include<string.h>
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int i,t,m=1;
	char c[101];
	scanf("%d",&t);
	while(t--)
	{
		scanf("%s",c);
		int length=strlen(c);
		int counter=0;
		char first =c[0];
		for(i=1;i<length;i++)
			{
				if(c[i]==first)
				continue;
				else
				{
					if(first=='+')
						first='-';
					else
						first='+';
					counter +=1;
				}
			}
		if(first=='-')
			counter+=1;
		printf("Case #%d: %d\n",m,counter);
		m++;
	}
}
