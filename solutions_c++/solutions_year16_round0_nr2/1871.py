#include <stdio.h>
#include <string.h>

char s[112];

int
main(void)
{
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);
		scanf("%s", s);
		int n = strlen(s);
		int ans = 0;
		for(int i = 1; i < n; i++)
			if(s[i] != s[i-1])
				ans++;
		if(s[n-1] == '-')
			ans++;
		printf("%d\n", ans);
	}
}
