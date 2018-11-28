#pragma comment(linker, "/STACK:128777216")

#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>
#include <algorithm>
#include <vector>
#include <deque>
#include <string>
#include <map>
#include <set>
#include <iostream>
#include <functional>
#include <numeric>
#include <sstream>
#include <exception>
#include <cassert>
#include <windows.h>

typedef long long i64;
typedef unsigned int u32;
const int null = 0;

using namespace std;

template<class T> int size(const T &a) {
	return int(a.size());
}
template<class T> T abs(const T &a) {
	return (a < 0? -a: a);
}
template<class T> T sqr(const T &a) {
	return a * a;
}

#define all(a) a.begin(),a.end()

struct MyThread {
	HANDLE thread;
	DWORD threadId;
	void create() {
		thread = CreateThread(NULL, 0, _solve, (void*)this, 0, &threadId);
	}
	DWORD WINAPI solve() {
		printf("%d\n", threadId);
		return 0L;
	}

	static DWORD WINAPI _solve(void* thread) {
		return ((MyThread*)thread)->solve();
	}
	void wait() {
		WaitForSingleObject(thread, INFINITE);
	}
};

const int max_n = 1000;

i64 a[37];

int main() {
#ifdef pperm
	freopen("input.txt", "r", stdin);
	//freopen("input.txt", "w", stdout);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	scanf("%d", &T);
	for (int iTest = 1; iTest <= T; iTest++) {
		i64 b;
		int n = 37;
		int f;
		memset(a, 0, sizeof(a));
		scanf("%lld %d", &b, &f);
		for (int i = 0; i < f; i++) {
			scanf("%lld", &a[i]);
		}
		sort(a, a + n);
		i64 sum = 0;
		double res = 0, res2 = 0;
		for (int i = 0; i < n; i++) {
			sum += a[i];
			int m = i + 1;
			i64 mn = a[i] * m - sum;
			if (mn > b) {
				break;
			}
			i64 mx = (i + 1 < n? (a[i + 1] - 1 - a[i]) * m + mn : b);
			mx = min(mx, b);
			mx = (mx - mn)/ m * m + mn;
			if (mx >= mn && mx > 0) {
				res = max(res, 36.0 / m * mx - mx);
				res = max(res, 36.0 / m * mn - mn);
			}
			i64 sum2 = 0;
			for (int j = i + 1; j < n; j++) {
				sum2 += a[j];
				if (j + 1 < n && a[j + 1] == a[j]) {
					continue;
				}
				i64 mxh = (j + 1 < n? a[j + 1] - 1 : b);
				int m2 = j - i;
				if (m + m2 >= 36) {
					break;
				}
				i64 h = min((b + sum + sum2 - m2) / (m + m2), mxh);
				if (h < a[j]) {
					break;
				}
				double cur = 36.0 / m * (h * m - sum) - (h * (m + m2) + m2 - sum - sum2);
				res2 = max(res2, cur);
			}
		}
		if (res2 > res) {
			res = res2;
		}
		printf("Case #%d: %.12lf\n", iTest, res);
	}
#ifdef pperm
	fprintf(stderr, "\n%.3lf\n", clock() / double(CLOCKS_PER_SEC));
#endif
	return 0;
}