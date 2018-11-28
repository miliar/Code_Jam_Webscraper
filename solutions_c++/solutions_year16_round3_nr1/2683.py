#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

int main(void) {
	cout.sync_with_stdio(false);
	int nTests;
	cin >> nTests;
	for(int t = 1; t <= nTests; ++t) {
		int N, S, p;
		cin >> N;
		vector<pair<int,char> > P;
		S = 0;
		for(int i = 0; i < N; ++i) {
			cin >> p;
			S += p;
			P.push_back(make_pair(p, 'A' + i));
		}
		cout << "Case #" << t << ": ";
		while(S > 0) {
			sort(P.begin(), P.end(), greater<pair<int,char> >());
			int half = (S - 2) / 2;
			if (P[0].first >= 2) {
				if (half < P[1].first) {
					cout << P[0].second << P[1].second << ' ';
					--P[0].first;
					--P[1].first;
					S -= 2;
					if (P[0].first == 0) --N;
					if (P[1].first == 0) --N;
				} else {
					cout << P[0].second << P[0].second << ' ';
					P[0].first -= 2;
					S -= 2;
					if (P[0].first == 0) --N;
				}
			} else {
				if (N != 3) {
					cout << P[0].second << P[1].second << ' ';
					--P[0].first;
					--P[1].first;
					S -= 2;
					if (P[0].first == 0) --N;
					if (P[1].first == 0) --N;
				} else {
					cout << P[0].second << ' ';
					--P[0].first;
					S -= 1;
					if (P[0].first == 0) --N;
				}
			}
		}
		cout << endl;
	}
	return 0;
}
