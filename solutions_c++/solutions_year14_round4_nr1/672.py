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
		int n, x;
		int a[200000];
		cin >> n >> x;
		for (int i = 0; i < n; i++)
			cin >> a[i];
		sort(a, a+n);
		int ans = 0;
		int j = -1;
		for (int i = n - 1; i >= 0; i--){
			if (i == j) break;
			if (j + 1 == i) {
				ans++;
				break;
			}
			if (a[j+1] + a[i] <= x){
				j++;
			}
			ans++;
		}
		cout << ans;
		cout << endl;
	}
	return 0;
}
