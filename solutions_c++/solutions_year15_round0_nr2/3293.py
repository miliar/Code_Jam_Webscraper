#include <iostream>
#include "stdio.h"

using namespace std;

int main() {
	int t;
	cin >> t;

	int d;
	int p[1024];
	for (int tcount = 1; tcount <= t; ++tcount) {
		cin >> d;

		int pmax = -1;
		for (int i = 0; i < d; ++i) {
			cin >> p[i];
			pmax = max(pmax, p[i]);
		}


		int tmin = 1000*1000;
		for (int i = 1; i <= pmax; ++i) {
			int time = 0;

			for (int j = 0; j < d; ++j)
				time += (p[j] - 1) / i;

			time += i;

			tmin = min(tmin, time);
			//cout << i << " " << time << endl;
		}

		cout << "Case #" << tcount << ": " << tmin << endl;
	}

	return 0;
}