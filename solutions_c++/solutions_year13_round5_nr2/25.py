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

const int max_n = 1010;

struct Point {
	int x, y;
	int id;
	void scan(int id) {
		this->id = id;
		scanf("%d %d", &x, &y);
		x *= 2;
		y *= 2;
	}
	void operator += (const Point &p) {
		x += p.x;
		y += p.y;
	}
	void operator -= (const Point &p) {
		x -= p.x;
		y -= p.y;
	}
	i64 operator * (const Point &p) const {
		return x * p.y - y * p.x;
	}
	bool isq12() const {
		return y > 0 || y >= 0 && x > 0;
	}
	i64 len2() const {
		return x * x + y * y;
	}
	bool operator < (const Point &p) const {
		if (isq12() != p.isq12()) {
			return isq12();
		}
		i64 val = (*this) * p;
		return val > 0 || val == 0 && len2() < p.len2();
	}
} p[max_n];

int r[max_n];

int main() {
#ifdef pperm
	freopen("input.txt", "r", stdin);
	//freopen("input.txt", "w", stdout);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	scanf("%d", &T);
	for (int iTest = 1; iTest <= T; iTest++) {
		int n;
		scanf("%d", &n);
		int sx = 0, sy = 0;
		for (int i = 0; i < n; i++) {
			p[i].scan(i);
			sx += p[i].x;
			sy += p[i].y;
		}
		sx /= n;
		sy /= n;
		i64 best = -1;
		for (int i = -50; i <= 50; i++) {
			for (int j = -50; j <= 50; j++) {
				Point c;
				c.x = sx + i;
				c.y = sy + j;
				bool bad = false;
				for (int i = 0; i < n; i++) {
					p[i] -= c;
					if (p[i].x == 0 && p[i].y == 0) {
						bad = true;
					}
				}
				if (!bad) {
					sort(p, p + n);
					i64 res = 0;
					for (int i = 0; i < n; i++) {
						res += p[i] * p[(i + 1) % n];
					}
					if (res < 0) res = -res;
					if (res > best) {
						best = res;
						for (int i = 0; i < n; i++) {
							r[i] = p[i].id;
						}
					}

				}
				for (int i = 0; i < n; i++) {
					p[i] += c;
				}
			}
		}
		printf("Case #%d:", iTest);
		for (int i = 0; i < n; i++) {
			printf(" %d", r[i]);
		}
		printf("\n");
	}
#ifdef pperm
	fprintf(stderr, "\n%.3lf\n", clock() / double(CLOCKS_PER_SEC));
#endif
	return 0;
}