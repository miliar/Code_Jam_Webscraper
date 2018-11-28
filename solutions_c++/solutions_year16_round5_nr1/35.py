#include <stdio.h>
#include <string.h>

char s[20100];
char sta[20100];
int main(void)
{
	int tt ,ii;
	int lens ,i;
	int np;
	int ans;
	
	scanf("%d" ,&tt);
	for (ii=1 ; ii<=tt ; ii++)
	{
		scanf("%s" ,s+1);
		lens=strlen(s+1);
		np=0;
		ans=0;
		for (i=1 ; i<=lens ; i++)
		{
			if (np==lens-i+1)
			{
				if (sta[np]==s[i])
				{
					ans+=5;
				}
				np--;
			}
			else if (np==0)
			{
				ans+=5;
				sta[++np]=s[i];
			}
			else
			{
				if (sta[np]==s[i])
				{
					np--;
					ans+=5;
				}
				else
				{
					ans+=5;
					sta[++np]=s[i];
				}
			}
		}
		printf("Case #%d: %d\n" ,ii ,ans);
	}
	
	return 0;
}
