#include <bits/stdc++.h>
using namespace std;

#define oo 1LL<<30
#define SZ(x) ((int)x.size())
#define valid(x,u) (x>=0 && x<u)
#define endl '\n'

int di [] = {0, 0, 1, -1, 1, 1, -1, -1};
int dj [] = {1, -1, 0, 0, 1, -1, 1, -1};

double C, F, X;

double fu() {
	double ret = X / 2.0, z = 2.0, curTime = 0.0;
	while(true) {
		curTime += (C / z); z += F;
		if(curTime + X / z > ret) break;
		ret = curTime + X / z;
	}
	return ret;
};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout << fixed << setprecision(9);

	freopen("in.in", "rt", stdin);
	freopen("out.out", "wt", stdout);

	int T, id = 0; cin >> T;
	while(T --) {
		cin >> C >> F >> X;
		double ans;
		if(C >= X) ans = X / 2.0;
		else ans = fu();
		cout << "Case #" << ++id << ": " << ans << endl;
	}

	return 0;
}
