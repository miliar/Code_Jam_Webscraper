#include <bits/stdc++.h>

using namespace std;

const int maxn = 1000;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		int K, ans = 0;
		string S;
		bitset<maxn> m, k;
		printf("Case #%d: ", t);
		cin >> S >> K;
		for (int i = 0; i < S.length(); ++i)
			m[i] = (S[i] == '-');
		for (int i = 0; i < K; ++i)
			k[i] = 1;
		for (int i = 0; i + K <= S.length(); ++i, k <<= 1)
			if (m[i])
			{
				m ^= k;
				ans++;
			}
		for (int i = 0; i < S.length(); ++i)
			if (m[i])
				ans = -1;
		if (ans >= 0)
			cout << ans << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}
}
