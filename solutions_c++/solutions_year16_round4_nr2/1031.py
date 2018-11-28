#include <algorithm>
#include <cctype>
#include <chrono>
#include <climits>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <stack>
#include <string>
#include <strstream>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
using namespace std;
typedef int64_t i64;
typedef double dbl;

#define NN 220

int t;
int N, K;
double P[NN];

int main()
{
	scanf("%d", &t);
	for (int ti = 0; ti < t; ++ti) {
		scanf("%d%d", &N, &K);
		for (int i = 0; i < N; ++i) {
			scanf("%lg", &P[i]);
		}
		int mask = 1 << N;
		vector<int> bits;
		bits.reserve(N);
		double best = 0;
		for (int m = 0; m < mask; ++m) {
			bits.clear();
			for (int i = 0; i < N; ++i) {
				if (m & (1 << i)) {
					bits.push_back(i);
				}
			}
			if (int(bits.size()) != K) {
				continue;
			}
			int mask2 = 1 << K;
			double sum = 0;
			for (int n = 0; n < mask2; ++n) {
				int nbits = 0;
				for (int i = 0; i < K; ++i) {
					if (n & (1 << i)) {
						++nbits;
					}
				}
				if (nbits != K/2) {
					continue;
				}
				double prod = 1.;
				for (int i = 0; i < K; ++i) {
					if (n & (1 << i)) {
						prod *= P[bits[i]];
					} else {
						prod *= 1. - P[bits[i]];
					}
				}
				//printf("prod=%lf\n", prod);
				sum += prod;
			}
			//printf("sum=%lf\n", sum);
			best = max(best, sum);
		}
		printf("Case #%d: %.7lf\n", ti+1, best);
	}
	return 0;
}

/* vim: set ts=4 sw=4 noet: */
