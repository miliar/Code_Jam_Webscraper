#include <bits/stdc++.h>

using namespace std;

typedef long long int lint;

lint t;

struct jamcoin {
	lint len;
	lint t[100];
	lint divs[11];
	jamcoin(lint _len, lint n) {
		len = _len;
		for (lint i = 0; i < 17; i++) {
			t[i] = (n&(1LL<<i)) > 0;
		}
	}
	lint translate(lint base) {
		lint pot = 1;
		lint ret = 0;
		for (lint i = 0; i < 17; i++) {
			ret = ret + pot * t[i];
			pot *= base;
		}
		return ret;
	}
	lint finddiv(lint n) {
		for (lint i = 2; i * i <= n; i++) {
			if (n%i == 0) return i;
		}
		return -1;
	}
	bool verify() {
		if (t[0] == 0 || t[len-1] == 0) return false;
		for (lint i = 2; i <= 10; i++) {
			divs[i] = finddiv(translate(i));
			if (divs[i] == -1) return false;
		}
		return true;
	}
	void print() {
		for (lint i = len-1; i >= 0; i--) printf("%lld", t[i]);
		printf(" ");
		for (lint i = 2; i <= 10; i++) printf("%lld ", divs[i]);
		printf("\n");
	}
};

void solve(lint n, lint j) {
	lint w = 0;
	for (lint i = 0; w < j; i++) {
		jamcoin j(n, i);
		if (j.verify()) {
			w++;
			j.print();
		}
	}
}

int main() {
	scanf("%lld", &t);
	for (lint i = 1; i <= t; i++) {
		lint n, j;
		scanf("%lld%lld", &n, &j);
		printf("Case #%lld:\n", i);
		solve(n, j);
	}
	return 0;
}