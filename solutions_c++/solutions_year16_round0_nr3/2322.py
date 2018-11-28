#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>

using namespace std;
typedef long long ll;
const int N = 100000;
int v[N + 10];
ll ans[100];


ll tran(int x, int k) {
	ll res = 0;
	ll p = 1;
	for (int i = 0; i < 16; i++) {
		if (x & (1<<i))
			res += p;
		p *= k;
	}
	return res;
}

ll cal(ll x) {
	for (ll i = 2; i * i <= x; i++)
		if (x % i == 0)
			return i;
	return 0;
}

void output(int x) {
	for (int i = 15; i >= 0; i--) {
		if (x & (1 << i))
			printf("1");
		else
			printf("0");
	}
}

int main() {
	printf("Case #1:\n");
	int num = 0;
	for (int i = 0; i < (1<<16); i++) {
		if ((i & 1) == 0) continue;
		if ((i & (1 << 15)) == 0) continue;
		bool flag = true;
		for (int j = 2; j <= 10; j++) {
			ll x = tran(i, j);
			ll p = cal(x);
			if (p == 0) {
				flag = false;
				break;
			} else {
				ans[j]= p;
			}
		}
		if (flag) {
			output(i);
			for (int i = 2; i <= 10; i++)
				printf(" %lld", ans[i]);
			printf("\n");
			num ++;
		}
		if (num == 50) break;
	}
}