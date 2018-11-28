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

int main() {
	int i, aktual, zvysok, pocet, a, pozadDlzka, pozadPocet, aktualDlzka;
	int c,f,x,akt,vys,ii;
	int p[4][4], p2[4];
	scanf("%d", &pocet);
	for (a = 0; a < pocet; a++) {
		cin >> c;
		c--;
		for (i = 0; i < 4; i++) {
			for (ii = 0; ii < 4; ii++)
				scanf("%d", &p[i][ii]);
		}
		for (i = 0; i < 4; i++) {
			p2[i] = p[c][i];
		}
		cin >> c;
		c--;
		for (i = 0; i < 4; i++) {
			for (ii = 0; ii < 4; ii++)
				scanf("%d", &p[i][ii]);
		}
		vys = 0;
		x = -1;
		for (i = 0; i < 4; i++) {
			for (ii = 0; ii < 4; ii++) {
				if (p[c][i] == p2[ii]) {
					vys++;
					x = p2[ii];
				}
			}
		}
		if (vys == 0)
			cout << "Case #" << a + 1 << ": Volunteer cheated!" << endl;
		if (vys == 1)
			cout << "Case #" << a + 1 << ": " << x << endl;
		if (vys > 1)
			cout << "Case #" << a + 1 << ": Bad magician!" << endl;
	}
	return 0;
}