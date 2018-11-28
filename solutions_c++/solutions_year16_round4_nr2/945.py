#include <vector>
#include <stdio.h>
#include <string>
#include <iostream>
#define forn(i, n) for(int i = 0; i < (int)n; i++)
using namespace std;
typedef long double ld;
void mul(vector<ld> &v, ld p, ld q){
	vector<ld> vv(v.size() + 1, 0);
	for(int i = 0; i < (int)v.size(); i++){
		vv[i + 1] += v[i] * p;
		vv[i] += v[i] * q;
	}
	swap(vv, v);
}
ld ans;
int n, k;
vector<ld> p, q;
void re(int i, int w, vector<ld>& v){
	if(i == n){
		if(w != 0)return;
		//cerr << v.size() << endl;
		ans = max(ans, v[k / 2]);
		return;
	}
	vector<ld> vv(v);
	mul(vv, p[i], q[i]);
	re(i + 1, w - 1, vv);
	re(i + 1, w, v);
	
}
void solve(){
	ans = 0;
	cin >> n >> k;
	p.clear(), q.clear();
	p.resize(n), q.resize(n);
	forn(i, n)
		cin >> p[i];
	forn(i, n)
		q[i] = 1 - p[i];
	vector<ld> v;
	v.push_back(1);
	re(0, k, v);
	cout << ans << endl;
}
int main(){
	cout.precision(10);
	cout << fixed;
	int t;
	cin >> t;
	for(int i = 0; i < t; i++){
		cout << "Case #" << i + 1<< ": ";
		solve();
	}
	return 0;
}
