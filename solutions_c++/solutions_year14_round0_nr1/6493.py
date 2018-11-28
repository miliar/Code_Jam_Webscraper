#include <bits/stdc++.h>

using namespace std;

#define REP(i, n) for(int i = 0; i < (int)(n); ++ i)
#define FOR(i, b, e) for(auto i = b; i < e; ++ i)

string go() {
	int n = 4, A, B;
	array<array<int, 4>, 4> a, b;

	cin >> A;
	REP(i, n) REP(j, n) cin >> a[i][j];
	cin >> B;
	REP(i, n) REP(j, n) cin >> b[i][j];

	int f[17] = {0};
	REP(j, n) f[ a[A - 1][j] ] ++;
	REP(j, n) f[ b[B - 1][j] ] ++;

	vector<int> C;
	FOR(i, 1, 16+1) if(f[i] == 2) C.push_back(i);

	if(C.size() == 0) return "Volunteer cheated!";
	if(C.size() == 1) return to_string(C[0]);
	return "Bad magician!";
}

int main() {
	freopen("A-small-attempt0.in", "rt", stdin);
	freopen("A-small-attempt0.out", "wt", stdout);

	int T;
	cin >> T;
	for(int t = 1; t <= T; ++ t) {
		cout << "Case #" << t << ": " << go() << endl;
	}
	return 0;
}
