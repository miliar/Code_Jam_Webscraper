#include <iostream>
#include <algorithm>

using namespace std;

bool gt(int a, int b) {
	return a > b;
}


int costs[1001][1001];

void initialize_costs() {
	for (int i = 0; i < 1001; ++i) {
		costs[i][i] = 0;
	}
	for (int i = 2; i < 1001; ++i) {
		for (int j = 1; j < i; ++j) {
			int max2 = (i+1)/2;
			int max3 = (i+2)/3;
			int cost2 = 1 + 2 * costs[max2][j < max2 ? j : max2];
			int cost3 = 2 + 3 * costs[max3][j < max3 ? j : max3];
			costs[i][j] = cost2 < cost3 ? cost2 : cost3;
		}
	}
}

int main()
{
	initialize_costs();

	int T;
	cin >> T;
	for (int j = 1; j <= T; ++j) {
		int D;
		cin >> D;
		int plates[D];
		for (int i = 0; i < D; i++) {
			cin >> plates[i];
		}
		sort(plates, plates+D, gt);
		
		int minutes = plates[0];
		for (int m = minutes - 2; m > 0; --m) {
			int cost = 0;
			for (int i = 0; i < D; ++i) {
				cost += costs[plates[i]][m];
			}
			int total = cost + m;
			if (total < minutes) {
				minutes = total;
			}
		}
		cout << "Case #" << j << ": " << minutes << endl;
	}
	return 0;
}

