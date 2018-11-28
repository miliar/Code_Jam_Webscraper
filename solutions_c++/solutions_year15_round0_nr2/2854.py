#include <bits/stdc++.h>

using namespace std;

int solve() {
	int D;
	cin >> D;
	vector<int> P(D);
	for(int &a: P) cin >> a;

	int best = 20000;
	for(int i=1; i <= 1000; i++) {
		int akt = i;
		for(int a:P) {
			akt += (a+i-1)/i - 1;
		}
		best = min(akt, best);
	}
	return best;
}

int main() {
	int t;
	cin >> t;
	for(int i=1; i <=t; i++) cout << "Case #" << i << ": " << solve() << endl;
}