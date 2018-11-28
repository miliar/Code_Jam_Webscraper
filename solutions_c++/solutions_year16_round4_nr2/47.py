#include <bits/stdc++.h>
using namespace std;

const int MAXN = 200+10;

double dp[MAXN], dp_temp[MAXN];

double go (vector<double> p){
	int n = (int)p.size();
	assert(n%2 == 0);
	for (int i=0; i<=n; i++)
		dp[i] = 0.0;
	dp[0] = 1.0;
	for (int i=0; i<n; i++){
		for (int j=0; j<=n; j++){
			dp_temp[j] = dp[j] * (1 - p[i]);
			if (j != 0)
				dp_temp[j]+= dp[j-1] * p[i];
		}
		for (int j=0; j<=n; j++)
			dp[j] = dp_temp[j];
	}
	return dp[n/2];
}

void main2(){
	int n,k; cin >> n >> k;
	vector<double> p(n);
	for (int i=0; i<n; i++)
		cin >> p[i];
	sort(p.begin(), p.end());
	double res = 0.0;
	for (int i=0; i<=k; i++){
		vector<double> pp;
		for (int j=0; j<i; j++)
			pp.push_back(p[j]);
		for (int j=n-(k-i); j<n; j++)
			pp.push_back(p[j]);
		res = max(res, go(pp));
	}
	cout << fixed << setprecision(8) << res << endl;
}

int main(){
	int t; cin >> t;
	for (int o=1; o<=t; o++){
		cout << "Case #" << o << ": ";
		main2();
	}
	return 0;
}
