#include<iostream>
#include<vector>
using namespace std;

int main() {
	int T;
	cin >> T;
	vector<double> mine, opps;
	for (int tc = 1; tc <= T; tc++) {
		int N;
		cin >> N;
		mine.clear(); opps.clear();
		for (int i=0; i<N; i++) {
			double x; cin >> x;
			mine.push_back(x);
		}
		sort(mine.begin(), mine.end());
		for (int i=0; i<N; i++) {
			double x; cin >> x;
			opps.push_back(x);
		}
		sort(opps.begin(), opps.end());

		int win_deceit = 0;
		int j = N-1;
		for (int i = N-1; i >= 0; i--) {
			if (mine[j] > opps[i]) {
				win_deceit++;
				j--;
			}
		}

		int win_fair = 0;
		int kens_win = 0;
		j = 0;
		for (int i=0; i<N; i++) {
			while (j<N && opps[j]<mine[i]) j++;
			if (j == N) break;
			kens_win++; j++;
		}
		win_fair = N - kens_win;

		cout << "Case #" << tc << ": " << win_deceit << " " << win_fair << endl;
	}
}