// /GCJ-2014/TEST/COOKIE

#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
#include <climits>
#include <map>
#include <set>
#include <utility>

using namespace std;

int main() {
	int n_tc = 0;
	cin >> n_tc;

	for(int tc = 1; tc <= n_tc; tc++) {
		long double farmcost = 0.0, farmfactor = 0.0, target = 0.0, factor = 2.0, ttime = 0.0;
		cin >> farmcost >> farmfactor >> target;

		while ((target / factor) >= (farmcost / factor) + (target / (factor + farmfactor)))
			ttime += (farmcost / factor), factor += farmfactor;

		ttime += (target / factor);
		cout << "Case #" << tc << ": ";
		printf("%.7llf\n", ttime);
	}
	return 0;
}