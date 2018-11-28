#include <iostream>
#include <algorithm>

using namespace std;

pair<int,int> a[1000];

void solve() {
	int n;
	cin >> n;
	for (int i=0; i<n; i++) {
		cin >> a[i].first;
		a[i].second = i;
	}
	sort(a, a+n);
	int front(0), back(n-1), total(0);
	for (int i=0; i<n; i++) {
		int fswap = a[i].second - front;
		int bswap = back - a[i].second;
		if (fswap <= bswap) {
			front++;
			for (int j=i+1; j<n; j++) {
				if (a[j].second < a[i].second) a[j].second++;
			}
			total += fswap;
		} else {
			back--;
			for (int j=i+1; j<n; j++) {
				if (a[j].second > a[i].second) a[j].second--;
			}
			total += bswap;
		}
	}
	cout << total;
}

int main() {
	int t;
	cin >> t;
	for (int cn=1; cn<=t; cn++) {
		cout << "Case #" << cn << ": ";
		solve();
		cout << "\n";
	}
	return 0;
}