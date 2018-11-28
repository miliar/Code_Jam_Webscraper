#include <bits/stdc++.h>

using namespace std;

int t;

int main()
{
	cin >> t;
	for (int tt = 1; tt <= t; tt++)
	{
		long long tmp = 1;
		int k, c, s;
		cin >> k >> c >> s;
		for (int i = 1; i < c; i++)
			tmp *= k;
		cout << "Case #" << tt << ": ";
		for (int i = 0; i < k; i++)
			cout << i * tmp + 1 << " \n"[i == k - 1];
	}
	return 0;
}