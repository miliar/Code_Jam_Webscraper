#include <iostream>
#include <cstdio>
#include <set>

using namespace std;

int a[11000];

void work() {
	multiset<int> st;
	int n, k;
	cin >> n >> k;
	for (int i = 0; i < n; i++) {
		cin >> a[i];
		st.insert(a[i]);
	}
	int ans = 0;
	while (!st.empty()) {
		multiset<int>::iterator it = st.begin();
		int c = *it;
		st.erase(it);
		ans++;
		multiset<int>::iterator it2 = st.upper_bound(k - c);
		if (it2 == st.begin())
			continue;
		it2--;
		st.erase(it2);
	}
	cout << ans << endl;
}

int main() {
	freopen("G:/1.in", "r", stdin);
	freopen("G:/1.out", "w", stdout);

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		work();
	}
}
