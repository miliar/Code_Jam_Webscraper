#include <bits/stdc++.h>
using namespace std;

const int maxn = 1000 + 55;

int n;
double w[2][maxn];

int normal() {
	int score = n;
	int dx = 0;
	for (int i = 0; i < n; ++i) {
		while (dx < n && w[1][dx] < w[0][i])
			dx++;
		if (dx >= n) break;
		score --;
		dx++;
	}
	return score;
}

int deceitful() {
	for (int i = 0; i <= n; ++i) {
		bool ok = 1;
		for (int j = 0; j < n-i; ++j)
			if (w[0][i+j] < w[1][j]) ok = 0;
		if (ok) return n-i;
	}
}

int main() {
	int tests; cin >> tests;
	for (int t = 1; t <= tests; ++t) {
		cin >> n;
		for (int j = 0; j < 2; ++j) {
			for (int i = 0; i < n; ++i) cin >> w[j][i];
			sort(w[j], w[j] + n);
		}
		
		cout << "Case #" << t << ": ";
		cout << deceitful();		
		cout << " ";
		cout << normal();		
		cout << endl;
	}
}
