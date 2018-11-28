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

#include <bitset>
void show_binary(unsigned int x) {
    PRINT("%s\n", bitset<32>(x).to_string().c_str());
}

void solve() {
	int n;
	int k;
	scanf("%d %d", &n, &k);
	vector<float> prob(n);
	for (int i = 0; i < n; i++) {
		scanf("%f", &prob[i]);
		SHOW(prob[i])
	}

	vector<float> now(k);
	int top = 1 << n;
	float ans = 0;
	for (unsigned int i = 0; i < top; i++) {
		int n1 = __builtin_popcount(i);
		if (n1 != k)
			continue;

		show_binary(i);
		int cnt = 0;
		for (int x = 0; x < n; x++) {
			if ((1 << x) & i) {
				now[cnt++] = prob[x];
				SHOW("choose", prob[x])
			}
		}

		int topK = 1 << k;
		float tmpTotal = 0;
		for (unsigned int j = 0; j < topK; j++) {
			int nY = __builtin_popcount(j);
			if (nY != k / 2)
				continue;

			show_binary(j);

			float tmp = 1;
			for (int y = 0; y < k; y++) {
				if ((1 << y) & j) {
					tmp *= now[y];
				}
				else {
					tmp *= 1 - now[y];
				}
			}
			SHOW(tmp)
			tmpTotal += tmp;
		}
		SHOW(tmpTotal)
		ans = max(ans, tmpTotal);
	}
	printf("%.7f\n", ans);
}

int main() {
    int nc;
    scanf("%d", &nc);
    for (int c = 1; c <= nc; c++) {
    	printf("Case #%d: ", c);
    	solve();
    }
}





