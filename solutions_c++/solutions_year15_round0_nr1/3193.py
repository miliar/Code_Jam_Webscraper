#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;

int to_int(char c)
{
	return (int)(c - '0');
}

void solve(int test)
{
	int n;
	cin >> n;
	n++;
	string str;
	cin >> str;
	int ans = 0;
	int cur_sum = to_int(str[0]);
	for (int i = 1; i < n; i++)
	{
		int cur_cnt = to_int(str[i]);
		if (cur_cnt == 0)
			continue;
		int add = max(0, i - cur_sum);
		ans += add;
		cur_sum += add + cur_cnt;
	}
	printf("Case #%d: %d\n", test, ans);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests;
	cin >> tests;
	for (int i = 0; i < tests; i++)
		solve(i + 1);

	return 0;
}
