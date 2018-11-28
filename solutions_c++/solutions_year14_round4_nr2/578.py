#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;

const int N(1010);

int ca, n;
int a[N];

int main() {
	freopen("in.txt", "r", stdin);
	cin >> ca;
	for (int c = 1; c <= ca; ++c) {
		cin >> n;
		for (int i = 0; i != n; ++i)
			cin >> a[i];
		int ans = 0;
		for (int i = 0; i != n; ++i) {
			int left = 0, right = 0;
			for (int j = 0; j != i; ++j)
				if (a[j] > a[i]) ++left;
			for (int j = i + 1; j != n; ++j)
				if (a[j] > a[i]) ++right;
			ans += min(left, right);
		}
		cout << "Case #" << c << ": " << ans << endl;
	}
	return 0;
}