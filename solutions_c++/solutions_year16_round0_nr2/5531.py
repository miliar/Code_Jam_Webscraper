#include <iostream>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <algorithm>
#include <queue>
using namespace std;

int count_regions(string str)
{
	char prev = 'x';
	int ans = 0;

	for (int i = 0; i < str.length(); i++)
	{
		if (str[i] != prev) ans++;
		prev = str[i];
	}
	return ans;
}

int main()
{
#if !ONLINE_JUDGE
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
#endif

	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int t;
	cin >> t;
	for (int z = 1; z <= t; z++)
	{
		string str;
		cin >> str;
		int cnt = count_regions(str);

		if (str[str.length() - 1] == '+') cnt--;

		cout << "Case #" << z << ": " << cnt << endl;
	}
	return 0;
}