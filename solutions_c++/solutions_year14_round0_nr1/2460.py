#include <iostream>
#include <fstream>
#include <map>
#include <ctime>
#include <cstdlib>
#include <string>
#include <algorithm>

#define e '\n'

using namespace std;

//#define FILE "hashuri"

#define INF 1023456789
#define ll long long

#ifdef FILE
ifstream f(string (string(FILE) + ".in").c_str());
ofstream g(string (string(FILE) + ".out").c_str());
#endif
#ifndef FILE
#define f cin
#define g cout
#endif

int i, j, n, m, tt, t, x, y, found, result;
int v[5][5];
int w[20];

int main() {


	f >> t;
	for (tt=1; tt <= t; tt++) {
		for (i=1; i<=16; i++) {
			w[i] = 0;
		}
		found = 0;
		result = 0;


		f >> n;
		for (i=1 ; i<=4 ; i++) {
			for (j=1; j<=4; j++) {
				f >> x;
				if (i==n) {
					w[x] ++;
				}
			}
		}

		f >> n;
		for (i=1 ; i<=4 ; i++) {
			for (j=1; j<=4; j++) {
				f >> x;
				if (i==n) {
					w[x] ++;
				}
			}
		}

		for (i=1; i<=16; i++) {
			if (w[i] == 2) {
				found ++;
				result = i;
			}
		}

		g << "Case #" << tt << ": ";
		if (found ==0) {
			g << "Volunteer cheated!" << e;
		} else if (found == 1) {
			g << result << e;
		} else {
			g << "Bad magician!" << e;
		}
	}


	return 0;

}
