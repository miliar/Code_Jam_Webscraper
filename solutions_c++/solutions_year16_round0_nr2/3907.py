#include <stdio.h>
#include <string.h>

char input[105];

int main()
{
	freopen(R"(C:\Users\Unused\Downloads\B-large.in)", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; tt++)
	{
		printf("Case #%d: ", tt);
		scanf("%s", input);
		int len = strlen(input);

		int ans = 0;

		for (int i = 1; i < len; i++)
		{
			if (input[i - 1] != input[i]) ans++;
		}

		if (input[len - 1] == '-') ans++;
		printf("%d\n", ans);
	}
}