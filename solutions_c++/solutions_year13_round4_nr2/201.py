#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair

typedef long long LL; 

LL N, P;

LL check(LL m) {
	LL t = 1LL << N;
	t = t - m;
	if (t == 0) return -1;
	LL ret = 0;
	for (int i = N - 1; i >= 0; i--) {
		if (t == 1) break;
		ret += (1LL << i);
		t /= 2;
	}
	return ret;
}

LL check2(LL m) {
	LL t = m + 1;
	LL ret = (1LL << N) - 1;
	for (int i = N - 1; i >= 0; i--) {
		if (t == 1) break;
		ret -= (1LL << i);
		t /= 2;
	}
	return ret;
}

int main() {
	int T;
	freopen("x.txt", "r", stdin); freopen("w.txt", "w", stdout);
	scanf("%d", &T);
	for (int re = 1; re <= T; re++) {
		scanf("%lld%lld", &N, &P);
		LL l = 0, r = (1LL << N);
		while (l + 1 < r) {
			LL mid = (l + r) / 2;
			if (check(mid) + P >= (1LL << N)) {
				l = mid;
			} else {
				r = mid;
			}
		}
		LL y = l;
		l = 0, r = (1LL << N);
		while (l + 1 < r) {
			LL mid = (l + r) / 2;
			if (check2(mid) + P >= (1LL << N)) {
				l = mid;
			} else {
				r = mid;
			}
		}
		LL x = l;
		printf("Case #%d: %lld %lld\n", re, x, y);
	}
}
