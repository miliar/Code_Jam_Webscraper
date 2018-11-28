#include <cstdio>
#include <algorithm>

int toInt(char ch)
{
	return ch - '0';
}

char in[1025];
int main()
{
	int T, S;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t)
	{
		scanf("%d", &S);
		scanf("%s", in);
		int cur = 0;
		int ret = 0;
		cur = toInt(in[0]); 
		for (int i = 1; in[i] != '\0'; ++i)
		{
			int num = toInt(in[i]);
			if (cur < i)
			{
				ret += (i - cur);
				cur = i; 
			}
			cur += num;
		}
		printf("Case #%d: %d\n", t, ret);
	}
	return 0;
}
