#include <bits/stdc++.h>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin >> t;
	for(int z = 1; z <= t; z++)
	{
		cout << "Case #" << z << ": ";
		int n;
		cin >> n;
		int a[n];
		for(auto &it: a)
			cin >> it;
		int p[n];
		iota(p, p + n, 0);
		sort(p, p + n, [&](int A, int B){return a[A] < a[B];});
		while(a[p[n - 1]])
		{
			if(n == 2)
			{
				cout << "AB ";
				a[p[n - 1]]--;
				a[p[n - 2]]--;
			}
			else
			{
				if(a[p[n - 1]] == 1 && a[p[n - 3]] == 1)
					cout << char('A' + p[n - 1]) << ' ';
				else
					{cout << char('A' + p[n - 1]) << char('A' + p[n - 2]) << ' '; a[p[n - 2]]--;}
				a[p[n - 1]]--;
			}
			sort(p, p + n, [&](int A, int B){return a[A] < a[B];});
		}
		cout << "\n";
	}
	return 0;
}
