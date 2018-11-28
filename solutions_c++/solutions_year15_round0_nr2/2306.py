#include <iostream>
#include <cstdio>
#include <vector>
#include <string>

using namespace std;

#define FILE "D"

int main() {
	ios_base::sync_with_stdio(false);
	freopen(FILE ".in", "r", stdin);
	freopen(FILE ".out", "w", stdout);
	int T;
	cin >> T;
	for (int _ = 0; _ < T; ++_) {
		int D;
		cin >> D;
		int A[D];
		for (int i = 0; i < D; ++i) {
			cin >> A[i];
		}	
		int ans = 10000;
		for (int maxans = 1; maxans <= 1000; ++maxans) {
			int nsplits = 0;
			for (int i = 0; i < D; ++i) {
				nsplits += (A[i] + maxans - 1)/ maxans - 1;
			}
			ans = min(ans, maxans + nsplits);
		}
		/*
			Print answer
		 */
		cout << "Case #" << _+1 << ": ";
		cout << ans;

		cout << "\n";
	}
	return 0;
}