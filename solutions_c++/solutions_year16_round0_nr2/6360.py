#include <bits/stdc++.h>

using namespace std;

#ifdef LOCAL
#include "delete_this.hpp"
#define t(...) debug(#__VA_ARGS__, __VA_ARGS__);
#else
#define t(...)
#endif

int a[100 + 10];


void hue() {
	string s;
	cin >> s;
	int sz = s.size();
	memset(a, 0, sizeof(a));
	for (int i = 0; i <= sz - 1; ++i) {
		a[i] = (s[i] == '+') ? 1 : 0;
	}
	int ans = 0;
	bool semua = true;
	for (int i = sz - 1; i >= 0; --i) {
		if (a[i] == 0) {
			semua = false;
			break;
		}
	}
	while (!semua) {
		int frst = -1;
		for (int i = sz - 1; i >= 0; --i) {
			if (a[i] == 0) {
				frst = i;
				break;
			}
		}
		for (int i = frst; i >= 0; --i) {
			a[i] = (a[i] == 1) ? 0 : 1;
		}
		semua = true;
		for (int i = sz - 1; i >= 0; --i) {
			if (a[i] == 0) {
				semua = false;
				break;
			}
		}
		ans++;
	}
	assert(ans <= 100);
	cout << ans << "\n";
}

int main() {
	int ntc;
	scanf("%d", &ntc);
	for (int itc = 0; itc <= ntc - 1; ++itc) {
		printf("Case #%d: ", itc + 1);
		hue();
	}
	return 0;
}
