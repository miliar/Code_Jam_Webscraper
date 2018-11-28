#include <bits/stdc++.h>
using namespace std;

const int N = 200;

void single_test() {
	int n, k;
	cin >> n >> k;
	vector<double> p(n);
	for(int i=0; i<n; ++i) {
		cin >> p[i];
	}
	int m = (1<<n);
	double res = -1.0;
	for(int i=0; i<m; ++i) {
		int cnt = 0;
		for(int j=0; j<n; ++j) if(i & (1<<j)) ++cnt;
		if(cnt!=k) continue;
		double proba[N+1] = {0};
		proba[0] = 1.0;
		for(int j=0; j<n; ++j) {
			if(i & (1<<j)) {
				double tmp[N+1] = {0};
				for(int a=0; a<N; ++a) {
					tmp[a+1] += proba[a] * p[j];
					tmp[a] += proba[a] * (1.0 - p[j]); 
				}
				memcpy(proba, tmp, sizeof(proba));
			}
		}
		res = max(res, proba[k/2]);
	}
	cout << res << endl;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.precision(10);
	cout << fixed;
	int t;
	cin >> t;
	for(int i=1; i<=t; ++i) {
		cout << "Case #" << i << ": ";
		single_test();
	}
	return 0;
}
