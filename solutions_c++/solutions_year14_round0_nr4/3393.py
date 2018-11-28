#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	freopen("D-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T, N;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> N;
		vector< pair<double, bool> > w(2 * N);
		for (int i = 0; i < 2 * N; i++) {
			double tw;
			cin >> tw;
			w[i] = make_pair(tw, (i < N));
		}

		sort(w.begin(), w.end());

		int balance1 = 0, balance2 = 0;
		int pt1 = 0, pt2 = 0;
		for (int i = 0; i < 2 * N; i++)
			if (w[i].second) {
				if (balance1) {
					balance1--;
					pt1++;
				}
				balance2++;
			} else {
				balance1++;
				if (balance2) {
					balance2--;
					pt2++;
				}
			}

		cout << "Case #" << t << ": " << pt1 << " " << N - pt2 << endl;
	}
}
