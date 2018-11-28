#include <bits/stdc++.h>
using namespace std;

long double eps = 1e-9;

int n;
long long V,X;
long long R[1000],C[1000];

long long read(){
	string s; cin >> s;
	long long ret = 0;
	for (int i=0; i<(int)s.size(); i++) if (s[i] != '.')
		ret = ret * 10 + s[i]-'0';
	return ret;
}

void main2(){
	cin >> n;
	V = read();
	X = read();
	for (int i=0; i<n; i++){
		R[i] = read();
		C[i] = read();
	}
	long long minC = *min_element(C, C+n);
	long long maxC = *max_element(C, C+n);
	if (maxC<X || minC>X){
		cout << "IMPOSSIBLE" << endl;
		return;
	}
	for (int i=0; i<n; i++)
		for (int j=i+1; j<n; j++) if (C[j] < C[i]){
			swap(C[i],C[j]);
			swap(R[i],R[j]);
		}
	long double lo = 0.0, hi = 1e9;
	for (int rep=0; rep<=400; rep++){
		long double mid = (lo + hi) / 2;
		long double rem = V;
		long double mini= 0.0;
		for (int i=0; i<n; i++){
			long double t = min(R[i]*mid, rem);
			mini+= t * C[i];
			rem -= t;
		}
		rem = V;
		long double maxi = 0.0;
		for (int i=n-1; i>=0; i--){
			long double t = min(R[i]*mid, rem);
			maxi+= t * C[i];
			rem -= t;
		}
		if (mini-eps<=V*X && V*X<=maxi+eps && abs(rem)<=eps)
			hi = mid;
		else
			lo = mid;
	}
	cout << fixed << setprecision(10) << lo << endl;
}

int main(){
	int tt; cin >> tt;
	for (int o=1; o<=tt; o++){
		cout << "Case #" << o << ": ";
		main2();
	}
	return 0;
}
