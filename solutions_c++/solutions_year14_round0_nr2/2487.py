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

double cc, ff, xx, rate, res, moment;

int main() {

	g << fixed << setprecision(7);

	f >> t;
	for (tt=1; tt <= t; tt++) {

		f >> cc >> ff >> xx;
		rate = 2.0;
		res = 0;
		moment = 0;

		if (xx < cc) {
			res = xx / rate;
		} else {
			for (;;) {
				res += cc / rate;
				if ( (xx-cc) / rate > xx / (rate+ff) ) {
					rate += ff;
				} else {
					res += (xx-cc) / rate;
					break;
				}
			}

		}

		g << "Case #" << tt << ": ";
		g << res << e;
	}


	return 0;

}
