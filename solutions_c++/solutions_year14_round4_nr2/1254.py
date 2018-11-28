/*
 * gcjb2/win.cpp
 * Created on: 2014-5-31
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
const int MAXN = 20;
int N;
int f[MAXN], g[MAXN];
bool visited[MAXN];

void input() {
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf("%d", &f[i]);
	}
}

int factorial(int a) {
	int ret = 1;
	for (int i = 1; i <= a; i++) {
		ret *= i;
	}
	return ret;
}

bool judge() {
	int i = 0;
	while (i + 1 < N && g[i + 1] > g[i]) {
		i++;
	}
	while (i + 1 < N && g[i + 1] < g[i]) {
		i++;
	}
	return i == (N - 1);
}

int cal() {
	int ret = 0;
	memset(visited, 0, sizeof(visited));
	for (int i = 0; i < N; i++) {
		int temp = 0;
		for (int j = 0; j < N; j++) {
			if (g[i] == f[j]) {
				visited[j] = true;
				break;
			}
			if (!visited[j]) {
				temp++;
			}
		}
		ret += temp;
	}
	return ret;
}

int work() {
	int round_num = factorial(N);
	int ret = N * N;
	memcpy(g, f, N * sizeof(int));
	for (int i = 0; i < round_num; i++) {
		if (judge()) {
			ret = min(ret, cal());
		}
		next_permutation(g, g + N);
	}
	return ret;
}

int main() {
//	freopen("data.in", "r", stdin);
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		input();
		printf("Case #%d: %d\n", t, work());
	}
	return 0;
}
