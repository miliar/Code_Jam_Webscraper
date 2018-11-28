#include <bits/stdc++.h>
using namespace std;

int TC, N, S, x[1005], y[1005], z[1005], par[1005];
vector< pair<int, pair<int, int> > > v;



int p(int x1) {
	if (par[x1] == x1) return x1;
	else return par[x1] = p(par[x1]);
}

void merge(int X, int Y) {
	X = p(X);
	Y = p(Y);
	par[X] = Y;
}

int main() {
	scanf("%d", &TC);
	for (int tc = 1; tc <= TC; tc++) {
		scanf("%d%d", &N, &S);
		for (int i = 0; i < N; i++) par[i] = i;
		int tmp;
		v.clear();
		for (int i = 0; i < N; i++) scanf("%d%d%d%d%d%d", &x[i], &y[i], &z[i], &tmp, &tmp, &tmp);
		for (int i = 0; i < N; i++) {
			for (int j = i + 1; j < N; j++) {
				int dx = x[i] - x[j];
				int dy = y[i] - y[j];
				int dz = z[i] - z[j];
				v.push_back(make_pair(dx * dx + dy * dy + dz * dz, make_pair(i, j)));
			}
		}
		sort(v.begin(), v.end());
		for (int i = 0; i < v.size(); i++) {
			if (p(v[i].second.first) != p(v[i].second.second)) {
				merge(v[i].second.first, v[i].second.second);
			}
			if (p(0) == p(1)) {
				printf("Case #%d: %.10lf\n", tc, sqrt(v[i].first));
				break;
			}
		}
	}
}
