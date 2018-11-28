#include <bits/stdc++.h>

#define itn itn
#define all(x) (x).begin(), (x).end()

using namespace std;

inline int nxt(){
	int x;
	scanf("%d", &x);
	return x;
}

const double eps = 1e-8;

void solve(){
	int n = nxt();
	double v, x;
	cin >> v >> x;
	cout << setprecision(10) << fixed;
	if (n == 1){
		double r, c;
		cin >> r >> c;
		if (fabs(x - c) < eps)
			cout << v / r << "\n";
		else
			cout << "IMPOSSIBLE\n";
	} else {
		vector<double> r(n), c(n);
		for (int i = 0; i < n; i++)
			cin >> r[i] >> c[i];
		if (c[1] < c[0]){
			swap(r[1], r[0]);
			swap(c[1], c[0]);
		}
		if (c[1] < x - eps || c[0] > x + eps){
			cout << "IMPOSSIBLE\n";
		} else {
			if (fabs(c[1] - c[0]) < eps){
				cout << v / (r[0] + r[1]) << "\n";
			} else {
				double a = x - c[0], b = c[1] - x;
				swap(a, b);
				double tt = v / (a + b);
				a *= tt;
				b *= tt;
				cout << max(a / r[0], b / r[1]) << "\n";
			}
		}
	}
}

int main(){

	int T = nxt();
	for (int _ = 0; _ < T; _++){
		printf("Case #%d: ", _ + 1);
		solve();
		cerr << "Test #" << _ + 1 << " completed\n";
	}

	return 0;
}