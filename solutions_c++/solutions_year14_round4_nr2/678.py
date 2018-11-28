#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>

using namespace std;
int casenum,T;

int main() {
	freopen("gcj14.in","r",stdin);
	freopen("gcj14.out","w",stdout);
	cin >> T;
	for (casenum = 1; casenum <= T; casenum++) {
		cout << "Case #" << casenum << ": ";
		int n;
		int a[2000];
		int f1[2000];
		int f2[2000];
		cin >> n;
		for (int i = 1; i <= n; i++) {
			cin >> a[i];
		}
		int l = 1;
		int r = n;
		int ans = 0;
		while (l < r) {
			int minn = 1<< 30;
			int p;
			for (int i = l; i <= r; i++) {
				if (a[i] < minn) {
					minn = a[i];
					p = i;
				}
			}
			if (p - l < r - p) {
				ans += p - l;
				for (int i = p; i > l; i--)
					a[i] = a[i-1];
				a[l] = minn;
				l++;
			}
			else {
				ans += r - p;
				for (int i = p; i < r; i++)
					a[i] = a[i+1];
				a[r] = minn;
				r--;
			}
		}
		cout << ans;
		cout << endl;
	}
	return 0;
}
