#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <locale>
#include <stdlib.h> 
using namespace std;

int main() {
	
	int T, t, d, C;
	int map[10];

	cin >> T;
	for (t = 0; t < T; t++) {
		// Check for INSOMNIA
		cin >> C;
		if (C == 0) {
			cout<<"Case #" << t+1 << ": INSOMNIA" << endl;
			continue;
		}

		// Reset array
		// and set up variables
		memset(map, 0, sizeof map);
		int c = 0, mnum = 0;
		while (++c) {
			long long temp = c * C;

			// Loop single number
			while (temp >= 10) {
				d = temp % 10;
				if (map[d] == 0) {
					map[d] = 1;
					mnum++;
				}
				temp = temp / 10;
			}

			if (map[temp] == 0) {
				map[temp] = 1;
				mnum++;
			}

			// We got all numbers
			if (mnum == 10) {
				cout<<"Case #" << t+1 << ": " << c * C << endl;
				break;
			}
		}
	}
}
