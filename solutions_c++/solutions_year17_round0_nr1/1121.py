#include <stdio.h>
#include <string.h>
int main()
{
	freopen( "A-large.in", "r", stdin );
	freopen( "output.txt", "w", stdout );
	long long int n,t,i,j,sum,r,k,lol;
	char s[1005];
	scanf("%lld",&t);
	for(lol=1;lol<=t;lol++)
	{
		scanf(" %s %lld",&s[0],&k);
		sum=0;
		n=strlen(s);
//		printf("%lld",n);
//		for(i=0;i<n;i++)
//		{
//			printf("%c",s[i]);
//		}
		for(i=0;i<n;i++)
		{
			if(s[i]=='+')continue;
			if(i+k>n)break;
			sum++;
			for(j=i;j<i+k;j++)
			{
				
				if(s[j]=='+')s[j]='-';
				else s[j]='+';
			}
//			for(r=0;r<n;r++)
//		{
//			printf("%c",s[r]);
//		}
//		printf("\n");
		}
		for(i=0;i<n;i++)
			if(s[i]=='-')break;
		if(i<n)		
			printf("Case #%lld: IMPOSSIBLE\n",lol);
		else	
		printf("Case #%lld: %lld\n",lol,sum);
	}
	return 0;
}
		
