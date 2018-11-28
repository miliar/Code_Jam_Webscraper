#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <cstdio>
#include <string>

using namespace std;


signed main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		long long n, cn;
		cin >> n;
		vector<int> used(10, false);
		cn = n;
		int cnt = 10;
		if (n == 0)
		{
			cout << "Case #" << i + 1 << ": INSOMNIA" << endl;
			goto cont;
		}
		while (true)
		{
			string s = to_string(cn);
			for (auto ch : s)
				if (!used[ch - '0'])
					used[ch - '0'] = true, cnt--;
			if (cnt == 0) {
				cout << "Case #" << i + 1 << ": " << s << endl;
				goto cont;
			}
			cn += n;
		}
	cont:;
	}
}