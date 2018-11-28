#define _USE_MATH_DEFINES
#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>

using namespace std;

int n_split_needed(int pancakes, int ne) {
	int d = (pancakes%ne == 0) ? 1 : 0;
	return floor(pancakes / ne) - d;
}

int n_split_needed_total(int ne, vector<int>& p, int d) {
	int s = 0;
	for (int j = 0; j < d; j++) {
		if (p[j] > ne)
			s += n_split_needed(p[j], ne);
	}
	return s;
}

int main() {


	int t,
		d,
		bestscore,
		ne_max,
		ns;

	cin >> t;
	for (int i = 0; i < t; i++) {

		//cout << "i:" << i << endl;

		cin >> d;

		vector<int> p(d);


		for (int j = 0; j < d; j++) {
			cin >> p[j];
			ne_max = max(ne_max, p[j]);
		}

		bestscore = ne_max;

		for (int ne = 1; ne <= ne_max; ne++) {
			
			ns = n_split_needed_total(ne, p, d);

			//cout << ne << ":" << ne+ns << endl;

			if (ne + ns < bestscore) {
				bestscore = ne + ns;
			}
		}



		cout << "Case #" << i + 1 << ": " << bestscore << endl;

	}
	cin.ignore();
	cin.ignore();
	cin.ignore();
	return 0;
}
