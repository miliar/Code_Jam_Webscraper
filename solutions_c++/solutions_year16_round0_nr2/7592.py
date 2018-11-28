#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		char s[102];
		scanf("%s",s);
		int flips=0;
		for(int j=0;j<strlen(s);j++)
		{
			if(j==0 && s[j]=='-')
			{
				while(s[j]=='-'&&j<strlen(s))
				{
					j++;
				}
				flips++;
			}
			else
			{
				if(s[j]=='-')
				{
					while(s[j]=='-'&&j<strlen(s))
					{
						j++;
					}
					flips+=2;
				}
			}
		}
		printf("Case #%d: %d\n",i,flips);
	}
	return 0;
}