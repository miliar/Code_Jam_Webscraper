#include <iostream>
#include <fstream>
#include <map>
#include <ctime>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <iomanip>

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

int t, tt;

int n, i, j, m;
double p1[1111], p2[1111];

int main() {


	f >> t;
	for (tt=1; tt <= t; tt++) {

		f >>n;
		for (i=1; i<=n; i++) {
			f >> p1[i];
		}

		for (i=1; i<=n; i++) {
			f >> p2[i];
		}

		sort (p1+1, p1+n+1);
		sort (p2+1, p2+n+1);

		int r1 = 0;
		int r2 = 0;


		//Startegy 1

		int j = n;
		for (i=n; i > 0; i--) {
			if (p2[j] > p1[i]) {
				r2++;
				j--;
			}
		}
		r2 = n - r2;


		// Strategy 2
		j = 1;
		for (i=1; i<=n; i++) {
			if (p1[i] > p2[j]) {
				r1++;
				j++;
			}
		}


		g << "Case #" << tt << ": ";
		g << r1 << " " << r2 << e;

	}


	return 0;

}
