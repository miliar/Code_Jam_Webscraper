#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main()
{
	int T;
	cin >> T;
	cout.precision(8);
	for (int casenum = 1; casenum <= T; ++casenum) {
		long N;
		cin >> N;
		double D[N], M[N];
		long H[N];
		double slowest = 0.0;

		forn(i, N) {
			cin >> D[i] >> H[i] >> M[i];
			slowest = max(slowest, (M[i] + H[i] - 1) * (360 - D[i]) / 360.0);
		}
		map<double, long> events;
		forn(i, N) {
			events[0] += H[i];
			forn(j, H[i]) {
				double time_a = M[i] + j;
				double time = time_a * (360 - D[i])/360;
				events[time]--;
				while (time < slowest) {
					time += time_a;
					events[time]++;
				}
			}
		}
		long total = 0;
		long min_total = LONG_MAX;
		for (auto&& e : events) {
			//cout << e.first << ':' << e.second << endl;
			total += e.second;
			//cout << total << endl;
			min_total = min(total, min_total);
		}

		cout << "Case #" << casenum << ": " << min_total << endl;
	}
	return 0;
}

