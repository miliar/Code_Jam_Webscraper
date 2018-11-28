#include <iostream>
#include <algorithm>
using namespace std;

int* getrow() {
	int a, i, j, dummy, *r = new int[4];
	cin >> a;
	for (i = 1; i < a; i++)
		for (j = 0; j < 4; j++)
			cin >> dummy;
	for (j = 0; j < 4; j++)
		cin >> r[j];
	for (i = a+1; i <= 4; i++)
		for (j = 0; j < 4; j++)
			cin >> dummy;
	return r;
}

bool bs(int* r, int num) {
		
}

int main () {
	int T, *r1, *r2, cand, candnum, i, j;
	cin >> T;
	for (int x = 1; x <= T; x++) {
		cand = 0;	candnum = 0;
		r1 = getrow();
		r2 = getrow();
		for (i = 0; i < 4; i++)
			for (j = 0; j < 4; j++)
				if (r1[j] == r2[i]) {
					candnum++;
					cand = r2[i];
				}
		cout << "Case #" << x << ": ";
		switch (candnum) {
			case 0: 	cout << "Volunteer cheated!";	break;
			case 1: 	cout << cand;					break;
			default: 	cout << "Bad magician!";
		}
		cout << endl;
	}
}
