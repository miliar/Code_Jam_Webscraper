#include<cstdio>
#include<cstring>
#include<string>

char in[1111];
std::string ans;
int len;

void solve()
{
	ans = in[0];
	for (int i = 1; i < len; i++)
	{
		if (in[i] < ans[0]) ans += in[i];
		else ans = in[i] + ans;
	}
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		scanf("%s", in);
		len = strlen(in);
		solve();
		printf("Case #%d: %s\n", t, ans.c_str());
	}
}