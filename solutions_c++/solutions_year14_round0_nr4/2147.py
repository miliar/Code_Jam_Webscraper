#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <set>
using namespace std;

const int MAX_N = 1000 + 10;
double my[MAX_N], op[MAX_N];

int calc(double a[], double b[], int n) {
	set<double> st(a, a + n);
	int ans = 0;
	for (int i = 0; i < n; ++i) {
		if (st.lower_bound(b[i]) != st.end()) {
			st.erase(st.lower_bound(b[i]));
			++ans;
		} else {
			st.erase(st.begin());
		}
	}
	return ans;
}

int main() {
	int T;
	cin >> T;
	for (int nc = 1; nc <= T; ++nc) {
		printf("Case #%d: ", nc);
		int n;
		cin >> n;
		for (int i = 0; i < n; ++i) {
			cin >> my[i];
		}
		for (int i = 0; i < n; ++i) {
			cin >> op[i];
		}
		sort(my, my + n), sort(op, op + n);
		cout << calc(my, op, n) << " " << n - calc(op, my, n) << endl;
	}
}
