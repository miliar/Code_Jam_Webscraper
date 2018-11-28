#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <stdint.h>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <queue>

using namespace std;

#define forl(i,a,b) for(int i = a; i < b; ++i)

int main()
{
	int cards1[4][4];
	int cards2[4][4];
	int possible[17];
	int numpossible;
	int ans1;
	int ans2;
	int numcases = 0;
	cin >> numcases;
	forl(casei, 0, numcases) {
		forl(i, 0, 17) possible[i] = 0;
		cin >> ans1;
		ans1--;
		forl(i, 0, 4) {
			forl(j, 0, 4) {
				cin >> cards1[i][j];
			}
		}
		cin >> ans2;
		ans2--;
		forl(i, 0, 4) {
			forl(j, 0, 4) {
				cin >> cards2[i][j];
			}
		}
		forl(i, 0, 4) {
			int card = cards1[ans1][i];
			forl(j, 0, 4) {
				if (cards2[ans2][j] == card) possible[card] = 1;
			}
		}
		numpossible = 0;
		forl(i, 1, 17) {
			if (possible[i] == 1) numpossible++;
		}
		if (numpossible == 0) {
			cout << "Case #" << (casei+1) << ": Volunteer cheated!" << endl;
		} else if (numpossible > 1) {
			cout << "Case #" << (casei+1) << ": Bad magician!" << endl;
		} else {
			forl(i, 1, 17) {
				if (possible[i] == 1) {
					numpossible = i;
					break;
				}
			}
			cout << "Case #" << (casei+1) << ": " << numpossible << endl;
		}
	}
	return 0;
}
