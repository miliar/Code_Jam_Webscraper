#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		int N;
		cin >> N;
		vector<pair<int, char> > P(N);
		int total = 0;
		for (int i = 0; i < N; ++i) {
			cin >> P[i].first;
			total += P[i].first;
			P[i].second = 'A' + i;
		}
		cout << "Case #" << t << ": ";
		sort(P.rbegin(), P.rend());
		while (P[0].first > P[1].first) {
			cout << P[0].second << " ";
			--P[0].first;
		}
		for (int i = 2; i < N; ++i) {
			while (P[i].first > 0) {
				cout << P[i].second << " ";
				--P[i].first;
			}
		}
		for (int i = 0; i < P[0].first; ++i) {
			cout << P[0].second << P[1].second << " ";
		}
		cout << "\n";
	}
	return 0;
}