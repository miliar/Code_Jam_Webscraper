#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ifstream fin("bs0.in");
ofstream fout("b.out");

ll tmp[100], rt[100];

inline ll getll() {
	double d;
	fin >> d;
	return llround(d*1e4);
}

void solve() {
	int n;
	fin >> n;
	ll tv = getll(), tt = getll();
	ll mint = 1<<30, maxt = 0;

	for (int i = 0; i < n; i++) {
		rt[i] = getll(), tmp[i] = getll();
		mint = min(mint, tmp[i]);
		maxt = max(maxt, tmp[i]);
	}
	if (mint > tt || maxt < tt) {
		fout << "IMPOSSIBLE";
		return;
	}
	// only for 2 flows
	if (tmp[0] == tmp[1] && tmp[0] == tt) {
		fout << setprecision(12) << fixed << (double)tv / (rt[0] + rt[1]);
		return;
	}
	if (tmp[0] == tt || tmp[1] == tt) {
		if (tmp[1] == tt) swap(tmp[0], tmp[1]), swap(rt[0], rt[1]);
		fout << setprecision(12) << fixed << (double)tv / rt[0];
		return;
	}
	double totv = ((double)(tmp[1] - tmp[0])) / (tt - tmp[0]);
	double mulx = tv / totv; // also equal to vb
	double va = tv - mulx;
	fout << setprecision(12) << fixed << max(va / rt[0], mulx / rt[1]);
}

int main() {
	int a;
	fin >> a;
	for (int i = 0; i < a; i++) {
		fout << "Case #" << i+1 << ": ";
		solve();
	   	fout << '\n';
	}
}
