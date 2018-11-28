// ProblemA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

/*
int _tmain(int argc, _TCHAR* argv[])
{
	return 0;
}
*/


#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
using namespace std;
typedef long long ll;

ll isNotPrime(ll x) {

	ll x2 = sqrt((long double) x) + 1;

	for (ll i = 2; i < x2; ++i) {
		if ((x % i) == 0) {
			return i;
		}
	}
	return 0;
}

ll val(ll jamcoin, int width, int base) {
	ll result = 0;
	ll bit = 1;
	for (int i = 0; i < width; ++i) {
		int b = (jamcoin & bit) ? 1 : 0;
		result += b * pow((double) base, i);
		bit <<= 1;
	}
	return result;
}

void print_jamcoin(ll jamcoin, int width) {
	ll bit = 1 << (width - 1);
	for (int i = 0; i < width; ++i) {
		if (jamcoin & bit) {
			printf("1");
		}
		else {
			printf("0");
		}
		bit >>= 1;
	}
}



int main(void) {
	FILE *fp = fopen("test.txt", "rt");
	if (fp == NULL) {
		printf("failed to open file\n");
		return -1;
	}

	#define MAX_LINE_SIZE 0x1000
	char line[MAX_LINE_SIZE];

	int case_num;
	fgets(line, MAX_LINE_SIZE, fp);
	case_num = strtol(line, NULL, 10);
	
	for (int i = 1; i <= case_num; ++i) {
		printf("Case #%d:", i);

		puts("");

		// n, j
		fgets(line, MAX_LINE_SIZE, fp);
		char *p = line;
		int N = strtol(p, &p, 10);
		int J = strtol(p, &p, 10);

		// printf("%d %d", n, j);
		//for (ll i = 0; i < 1002; ++i) {
		//	printf("%lld, %lld\n", i, isNotPrime(i));
		//}

		if (1) {	// N == 6) {
			// example
			int count_ans = 0;
			ll jj = (ll) pow((double) 2, N - 2);
			for (ll j = 0; j < jj; ++j) {
				ll jamcoin = (1 << (N - 1)) | (1) | (j << 1);  
				
				//print_jamcoin(jamcoin, n);
				//printf(" ");
				

				ll values[11];
				int k;
				for (k = 2; k <= 10; ++k) {
					ll v = val(jamcoin, N, k);
					ll vv = isNotPrime(v);
					// printf("%lld=>%lld ", v, vv);
					if (vv) {
						values[k] = vv;
					}
					else {
						// printf("\n%lld is prime\n", v);
						break;
					}
				}
				if (k == 11) {
					++count_ans;
					print_jamcoin(jamcoin, N);
					for (int kk = 2; kk <= 10; ++kk) {
						printf(" %lld", values[kk]);
					}
					puts("");
				}

				if (count_ans == J) {
					break;
				}

			}
		}
		else if (N == 16) {
			// small
		}
		else {
			// large
		}





		puts("");

	}

	fclose(fp);
}