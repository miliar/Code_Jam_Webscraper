#include<cstdio>
#include<cstring>
bool d[100];
int solve(int len)
{
	int c = 0, ans;
	bool t;
	if (!len) return 0;
	if (d[0])
	{
		d[0] = false;
		for (int i = 1; i < len; i++)
		{
			if (!d[i]) break;
			d[i] = false;
		}
		ans = 1 + solve(len);
	}
	else
	{
		int j=1;
		for (; j < len; j++)
		{
			if (d[j]) break;
		}
		for (int i = 0; i < (len + 1) >> 1; i++)
		{
			t = !d[i];
			d[i] = !d[len - i - 1];
			d[len - i - 1] = t;
		}
		ans = 1 + solve(len - j);
	}
	return ans;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, n;
	char in[111];
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		scanf("%s", in);
		n = 0;
		for (int i = 0; i < strlen(in); i++)
		{
			d[i] = in[i] == '+';
			if (!d[i]) n = i + 1;
		}
		printf("Case #%d: %d\n", t, solve(n));
	}
}