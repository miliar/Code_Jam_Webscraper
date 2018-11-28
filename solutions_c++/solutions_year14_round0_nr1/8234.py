/*
 * A.cpp
 *
 *  Created on: Apr 12, 2014
 *      Author: kerollosasaad
 */
#include<bits/stdc++.h>
using namespace std;

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("Asmall.out", "w", stdout);

	int tc, counter = 1;
	cin >> tc;
	while (tc--) {
		int first, second, arr[2][4], tmp, ok = 0, ret = 0;
		cin >> first;
		for (int i = 0; i < 16; i++)
			((i / 4) + 1 == first) ? cin >> arr[0][i % 4] : cin >> tmp;
		cin >> second;
		for (int i = 0; i < 16; i++)
			((i / 4) + 1 == second) ? cin >> arr[1][i % 4] : cin >> tmp;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				if (arr[0][i] == arr[1][j])
					ok++, ret = arr[0][i];
		/*
		 Case #1: 7
		 Case #2: Bad magician!
		 Case #3: Volunteer cheated!
		 */
		cout << "Case #" << counter++ << ": ";
		if (ok > 1)
			cout << "Bad magician!\n";
		else if (ok == 1)
			cout << ret << endl;
		else
			cout << "Volunteer cheated!\n";
	}

	return 0;
}

