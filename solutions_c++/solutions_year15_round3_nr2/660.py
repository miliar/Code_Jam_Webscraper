#include <iostream>     // std::cout
#include <algorithm>    // std::next_permutation, std::sort
#include <math.h>
#include <stdlib.h>
#include <stack>
#include <queue>
#include <stdio.h>
#include <stdint.h>

using namespace std;




/*
uint64_t val(uint64_t time) {

	uint64_t facuti = 0;
	for (int i = 0; i < b; ++i) {
		facuti += (time / m[i]);
		if (time % m[i] != 0 ) facuti ++;
	}
	return facuti;
}



// ALWAYS USE THIS BINARY SEARCH FCT. OTHERS HAVE BUGS.
uint64_t bs(uint64_t imin, uint64_t imax) {
	while (imax > imin + 1) {

		uint64_t imid = imin + (imax - imin) / 2;
		uint64_t f = val(imid);
		if (f < n)
		        imin = imid;
		else         
			imax = imid;
	}
	return imin;
}


uint64_t gcd(uint64_t a, uint64_t b)
{
    for (;;)
    {
        if (a == 0) return b;
        b %= a;
        if (b == 0) return a;
        a %= b;
    }
}

uint64_t lcm(uint64_t a, uint64_t b)
{
    uint64_t temp = gcd(a, b);

    return temp ? (a / temp * b) : 0;
}
*/
//uint64_t m[1001];


uint64_t K,L,S, mmax = 0 ;

string keyboard = "";
string target = "";

double rez = 0;


void bkt(string prefix, bool findMax) {
	if (prefix.size() == S) {

		uint64_t nroccur = 0;
		for (int i = 0; i + target.size() <= prefix.size(); ++i) {
			bool isequal = true;
			for (int j = 0; j < target.size(); ++j) {
				if (target[j] != prefix[i + j]) {
					isequal = false;
					break;
				}
			}
			if (isequal) nroccur ++;
		}

		if (findMax) {
			mmax = max(mmax, nroccur);
		} else {
			rez += (mmax - nroccur);
		}

		return;
	}

	for (int i = 0; i < keyboard.size(); ++i) {
		string x = prefix + keyboard[i];
		bkt(x, findMax);
	}
}


int main () {
	int T;
	cin >> T;

	for (int t = 1; t <= T; ++t) {

		cin >> K >> L >> S;
		cin >> keyboard;
		cin >> target;

		mmax = 0;
		rez = 0;

		bkt("", true);
		bkt("",false);

		for (int i = 0; i < S; ++i) {
			rez /= K; 
		}

		printf("Case #%d: %.8lf\n", t, rez);
	}
	return 0;
}
