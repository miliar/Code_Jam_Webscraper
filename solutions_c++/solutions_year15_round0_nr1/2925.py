#include <cstdio>
#include <algorithm>

using namespace std;

typedef long long ll;

inline ll get_int() {
	ll p = 0;
	char c = getchar();
	while (c < '0' || c > '9') c = getchar();
	while ('0' <= c && c <= '9') p = p * 10 + (c - '0'), c = getchar();
	return p;
}

int T, smax;
int a[1020];

bool check(int x) {
	int temp = x;
	for (int i = 0; i <= smax; ++ i) {
		if (temp < i) return false;
		temp += a[i];
	}
	return true;
}

int main() {
	T = get_int();
	for (int t = 1; t <= T; ++ t) {
		smax = get_int();
		for (int i = 0; i <= smax; ++ i) {
			char c = getchar();
			a[i] = (c - '0');
		}
		int l = -1, r = 10000;
		while (l + 1 < r) {
			int mid = (l + r) >> 1;
			if (check(mid)) r = mid;
			else l = mid;
		}
		printf("Case #%d: %d\n", t, r);
	}
	return 0;
}

