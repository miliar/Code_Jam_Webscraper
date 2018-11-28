#include <bits/stdc++.h>

using namespace std;

string digs[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
string repr = "ZWXUSGOTFN";
int nms[] = {0, 2, 6, 4, 7, 8, 1, 3, 5, 9};

signed main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin >> t;
	for(int i = 0; i < t; i++)
	{
		cout << "Case #" << i + 1 << ": ";
		int n;
		cin >> n;
		unordered_map<string, int> gg[2];
		int A[n], B[n];
		for(int i = 0; i < n; i++)
		{
			string a, b;
			cin >> a >> b;
			if(!gg[0][a])
				gg[0][a] = gg[0].size();
			if(!gg[1][b])
				gg[1][b] = gg[1].size();
			A[i] = gg[0][a];
			B[i] = gg[1][b];
		}
		int left[n], right[n];
		for(int i = 0; i < n; i++)
		{
			left[i] = right[i] = 0;
			for(int j = 0; j < n; j++)
			{
				left[i] |= (1 << j) * (A[i] == A[j]);
				right[i] |= (1 << j) * (B[i] == B[j]);
			}
		}
		int msk_sz = 1 << n;
		int dp[msk_sz][n];
		memset(dp, 0, sizeof(dp));
		for(int msk = 0; msk < msk_sz; msk++)
			for(int i = 0; i < n; i++)
				for(int j = 0; j < n; j++)
				{
					if((msk >> i) & 1)
					if(!((msk >> j) & 1))
					{
						dp[msk | (1 << j)][j] = max(dp[msk | (1 << j)][j], dp[msk][i] + ((msk & left[j]) && (msk & right[j])));
					}
				}
		cout << *max_element(dp[msk_sz - 1], dp[msk_sz - 1] + n);
		cout << "\n";
	}
	return 0;
}
