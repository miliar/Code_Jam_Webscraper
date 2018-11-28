#include <bits/stdc++.h>
using namespace std;

struct water {
	double r, c;
	water(double a=0, double b=0) {r=a; c=b;}
	bool operator<(const water &oth) const {return c<oth.c;}
};

const int MAXN = 105;
const double EPSILON = 1e-9;
int T, N;
double V, X;
vector<water> flow;

int main() {
	if(fopen("test.in","r")) {
		freopen("test.in", "r", stdin);
		freopen("test.out", "w", stdout);
	}
	cin >> T;
	for(int t=1; t<=T; ++t) {
		flow.clear();
		cin >> N >> V >> X;
		for(int i=0; i<N; ++i) {
			double r,c;
			cin >> r >> c;
			flow.push_back(water(r,c));
		}
		sort(flow.begin(), flow.end());
		auto mid = lower_bound(flow.begin(), flow.end(), water(0,X));
		double low=0, high=0;
		for(auto it=mid; it!=flow.end(); ++it) {
			high += it->r * (it->c - X);
		}
		for(auto it=reverse_iterator<vector<water>::iterator>(mid); it!=flow.rend(); ++it) {
			low += it->r * (X - it->c);
		}
		double rate = 0;
		if(high > low + EPSILON) {
			for(auto it=reverse_iterator<vector<water>::iterator>(mid); it!=flow.rend(); ++it)
				rate += it->r;
			double gather = 0;
			for(auto it=mid; it!=flow.end(); ++it) {
				if(abs(it->c - X) < EPSILON) {
					rate += it->r;
					continue;
				}
				double x = low - gather;
				x = min(x, it->r * (it->c - X));
				rate += x / (it->c - X);
				gather += x;
			}
		} else {
			for(auto it=mid; it!=flow.end(); ++it)
				rate += it->r;
			double gather = 0;
			for(auto it=reverse_iterator<vector<water>::iterator>(mid); it!=flow.rend(); ++it) {
				if(abs(it->c - X) < EPSILON) {
					rate += it->r;
					continue;
				}
				double x = high - gather;
				x = min(x, it->r * (X - it->c));
				rate += x / (X - it->c);
				gather += x;
			}
		}
		cout << "Case #" << t << ": ";
		if(rate > EPSILON) cout << setprecision(9) << V / rate << '\n';
		else cout << "IMPOSSIBLE\n";
	}
}
