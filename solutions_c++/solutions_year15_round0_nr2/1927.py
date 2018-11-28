#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <queue>
#include <numeric>
#include <array>
#include <map>
#include <unordered_map>
#include <functional>
#include <iostream>
#include <thread>
#include <sstream>
#include <atomic>

using namespace std;

int main () {
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		int D, maxP=0;
		scanf("%d", &D);
		vector<int> P(D);
		for (auto& p:P) {
			scanf("%d", &p);
			maxP=max(maxP, p);
		}
		int w=maxP++;
		while (--maxP) {
			int ad=maxP;
			for (auto& p:P) {
				ad+=(p-1)/maxP;
			}
			w=min(w, ad);
		}
		printf("Case #%d: %d\n", t, w);
	}
	return 0;
}
