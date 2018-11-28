#include <bits/stdc++.h>
typedef long long LL;
using namespace std;
#define ALL(x) (x.begin(), x.end())
#define rep(i,n) for(int i = 0;i < n;i ++)

const int inf = 1e9;

int main() {
//	freopen("out.txt", "w", stdout);
	ios :: sync_with_stdio(false);
	cout << fixed << setprecision(16);
	int T, K, C, S;
	cin >> T;
	rep(cas, T) {
		cin >> K >> C >> S;
		cout << "Case #" << cas + 1 << ": ";
		rep(i, K) {
			cout << i + 1;
			if (i == K - 1) {
				cout << endl;
			} else {
				cout << " ";
			}
		}
	}
	return 0;
}

