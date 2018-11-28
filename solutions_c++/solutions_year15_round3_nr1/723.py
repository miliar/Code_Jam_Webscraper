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

int b;

uint64_t r,c,w;




int main () {
	int T;
	cin >> T;

	for (int t = 1; t <= T; ++t) {

		cin >> r >> c >> w;

		uint64_t rez = 0;		
		
		rez = (c / w) + w;

		if (c % w == 0) rez = (c / w) + w - 1;

		int x = c/w;
		rez += (r - 1) * x;

		printf("Case #%d: %lu\n", t, rez);

	}
	return 0;
}
