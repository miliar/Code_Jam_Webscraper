#include <bits/stdc++.h>

using namespace std;

char s[200];

int main()
{
	int t;
	scanf("%d\n",&t);
	for (int c=1;c<=t;c++)
	{
		gets(s);
		int len = strlen(s);
		bool happySideUp = (s[0]=='+');
		int cnt = 0;
		for (int i=1; i<len; i++)
		{
			if (s[i]!=s[i-1])
			{
				cnt++;
				happySideUp = (s[i]=='+');
			}
		}
		if (!happySideUp) cnt++;
		printf("Case #%d: %d\n",c,cnt);
	}
	return 0;
}