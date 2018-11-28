#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

const int N = 1e6;
const int CT = 16;

struct quat {
	int sign;
	int val;
	quat() {
		val = 0;
		sign = 1;
	}
	quat(int sign, int val) : sign(sign), val(val) {}

	quat operator *(quat const &u) {
		if (val * u.val == 0) return quat(sign * u.sign, val + u.val);
		if (val == u.val) return quat(-1 * u.sign * sign, 0);
		quat res(sign * u.sign, 6 - val - u.val);
		int nval = ((val == 3) ? 1 : (val + 1));
		if (u.val != nval) res.sign *= -1;
		return res;
	}	

	bool operator ==(quat const& u) const {
		return ((sign == u.sign) && (val == u.val));
	}

	bool operator !=(quat const& u) const {
		return !(*this == u);
	}
};

quat a[N];

quat pw(quat x, long long y) {
	quat res;
	while (y) {
		if (y % 2) res = res * x;
		x = x * x;
		y /= 2;
	}
	return res;
}

int main() {
	freopen("input.txt", "r", stdin);
	int ttt;
	scanf("%d\n", &ttt);
	for (int tt = 1; tt <= ttt; tt++) {
		printf("Case #%d: ", tt);
		int n;
		long long x;
		cin >> n >> x;
		long long l = x * n;
		string s;
		cin >> s;
		quat all;
		for (int i = 0; i < n; i++) {
			a[i].sign = 1;
			a[i].val = string("1ijk").find(s[i]);
			all = all * a[i];
		}
		all = pw(all, x);
		if (all != quat(-1, 0)) {
			puts("NO");
			continue;
		}
		long long fi = l + 1;
		long long lj = -1;
		quat cur;
		for (int i = 0; i < CT * n; i++) { 
			cur = cur * a[i % n];
			if (cur == quat(1, 1)) {
				fi = i;
				break;
			}
		}
		cur = quat(1, 0);
		reverse(a, a + n); 
		for (int i = 0; i < CT * n; i++) { 
			cur = a[i % n] * cur;
			if (cur == quat(1, 3)) {
				lj = l - i - 1;
				break;
			}
		}
		if ((fi < lj) && (fi >= 0) && (lj < l)) {
			puts("YES");
		} else {
			puts("NO");
		}
	}
}

