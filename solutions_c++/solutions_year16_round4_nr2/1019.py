#include <cstdio>
#include <cstring>
#include <map>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>

using namespace std;

int chosen;
double probs[20];
map<int, int> btoi;

double calc(int mask, bool sign) {
	int next, i;
	double res = 1.0;
	
	while (mask) {
		next = mask & (mask - 1);
		i = btoi[mask - next];
		mask = next;
		
		if (sign) {
			res *= probs[i];
		} else {
			res *= 1.0 - probs[i];
		}
	}	
	
	return res;
}

int main() {
	int T, N, K;
	
	for (int i = 0; i < 17; i++) {
		btoi[(1<<i)] = i;
	}
	
	scanf("%d", &T);
	for (int test = 1; test <= T; test++) {
		scanf("%d %d", &N, &K);
		
		for (int i = 0; i < N; i++) {
			scanf("%lf", &probs[i]);
		}
		
		double best = 0.0;
		for (int mask = 0; mask < (1<<N); mask++) {
			if (__builtin_popcount(mask) == K) {
				double cur = 0.0;
				for (int yes = 1; yes < (1<<N); yes++) {
					if (__builtin_popcount(yes) != K / 2) {
						continue;
					}
					
					if ( (mask | yes) == mask) {
						cur = cur + calc(yes, true) * calc(mask ^ yes, false);
					}
				}
				if (cur > best) {
					best = cur;
				}
			}
		}
		
		printf("Case #%d: %.6lf\n", test, best);
	}
	return 0;
}