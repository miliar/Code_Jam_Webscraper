/*
 * Author    : ben
 */
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <functional>
#include <numeric>
#include <cctype>
using namespace std;
const int MAXN = 1009;
double xs[MAXN], ys[MAXN];
int N;

int work1() {
	sort(xs, xs + N);
	sort(ys, ys + N);
	int ret = 0, s = 0;
	for(int i = 0; i < N; i++) {
		if(xs[i] > ys[s]) {
			ret++;
			s++;
		}
	}
	return ret;
}

int work2() {
	sort(xs, xs + N, greater<double>());
	sort(ys, ys + N, greater<double>());
	int s = 0, ret = 0;
	for(int i = 0; i < N; i++) {
		if(xs[i] > ys[s]) {
			ret++;
		} else {
			s++;
		}
	}
	return ret;
}

int main() {
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++) {
		scanf("%d", &N);
		for(int i = 0; i < N; i++) {
			scanf("%lf", &xs[i]);
		}
		for(int i = 0; i < N; i++) {
			scanf("%lf", &ys[i]);
		}
		printf("Case #%d: %d %d\n", t, work1(), work2());
	}
	return 0;
}

