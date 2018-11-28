#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

void printLawn(int *lawn, int n, int m) {
	for (int i=0; i<n; i++) {
		for (int j=0; j<m; j++) {
			cout << *(lawn + i*m + j) << " ";
		}
		cout << endl;
	}
}

bool solve() {
	// input
	int n, m;
	cin >> n >> m;
	int target[n][m];

	for (int i=0; i<n; i++) {
		for (int j=0; j<m; j++) {
			cin >> target[i][j]; 
		}
	}

	// cout << n << " " << m << endl;
	//	printLawn((int *)target, n, m);

	// solve
	bool ok[n][m];
	int lawn[n][m];
	for (int i=0; i<n; i++) {
		for (int j=0; j<m; j++) {
			lawn[i][j] = 100;
			ok[i][j] = false;
		}
	}

	int todoCt = n*m;
	while (todoCt > 0) {
		/// find max from unreached targets
		int maxI=-1, maxJ=-1;
		int maxH = -1;
		for (int i=0; i<n; i++) {
			for (int j=0; j<m; j++) {
				if ( !ok[i][j] && target[i][j] > maxH ) {
					maxH = target[i][j];
					maxI = i;
					maxJ = j;
				}
			}
		}
		// cout << "maxH:" << maxH << endl;

		// test maxi-th row
		bool flag = true;
		for (int j=0; j<m; j++) {
			if ( ok[maxI][j] && target[maxI][j] > maxH ) {
				flag = false;
				break;
			}
		}

		if (flag) {
			// cut grass on the maxi-th row 
			for (int j=0; j<m; j++) {
				lawn[maxI][j] = min(lawn[maxI][j], maxH);
				if (!ok[maxI][j] && lawn[maxI][j] == target[maxI][j]) {
					ok[maxI][j] = true;
					todoCt--;
				}
			}
		}

		if (flag) {
//			cout << endl;
//			printLawn((int *)lawn, n, m);
			continue;
		}

		// test maxj-th column
		flag = true;
		for (int i=0; i<n; i++) {
			if ( ok[i][maxJ] && target[i][maxJ] > maxH ) {
				flag = false;
				break;
			}
		}

		if (flag) {
			for (int i=0; i<n; i++) {
				lawn[i][maxJ] = min(lawn[i][maxJ], maxH);
				if ( !ok[i][maxJ] && lawn[i][maxJ] == target[i][maxJ]) {
					ok[i][maxJ] = true;
					todoCt --;
				}
			}
		}
//		cout << endl;
//		printLawn((int *)lawn, n, m);

		if (!flag)
			break;
	}

	return todoCt == 0;
}

int main()
{
	int caseNum;
	cin >> caseNum;

	for (int caseNo=1; caseNo <= caseNum; ++caseNo) {
		int res = solve();
		cout << "Case #" << caseNo << ": ";
		switch (res) {
			case true:
				cout << "YES" << endl;
				break;
			case false:
				cout << "NO" << endl;
				break;
		}

	}

	return 0;
}
