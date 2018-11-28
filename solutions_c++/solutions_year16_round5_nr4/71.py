#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
using namespace std;

void solve()
{
	int n, m;
	cin >> n >> m;
	string s;
	bool ok = true;
	while(n--)
	{
		cin >> s;
		bool allOne = true;
		for (int i = 0; i < m; i++)
			allOne &= (s[i] == '1');
		ok &= !allOne;
	}
	cin >> s;
	if (!ok)
	{
		cout << "IMPOSSIBLE" << endl;
		return;
	}
	for (int i = 0; i < 50; i++)
		cout << "10";
	cout << "?1 0";
	for (int i = 0; i < m - 1; i++)
		cout << "?";
	cout << endl;
	return;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		cout << "Case #" << i << ": ";
		solve();
	}

	return 0;
}