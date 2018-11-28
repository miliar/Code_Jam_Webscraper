#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <iterator>
#include <string>
#include <memory.h>
using namespace std;

#include <cctype>
#include <cstdio>
#include <cstdarg>
#include <ctime>
#include <cmath>
#include <cassert>


const int INF = (1 << 30) - 1;
const float PI = (float)acos(-1.0);
const float EPS = 1e-5;
const float BASE2 = 1.0/log(2);

int cases;

int K,C,S;


int main ()
{
	long long x;
	scanf("%d", &cases);
	for (int k = 1; k <= cases; k++) {
		scanf("%d%d%d", &K, &C, &S);
//		cout << K << " " << C << " " << S << endl;
		printf("Case #%d: ", k);
		if (C+S <= K) {
			printf("IMPOSSIBLE\n");
			continue;
		}
		int z = K;
		for (int i = max(K-C, 0); i >= 0; i--) {
//			cout << K-S << " " << i << endl;
			if (i == 0) {
				x = 0;
				while (z>=1) {
					x *= K;
					x += z-1;
					--z;
				}
				printf("%lld\n", x+1);
			}
			else {
				printf("%d ", z--);
			}
		}
	}
	return 0;
}


