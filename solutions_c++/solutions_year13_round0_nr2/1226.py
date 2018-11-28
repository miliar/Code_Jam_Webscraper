
#include <iostream>
using namespace std;

#define show(x) #x " = " << (x)
#define rep(i,n) for (int i = 0; i < int(n); ++i)

int a[100][100], u[100], v[100];
void setmax(int& x, int y) { if (x < y) x = y; }

void solve() {
	int N, M;
	cin >> N >> M;
	rep (i,N) rep (j,M) cin >> a[i][j];
	rep (i,N) {
		int max = 0;
		rep (j,M) setmax(max, a[i][j]);
		u[i] = max;
	}
	rep (j,M) {
		int max = 0;
		rep (i,N) setmax(max, a[i][j]);
		v[j] = max;
	}

	rep (i,N) rep (j,M) {
		if (a[i][j] != u[i] && a[i][j] != v[j]) {
			cout << "NO" << endl;
			return;
		}
	}
	cout << "YES" << endl;
}	

int main() {
	int T;
	cin >> T;
	rep (i,T) {
		cout << "Case #" << i+1 << ": ";
		solve();
	}
}
