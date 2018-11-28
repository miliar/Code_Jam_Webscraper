#include <iostream>
#include <set>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;
#define int long long
set <char> sss;
void doo(string s) {
	for (auto it : s) {
		sss.insert(it);
	}
}
signed main() {
#ifndef ONLINE_JUDGE
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int q;
	cin >> q;
	
	for (int qq = 1; qq <= q; ++qq) {
		sss.clear();
		int n;
		cin >> n;
		for (int i = 1; i <= 1e5; ++i) {
			doo(to_string(n * i));
			if (sss.size() == 10) {
				printf("Case #%I64d: %I64d\n", qq, n * i);
				goto ll;
			}
		}
		printf("Case #%d: INSOMNIA\n", qq);
	ll:;
	}
}