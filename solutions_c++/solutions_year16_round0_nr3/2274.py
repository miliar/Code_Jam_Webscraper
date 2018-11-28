#include <bits/stdc++.h>

using namespace std;
#define For(i,l,r) for (int i = l; i <= r; ++i)

int func(long long x, int b, int mod) {
	int res = 0;
	int mult = 1;
	while (x) {
		(res += mult * (x % 2)) % mod;
		x /= 2;
		(mult *= b) %= mod;
	}
	return res;
};

int N;
vector< vector< pair<long long, int> > > coins;
const int prpr[] = {2,3,5,7,11,13,17,19,23};
void dfs(int now, long long nowx) {
	if (now >= N) {
		if (nowx % 2 == 0) return ;
		vector< pair<long long, int> > coin;
		int valid_all = true;
		For(b,2,10) {
			int t = func(nowx, b, 223092870);
			bool valid = false ;
			For(j,0,8) if (t % prpr[j] == 0) {
				valid = true;
				coin.emplace_back(t, prpr[j]); break ;
			}
			if (!valid) valid_all = false ;
		}
		if (valid_all) coins.push_back(coin);
		return ;
	}
	if (coins.size() >= 500) return ;
	dfs(now + 1, nowx * 2 + 0);
	dfs(now + 1, nowx * 2 + 1);
}

void print(int x) {
	if (x == 0) return ;
	print(x / 2);
	printf("%d", x % 2);
}

int J;
int main() {
	int T;
	cin >> T;
	For(TK,1,T) {
		printf("Case #%d:\n", TK);
		cin >> N >> J;
		coins.clear();
		dfs(1, 1);
		int cnt = 0;
		for (auto x: coins) {
			print(x[0].first);
			for (auto y: x) printf(" %d", y.second);
			puts("");
			if (++cnt == J) break ;
		}
	}
	// int n;
	// while (cin >> n) {
	// 	cout << func(n) << endl;
	// }
	// int T; cin >> T;
	// For(TK,1,T) {
	// }
	return 0;
}