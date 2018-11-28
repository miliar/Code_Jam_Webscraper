#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <utility>
#include <cstring>
using namespace std;

#define rep(i,n) for(int i=0; i<n; i++)
typedef long long ll;

int main() {
	int t;
	cin >> t;
	for(int dt=1; dt<=t; dt++) {
		int d;
		cin >> d;
		vector<int> p(d);
		int mx = 0;
		rep(i, d) {
			cin >> p[i];
			mx = max(mx, p[i]);
		}
		int res = mx;
		for(int top=1; top<=mx; top++) {
			int cnt = 0;
			rep(i, d) {
				cnt += (p[i]+top-1) / top - 1;
			}
			res = min(res, top+cnt);
		}
		cout << "Case #" << dt << ": " << res << endl;
	}
	return 0;
}
