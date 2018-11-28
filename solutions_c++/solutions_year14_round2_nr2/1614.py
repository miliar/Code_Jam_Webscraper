#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <utility>
using namespace std;

#define rep(i,n) for(int i=0; i<n; i++)
typedef long long ll;

void init() {
    cin.tie(0);
    ios::sync_with_stdio(false);
}

int main() {
    init();
	int t;
	cin >> t;
	rep(tt, t) {
		unsigned int a, b, k;
		int cnt = 0;
		cin >> a >> b >> k;
		rep(da, a) {
			rep(db, b) {
				unsigned int x = da & db;
				if( x < k ) cnt++;
			}
		}
		cout << "Case #" << (tt+1) << ": ";
		cout << cnt << endl;
	}
	return 0;
}
