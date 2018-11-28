#include<iostream>
#include<cstdio>
#include<string>
#include<set>
#include<algorithm>
#include<vector>
#include<map>
#include<cmath>
#include<queue>
using namespace std;

void Solution()
{
	int n;
	string s;
	cin >> n >> s;
	int ans = 0, up = 0;

	for (int i = 0; i <= n; i++)
	{
		int k = s[i] - '0';
		int need = max(0, i - up);
		ans += need;
		up += need;
		up += k;
	}
	cout << ans;
}

int main()
{
#ifdef LOCAL
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);
		Solution();
		printf("\n");
	}
}