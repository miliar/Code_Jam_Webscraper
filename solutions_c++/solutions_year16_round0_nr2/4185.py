#include<iostream>
#include<cstdio>
#include<string>
#include<set>
#include<algorithm>
#include<vector>
#include<map>
#include<cmath>
#include<queue>
#include<time.h>
using namespace std;

void solve()
{
	string s;
	cin >> s;
	int cnt = 0;
	for (int i = s.size() - 1; i >= 0; i--)
	{
		if (s[i] == '+')
			continue;
		cnt++;
		for (int j = i; j >= 0; j--)
		{
			if (s[j] == '+')
				s[j] = '-';
			else
				s[j] = '+';
		}
	}
	cout << cnt;
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
		cout << "Case #" << t << ": ";
		solve();
		cout << endl;
		cerr << t << " " << 1.0 * clock() / CLOCKS_PER_SEC << endl;
	}
}