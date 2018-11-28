#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

const int MAX_N = 1000;

int n;
double a[2][MAX_N];


int pointsWar(const double a[MAX_N], const double b[MAX_N]) {
	int points = 0;
	vector<double> numbers = vector<double>(b, b+n);
	for (int i = 0; i < n; ++i) {
		double value = a[i];
		vector<double>::iterator it = lower_bound(numbers.begin(), numbers.end(), value);
		if (it != numbers.end()) {
			numbers.erase(it);
			//cout << "B point" << endl;
			points++;
		}
		else {
			numbers.erase(numbers.begin());
			//cout << "A point" << endl;
		}
	}
	return points;
}

//int pointsDeceitfulWar() {
	//int points = 0;

	//int la = 0;//left a
	//int ra = n-1;//right a
	//int lb = 0;
	//int rb = n-1;

	//for (int j = 0; j < n; ++j) {
		//if (a[0][la] > a[1][lb]) {
			//points++;
			//la++;
			//lb++;
		//}
		//else if (a[0][ra] > a[1][rb]) {
			////make point
			//cout << "make point" << endl;
			//cout << a[0][ra] << " -> " << a[1][lb] << endl;
			//points++;
			//ra--;
			//lb++;
		//}
		//else {
			////trick into losing best part
			//cout << "trick" << endl;
			//cout << a[0][la] << " -> " << a[1][rb] << endl;
			////pb++;
			//la++;
			//rb--;
		//}
	//}
	//return points;
//}

int main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cin >> n;
		for (int j = 0; j < 2; ++j) {
			for (int k = 0; k < n; ++k)
				cin >> a[j][k];
			sort(a[j], a[j]+n);
		}

		cout << "Case #" << i << ": " << pointsWar(a[1], a[0]) << ' ' << n - pointsWar(a[0], a[1]) << endl;
		//cout << "Case #" << i << ": " << pointsWar(a[0], a[1]) << endl;
		//cout << "Case #" << i << ": " << pointsDeceitfulWar() << ' ' << pointsWar() << endl;
		//cout << "------------------" << endl << endl;
	}

	return 0;
}
