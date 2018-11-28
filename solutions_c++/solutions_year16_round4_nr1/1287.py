#include <bits/stdc++.h>

#define all(x) (x).begin(), (x).end()

using namespace std;

inline int nxt(){
	int x;
	scanf("%d", &x);
	return x;
}

const string rsp = "RSP";
string dp[3][13];

void solve(int test){
	printf("Case #%d: ", test);

	int n = nxt(), r = nxt(), p = nxt(), s = nxt();
	int a[3] = {1, 0, 0};
	int b[3];
	for (int i = 0; i < n; i++){
		for (int j = 0; j < 3; j++)
			b[j] = a[j];
		for (int j = 0; j < 3; j++)
			b[(j + 1) % 3] += a[j];
		for (int j = 0; j < 3; j++)
			a[j] = b[j];
	}
	int _ = 0;
	while (_ < 3 && (r != a[_] || s != a[(_ + 1) % 3] || p != a[(_ + 2) % 3]))
		_++;
	if (_ == 3)
		puts("IMPOSSIBLE");
	else {
		_ = (3 - _) % 3;
		cout << dp[_][n] << "\n";
	}
}

int main(){

	for (int i = 0; i < 3; i++)
		dp[i][0] = rsp[i];
	for (int i = 1; i < 13; i++){
		for (int j = 0; j < 3; j++){
			for (int k = 0; k < 3; k++){
				if (j == k)
					continue;
				int _ = j;
				if ((k + 1) % 3 == j)
					_ = k;
				if (dp[_][i] == "" || dp[_][i] > dp[j][i - 1] + dp[k][i - 1])
					dp[_][i] = dp[j][i - 1] + dp[k][i - 1];
			}
		}
	}

	int T = nxt();
	for (int i = 0; i < T; i++){
		solve(i + 1);
		cerr << "Test #" << i + 1 << " is complete\n";
	}

	return 0;
}