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
		int maxS, w=0, sum=0;
		char S[1024];
		scanf("%d%s", &maxS, S);
		for (int i=0; i<=maxS; i++) {
			w=max(w, i-sum);
			sum+=S[i]-'0';
		}
		printf("Case #%d: %d\n", t, w);
	}
	return 0;
}
