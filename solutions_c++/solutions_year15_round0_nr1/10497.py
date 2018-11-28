#include <stdio.h>
#include <string.h>

int main()
{
	int standing=0,persons_needed=0,i,Smax,T,n=1;
	char s[1002];
	
	scanf("%d",&T);
	
	while(T--)
	{
		persons_needed = standing = 0;
		scanf("%d",&Smax);
		scanf("%s",s);
		for(i=0;i<=Smax;i++)
		{
			if(s[i]=='0')
				continue;
			if(i<=standing)
				standing += s[i]-'0';
			else
			{
				persons_needed += i-standing;
				standing += persons_needed + (s[i]-'0');
			}	
		}
		printf("Case #%d: %d\n",n++,persons_needed);
	}
	
	
	return 0;
}
