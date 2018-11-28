#include <bits/stdc++.h>
using namespace std;

double getP(vector<double> const& A, int k) {
	vector<double> O(k+1), N(k+1);
	O[0] = 1.0;

	for(auto p: A) {
		N[0] = O[0] * (1-p);
		for(int i=1; i<=k; i++) {
			N[i] = O[i-1] * p + O[i] * (1-p);
		}
		swap(O, N);
	}

	return O[k];
}

double brute(vector<double> const& A, int k) {
	int n = A.size();

	double res= 0.0;
	for(int i=0; i<(1<<n); i++) {
		if(__builtin_popcountl(i) != k) continue;
		vector<double> X;
		for(int j=0; j<n; j++) if(i & (1<<j)) X.push_back(A[j]);
		res = max(res, getP(X, k/2));
	}
	return res;
}

double model(vector<double> A, int k) {
	int n = A.size();

	double res = 0.0;
	sort(A.begin(), A.end());
	for(int i=0; i<=k; i++) {
		vector<double> X;
		for(int j=0; j<i; j++) X.push_back(A[j]);
		for(int j=n-k+i; j<n; j++) X.push_back(A[j]);

		res = max(res, getP(X, k/2));
	}

	return res;
}

double test () {
	int n, k;
	cin >> n >> k;
	vector<double> V;

	for(int i=0; i<n; i++) {
		double x;
		cin >> x;
		V.push_back(x);
	}

	double B = model(V, k);
#if 0
	double A = brute(V, k);
	if(abs(A - B) > 1e-6) {
		cout << A << endl; cout << B << endl;
		assert(false);
	}
#endif
	return B;
}

int main() {
	int t;
	cin >> t;
	cout << fixed << setprecision(10);
	for(int i=1; i<=t; i++) {
		double result = test();
		cout << "Case #" << i << ": " << result << endl;
	}
}
