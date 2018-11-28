#include <bits/stdc++.h>

using namespace std;

#ifdef LOCAL
#include "delete_this.hpp"
#define t(...) debug(#__VA_ARGS__, __VA_ARGS__);
#else
#define t(...)
#endif

int ada[10];
int ans[1000000 + 10];

void hoho(long long a) {
	while (a > 0) {
		ada[a % 10] = 1;
		a /= 10;
	}
}

bool semua() {
	for (int i = 0; i <= 9; ++i) {
		if (!ada[i]) {
			return false;
		}
	}
	return true;
}

void jwb(long long k) {
	memset(ada, 0, sizeof(ada));
	int kali = 1;
	while (1) {
		hoho(k * kali);
		if (semua()) {
			cout << (k * kali) << "\n";
			return;
		}
		kali++;
	}
}


int main() {
	int ntc;
	scanf("%d", &ntc);
	for (int itc = 0; itc <= ntc - 1; ++itc) {
		printf("Case #%d: ", itc + 1);
		int n;
		scanf("%d", &n);
		if (n == 0) {
			puts("INSOMNIA");
			continue;
		}
		jwb(n);
	}
	return 0;
}