#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int solve() {
	double result;
	int n;
	double v,x;

	stack<pair<double,double>> l,m;

	double speed = 0;

	cin >> n >> v >> x;
	for(int i=0; i < n; i++) {
		pair<double,double> p;
		cin >> p.first >> p.second;
		if(p.second == x) speed += p.first;
		if(p.second < x) l.push(p);
		if(p.second > x) m.push(p);
	}
	//cerr << speed << " " << m.size() << l.size() << endl;
	if(speed == 0 && (m.size() == 0 || l.size() == 0)) {
		cout << "IMPOSSIBLE" << endl;
		return 0;
	}
	// 2 30.0000 65.4321
	// 0.0001 50.0000
	// 100.0000 99.9000
	
	while(!l.empty() && !m.empty()) {
		auto a = l.top(); l.pop();
		auto b = m.top(); m.pop();

		double v0 = a.first, x0 = a.second, v1 = b.first, x1 = b.second;
		double temp = (v0 * x0 + v1 * x1) / (v0 + v1);
		//cerr << setprecision(9) << temp << endl;
		if(temp > x) {
			double del = x - x1;
			double xx = (v0*x0-x*v0)/del;
			m.push(make_pair(v1-xx,x1));
			speed += xx + v0;
		}
		if(temp < x) {
			double del = x - x0;
			double xx = (v1*x1-x*v1)/del;
			l.push(make_pair(v0-xx, x0));
			speed += xx + v1;
		}
		if(temp == x) {
			speed += v0 + v1;
		}

	}
	cout << fixed;

	cout << setprecision(9) << v/speed << endl;
}

int main(void) {
	ios::sync_with_stdio(false);
	cout << fixed << setprecision(9);

	int T;
	cin >> T;
	for(int t=1; t <= T; t++) {
		cout << "Case #"<< t << ": "; 
		solve();
	}
	return 0;
}