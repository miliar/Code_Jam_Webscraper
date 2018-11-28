#include <bits/stdc++.h>
using namespace std;

#define fr(a,b,c) for (int a = b; a < c; ++a)

int go(vector<double> a, vector<double> b) {
	multiset<double> B(b.begin(), b.end());
	int pnt = 0;
	fr(i,0,a.size()) {
		double x = a[i];
		multiset<double>::iterator it = B.upper_bound(x);
		if (it == B.end()) {
			pnt++;
			B.erase(B.begin());
		} else B.erase(it);
	}
	return pnt;
}

int main() {
	int t, caso = 1;
	for (cin >> t; caso <= t; ++caso) {
		printf("Case #%d: ", caso);
		int n;
		cin >> n;
		vector<double> a(n), b(n);
		fr(i,0,n) cin >> a[i];
		fr(i,0,n) cin >> b[i];
		
		printf("%d %d\n", n-go(b,a), go(a,b));
	}
	return 0;
}
