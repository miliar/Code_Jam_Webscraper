#include <iostream>
#include <stdbool.h>
#include <stdint.h>
#include <vector>
#include <cstring>
#include "gmpxx.h"
typedef mpz_class bignumber;

using namespace std;

void usage() 
{
	cout << "usage: cat testset.txt | ./main > output.txt \n";
	cout << "\ttestset - testset filename\n";
}

long area(long radius) 
{
	long rout = radius + 1;
	long rin = radius;
	
	return (rout*rout) - (rin*rin);
}

int solve(long startr, long ml) 
{
	// a = (rout^2 - rin^2) ml
	int numrings = 0;
	do {
		numrings++;
		ml -= area(startr);
		// cout << ml << "mL" <<  endl;
		startr += 2;
	} while (ml > 0);

	if (ml < 0) numrings--;

	return numrings;
}


int main(int argc, char *argv[])
{
	int i, numcases;
	long r, t;

	if (argc != 1) {
		usage();
		return -1;
	}

	cin >> numcases;
	for (i=1; i<=numcases; i++) {
		cin >> r >> t;

		// cout << r << " rad " << t << endl;
		cout << "Case #" << i << ": " << solve(r, t) << endl;
	}

	return 0;
}
