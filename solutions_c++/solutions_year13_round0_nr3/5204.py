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

int main () {
	int pocet, i, a1, a2, a3, ii, iii, draw, j, a, b, pali[5], vys;
	string r;
	char znak, rr[3][5][5];
	cin >> pocet;
	pali[0] = 1;
	pali[1] = 4;
	pali[2] = 9;
	pali[3] = 121;
	pali[4] = 484;
	for (i = 0; i < pocet; i++) {
		cin >> a;
		cin >> b;
		vys = 0;
		for (ii = 0; ii < 5; ii++)
			if (pali[ii] >= a && pali[ii] <= b)
				vys++;
		cout << "Case #" << i + 1 << ": " << vys << endl;
	}
	return 0;
}
