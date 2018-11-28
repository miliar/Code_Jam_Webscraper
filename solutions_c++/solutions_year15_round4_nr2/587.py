#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define EPS (00)
typedef pair< pair<int, int> , pair<double, double> > state;
#define mp make_pair
int N, T;
double V, Xf, R[150], Cf, used[150];
ll X, C[150];
vector<state> v;
bool cmp (state a, state b) {
	return a.second.first + a.second.second > b.second.first + b.second.second;
}
bool check(double t) {
	double vol = 0.0;
	for (int i = 0; i < N; ++i) used[i] = 0.0;
	for (auto it = v.begin(); it != v.end(); ++it) {
		int x = it->first.first, y = it->first.second;
		double tl = t - max(used[x], used[y]);
		if (tl < EPS) continue;
		vol += tl*(it->second.first + it->second.second);
		used[x] += tl*it->second.first/R[x];
		used[y] += tl*it->second.second/R[y];
		if (vol > V - EPS) return true;
	}
	return false;
}
int main() {
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	scanf("%d", &T);
	for (int TC = 1; TC <= T; ++TC) {
		scanf("%d", &N);
		scanf("%lf%lf", &V, &Xf);
		X = round(Xf*10000);
		for (int i = 0; i < N; ++i) {
			scanf("%lf%lf", &R[i], &Cf);
			C[i] = round(Cf*10000) - X;
			if (C[i] == 0) v.push_back(mp(mp(i, i), mp(R[i]/2.0, R[i]/2.0)));
			else {
				for (int j = 0; j < i; ++j) {
					if ( (C[i] < 0) != (C[j] < 0) ) {
						if ( R[i]*abs(C[i]) < R[j]*abs(C[j]) ) {
							double r = (double) R[i]*(double) abs(C[i])/(double) abs(C[j]);
							v.push_back(mp(mp(i, j), mp(R[i], r)));
						}
						else {
							double r = (double) R[j]*(double) abs(C[j])/(double) abs(C[i]);
							v.push_back(mp(mp(i, j), mp(r, R[j])));
						}
					}
				}
			}
		}
		
		printf("Case #%d: ", TC);
		if (v.empty()) {
			puts("IMPOSSIBLE");
			continue;
		}
		sort(v.begin(), v.end(), cmp);
		double s = 0, e = 10e50, m;
		while (m = (s+e)/2, e-s > 10e-7) {
			if (check(m)) e = m;
			else s = m;
		}
		printf("%.8lf\n", e);
		v.clear();
	}
}
