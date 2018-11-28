#include <bits/stdc++.h>
using namespace std;

typedef long long int ll;
typedef pair<ll,ll> par;
const int MAX_N = 22;

int dp[MAX_N][MAX_N];

void init()
{
	for (int i = 1; i <= 20; i++) {
		for (int j = 1; j <= i; j++) {
			dp[i][j] = i;
		}
		for (int j = i+1; j <= 20; j++) {
			dp[i][j] = 1 + dp[i][j - i];
		}
	}

	// for (int i = 0; i <= 10; i++) {
	// 	for (int j = 0; j <= 10; j++) {
	// 		printf("%d ", dp[i][j]);
	// 	}
	// 	printf("\n");
	// }
}

void solve()
{
	int r, c, w;
	cin >> r >> c >> w;
	int ret = (r - 1) * (c / w) + dp[w][c];
	cout << ret << endl;
}

int main()
{
	init();
	int t; scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		solve();
	}
}
