#include <iostream>     // std::cout
#include <algorithm>    // std::next_permutation, std::sort
#include <math.h>
#include <stdlib.h>
#include <stack>
#include <queue>
#include <stdio.h>
#include <stdint.h>

using namespace std;


uint64_t m[1001];

int b;

uint64_t n;



uint64_t val(uint64_t time) {

	uint64_t facuti = 0;
	for (int i = 0; i < b; ++i) {
		facuti += (time / m[i]);
		if (time % m[i] != 0 ) facuti ++;
	}
	return facuti;
}

int bs(uint64_t imin, uint64_t imax) {
	while (imax >= imin) {

		uint64_t imid = imin + (imax - imin) / 2;

		uint64_t f = val(imid);
		uint64_t g = val(imid + 1);
	//	cout << imid << " -------- " << f  << " " << g<< " " << n << " " << (f < n && n <= g) << endl;
		if(f < n && n <= g)
			return imid; 
		else if (f < n)
		        imin = imid + 1;
		else         
			imax = imid - 1;
	}
	return -1;
}




int main () {
	int T;
	cin >> T;

	for (int t = 1; t <= T; ++t) {

		cin >> b >> n;
		uint64_t prod = 1;
		for (int i = 0; i < b; ++i) {
			cin >> m[i];

			prod *= m[i];
		}


		uint64_t sum = 0;
		for (int i = 0; i < b; ++i) {
			sum += (prod / m[i]);
		}

		n = (n % sum);
		if (n == 0)  n += sum;

		uint64_t end = (n + 1) * 100000;
		uint64_t start = 0; 
		uint64_t bbs = bs(start, end);

		uint64_t f = val(bbs);

//		cout << bbs << " " << f << endl;
		int rez = -1;
		for (int i = 0; i < b; ++i) {
			if (bbs % m[i] == 0) {
				f ++;
				if (f == n) {
					rez = i + 1;
					break;
				}
			}
		}

		printf("Case #%d: %d\n", t, rez);

	}
	return 0;
}
