#define _USE_MATH_DEFINES
#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <map>

using namespace std;


int main() {


	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {

		//cout << "i:" << i << endl;

		int m;
		cin >> m;

		//cout << "m:" << m << endl;

		int s = 0;
		int f = 0;

		for (int j = 0; j <= m; j++) {
			char c;
			cin >> c;

			//cout << j << ":" << c << endl;

			int a = c - '0';

			if (s < j) {
				f += j - s;
				s = j;
			}

			s += a;

			
		}

		cout << "Case #" << i + 1 << ": " << f << endl;

	}
	cin.ignore();
	cin.ignore();
	cin.ignore();
	return 0;
}
