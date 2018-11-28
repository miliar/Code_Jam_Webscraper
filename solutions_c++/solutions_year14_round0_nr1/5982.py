#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
//#include <ctime>
#include <map>
using namespace std;

int row[4];

void solve() {
	int firstRow;
	int secondRow;	
	int temp;

	cin >> firstRow;
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			cin >> temp;
			if (i == firstRow-1) {
				row[j] = temp;
			}
		}
	}
	cin >> secondRow;
	int count = 0;
	int val = -1;
	for (int i  = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			cin >>temp;
			if (i == secondRow-1) {	
				for (int k = 0; k < 4; k++) {
					if (row[k] == temp) {
						val = temp;
						count++;
					}
				}
			}
		}
	}

	if (count == 1) {
		cout << val <<  endl;
	} else if (count == 0) {
		cout << "Volunteer cheated!" << endl;
	} else {
		cout << "Bad magician!" << endl;
	}

}

int MAIN() {
	int numTestCases;
	cin >> numTestCases;
	for (int i = 1; i <= numTestCases; i++) {
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	//cout << fixed << setprecision(16);
	return MAIN();
}



