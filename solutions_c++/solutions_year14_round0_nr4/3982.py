#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <queue>

#include<stdio.h>
#include<ctype.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>
//#include <random>
#include <time.h>

using namespace std;

#define X first
#define Y second
#define MP make_pair
#define PB push_back
#define SZ size

int main() {
	int i, aktual, zvysok, pocet, a, pozadDlzka, pozadPocet, aktualDlzka, ii, iii, c, vys2, vys;
	double f,x,akt, k;
	vector<double> on, ona, on2, on3;
	scanf("%d", &pocet);
	for (a = 0; a < pocet; a++) {
		scanf("%d", &c);
		for (i = 0; i < c; i++) {
			cin >> k;
			ona.PB(k);
			//cout << k;
		}
		for (i = 0; i < c; i++) {
			cin >> k;
			on.PB(k);
		}
		sort(ona.begin(), ona.end());
		sort(on.begin(), on.end());
		on3 = on;
		vys = 0;
		for (i = 0; i < c; i++) {
			if (ona[i] > on3[0]) {
				vys++;
				for (ii = 1; ii < on3.SZ(); ii++) {
					on2.PB(on3[ii]);
				}
				on3.clear();
				on3 = on2;
				on2.clear();
			} else {
				for (ii = 0; ii < on3.SZ() - 1; ii++) {
					on2.PB(on3[ii]);
				}
				on3.clear();
				on3 = on2;
				on2.clear();
			}
		}
		//cout << vys;
		vys2 = 0;
		for (i = c - 1; i >= 0; i--) {
			if (ona[i] > on[i]) {
				for (ii = 1; ii < on.SZ(); ii++)
					on2.PB(on[ii]);
				vys2++;
				on.clear();
				on = on2;
				on2.clear();
				sort(on.begin(), on.end());
			} else {
				for (ii = 0; ii < on.SZ(); ii++) {
					if (on[ii] > ona[i]) {
						for (iii = 0; iii < on.SZ(); iii++) {
							if (ii != iii)
								on2.PB(on[iii]);
						}
						break;
					}
				}
				on.clear();
				on = on2;
				on2.clear();
				sort(on.begin(), on.end());
				
			}			
		}
		on.clear();
		ona.clear();
		cout << "Case #" << a + 1 << ": "<< vys << " " << vys2 << endl;
	}
	return 0;
}