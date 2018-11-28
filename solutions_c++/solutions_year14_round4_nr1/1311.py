#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int T;
	cin>>T;
	for (int t = 1; t <= T; ++t) {
		int n, m;
		cin>>n>>m;
		int a[10005];
		for (int i = 0; i < n; ++i) {
			cin>>a[i];
		}
		sort(a, a+n);
		int i, j = 0, ans = 0;
		for ( i = n-1; i > j; --i) {
			if (a[i]+a[j] > m) {
				++ans;
			}
			else {
				++ans;
				++j;
			}
		}
		if (i == j) {
			++ans;
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
}