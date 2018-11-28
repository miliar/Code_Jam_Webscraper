#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

string str;
int k;
void solve()
{
	int ans = 0;
	for (int i = 0; i <= (int)str.length() - k; i++)
	{
		if (str[i] == '+')
			continue;
		ans++;
		for (int s = i; s < i + k; s++)
			str[s] = (str[s] == '-' ? '+' : '-');
	}
	for (char c : str)
		if (c == '-')
			ans = -1;
	if (ans == -1)
		puts("IMPOSSIBLE");
	else
		printf("%d\n", ans);
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		cin >> str >> k;
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}
