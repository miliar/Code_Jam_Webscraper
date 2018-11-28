#include <bits/stdc++.h>

using namespace std;

#define INP "inp.txt"
#define OUT "out.txt"
#define ll long long
#define ull unsigned long long

int T, K, C, S;

void solve() {
	std::vector<ull> v;
	for(int i = 1; i <= K; i++) v.push_back((ull)i);
	for(int i = 2; i <= C; i++) {
		for(int j = 0; j < K; j++) {
			v[j] = (v[j] - 1) * (ull) K + j + 1;
		}
	}

	for(int i = 0; i < K; i++) {
		cout << " " << v[i];
	}
}

int main () {
	freopen(INP, "r", stdin);
	freopen(OUT, "w", stdout);

	scanf("%d ", &T);
	for(int tt = 1; tt <= T; tt++) {
		scanf("%d %d %d", &K, &C, &S);

		cout << "Case #" << tt << ":";
		solve();
		cout << endl;
	}
	return 0;
}