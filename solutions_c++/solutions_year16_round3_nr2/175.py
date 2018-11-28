#include <bits/stdc++.h>

using namespace std;

#define int int64_t

signed main()
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
		int n, k;
		cin >> n >> k;
		if(k > (1LL << n - 2))
		{
			cout << "IMPOSSIBLE\n";
			continue;
		}
		cout << "POSSIBLE\n";
		int A[n][n];
		memset(A, 0, sizeof(A));
		for(int i = 1; i < n; i++)
			for(int j = i + 1; j < n; j++)
				A[i][j] = 1;
		if(k == (1LL << n - 2))
		{
			fill(A[0] + 1, A[0] + n, 1);
		}
		else
		{
			for(int i = 0; i < n; i++)
				if((k >> i) & 1)
					A[0][n - i - 2] = 1;
		}
		for(auto it: A)
		{
			for(int i = 0; i < n; i++)
				cout << it[i];
			cout << "\n";
		}
	}
	return 0;
}
