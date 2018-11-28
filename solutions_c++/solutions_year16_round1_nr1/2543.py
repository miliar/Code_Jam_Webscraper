#include <cstdio>
#include <cstring>

char s[1001];

void work(int l, int r)
{
	if (l > r)
		return;
	char c = 0;
	int pos = 0;
	for (int i = l; i <= r; ++i)
		if (s[i] >= c)
		{
			c = s[i];
			pos = i;
		}
	printf("%c", c);
	work(l, pos - 1);
//	work(pos + 1, r);
	for (int i = pos + 1; i <= r; ++i)
		printf("%c", s[i]);
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d\n", &T);
	for (int ttt = 1; ttt <= T; ++ttt)
	{
		scanf("%s\n", &s);

		printf("Case #%d: ", ttt);
		work(0, strlen(s) - 1);

		printf("\n");
	}

	return 0;
}