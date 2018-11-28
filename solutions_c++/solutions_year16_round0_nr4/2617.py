#include <stdio.h>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <climits>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <bitset>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <cassert>

#define SHOW(...) {;}
#define REACH_HERE {;}
#define PRINT(s, ...) {;}
#define PRINTLN(s, ...) {;}

// #undef HHHDEBUG
#ifdef HHHDEBUG
#include "template.h"
#endif

using namespace std;

template<typename T>
using Grid = vector<vector<T>>;

const double PI = acos(-1);

#define NO "IMPOSSIBLE"

long long pow(long long x, long long p) {
	long long ret = 1;
	while (p--)
		ret *= x;
	return ret;
}

void sol() {
	long long k;
	long long c;
	long long s;
	scanf("%lld %lld %lld", &k, &c, &s);
	for (int i = 1; i <= s; i++)
		printf("%d ", i);
	printf("\n");
	return ;

	if (s * c < k) {
		printf(NO "\n");
		return ;
	}
	s = k / c;
	if (k % c)
		s++;

	SHOW(k, c, s)

	vector<long long> coef(c);
	for (int i = 0; i < coef.size(); i++) {
		coef[i] = pow(k, c - i - 1);
		SHOW(i, coef[i])
	}

	long long origin_idx = 0;
	for (int i = 0; i < s; i++) {
		long long idx = origin_idx * coef[0];
		SHOW(idx)
		for (int j = 0; j < c && origin_idx < k; j++) {
			long long off = j * coef[j];
			idx += off;
			SHOW(origin_idx, coef[j], off, idx)
			origin_idx++;
		}
		idx++;
		printf("%lld ", idx);
	}
	printf("\n");
}

int main() {
    ios::sync_with_stdio(false);

    int nc;
    scanf("%d", &nc);
    for (int i = 1; i <= nc; i++) {
    	printf("Case #%d: ", i);
    	sol();
    }
}




// C = 1:      L           G           L     
// C = 2:  L   G   L   G   G   G   L   G   L 
// C = 3: LGL GGG LGL GGG GGG GGG LGL GGG LGL


// C = 1:      L           G           L     
// C = 2:  L   G   L   G   G   G   L   G   L 


// C = 1: L       G
// C = 2: L   G   G   G
// C = 3: L G G G G G G G
//        0 1 2 3 4 5 6 7



