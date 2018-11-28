#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

int solve(string s)
{
	int pos;
	while ((pos = s.find("--")) != string::npos)
	{
		s.replace(pos, 2, "-");
	}
	pos = 0;
	while ((pos = s.find("++")) != string::npos)
	{
		s.replace(pos, 2, "+");
	}
	if (s[0] == '-')
		return (s.length() % 2 == 0 ? s.length() - 1 : s.length());
	else
		return (s.length() % 2 == 0 ? s.length() : s.length() - 1);
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	char test[110];
	for (int i = 0; i < T; i++)
	{
		scanf("%s", test);
		printf("Case #%d: %d\n", i + 1, solve(test));
	}
	return 0;
}