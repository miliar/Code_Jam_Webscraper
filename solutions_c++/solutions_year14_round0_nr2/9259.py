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
		printf("Case #%d: ", t);
		double C, F, X;
		scanf("%lf%lf%lf", &C, &F, &X);
		int K=max(ceil(X/C - 2.0/F - 1.0), 0.0);
		double R = X/(2+K*F);
		for (int k=K-1; k>=0; k--) {
			R+=C/(2+k*F);
		}
		printf("%.7lf", R);
		printf("\n");
	}
	return 0;
}
