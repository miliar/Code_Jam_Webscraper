#include <stdio.h>
#include<string.h>
int main()
{
	freopen( "B-large.in", "r", stdin );
	freopen( "output.txt", "w", stdout );
	int n,t,i,sum,lol,len;
	char a[101];
	bool rsv;
	scanf("%d",&t);
	for(lol=1;lol<=t;lol++)
	{
		scanf(" %s",&a[0]);
		
		len=strlen(a);sum=0;
		rsv=true;
		for(i=len-1;i>=0;i--)
		{
			if(rsv&&a[i]=='-')
			{
				rsv=false;
				sum++;
			}
			if((!rsv)&&a[i]=='+')
			{
				rsv=true;
				sum++;
			}
		}
		printf("Case #%d: %d\n",lol,sum);
	}
	return 0;
}
		
