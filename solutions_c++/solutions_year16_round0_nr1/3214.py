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

const double E = 1e-8;
const double PI = acos(-1);


void sol(long long n) {
	if (n == 0) {
		printf("INSOMNIA\n");
		return ;
	}

	int left = 10;
	bool x[10];
	fill(x, x + 10, false);
	long long c = 1;
	while (true) {
		long long m = c * n;
		long long mm = m;
		while (mm != 0) {
			int r = mm % 10;
			if (!x[r])
				left--;
			x[r] = true;
			mm /= 10;
		}
		if (left <= 0) {
			printf("%lld\n", m);
			return ;
		}
		c++;
	}
}

int main() {
    ios::sync_with_stdio(false);

    int nc;
    scanf("%d", &nc);
    for (int i = 1; i <= nc; i++) {
    	printf("Case #%d: ", i);

		long long n;
		scanf("%lld", &n);
    	sol(n);
    }
}





