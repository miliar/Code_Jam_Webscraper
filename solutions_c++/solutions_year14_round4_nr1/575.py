#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;

const int N(10010);

int ca, n, x;
int a[N];

int main() {
	freopen("in.txt", "r", stdin);
	cin >> ca;
	for (int c = 1; c <= ca; ++c) {
		cin >> n >> x;
		for (int i = 0; i != n; ++i)
			cin >> a[i];
		sort(a, a + n);
		int i = n - 1, j = 0, ans = 0;
		for (; i > j; --i) {
			if (a[i] + a[j] <= x) ++j;
			++ans;
		}
		if (i == j) ++ans;
		cout << "Case #" << c << ": " << ans << endl;
	}
	return 0;
}