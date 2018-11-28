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

void solve()
{
	int a, b, k;
	cin >> a >> b >> k;
	int ans = 0;
	for (int i = 0; i < a; i++)
		for (int j = 0; j < b; j++)
			if ((i & j) < k)
				ans++;
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
	for (int i = 0; i < T; i++)
	{
		cout << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
	}
}