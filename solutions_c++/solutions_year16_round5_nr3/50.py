#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<string>
#include <vector>
#include <cmath>
using namespace std;

struct UF {
	vector<int> fa;
	void init(int n) {
		fa.assign(n, 0);
		for (int i = 0; i < n; ++i) {
			fa[i] = i;
		}
	}

	int find(int x) {
		if (fa[x] == x)
			return x;
		return fa[x] = find(fa[x]);
	}

	bool unite(int a, int b) {
		a = find(a), b = find(b);
		if (a == b)
			return false;
		fa[a] = b;
		return true;
	}
};

int main() {
	int T;
	cin >> T;
	for (int nc = 1; nc <= T; ++nc) {
		int N, S;
		cin >> N >> S;
		double ans = 0;

		UF U;
		U.init(N);

		vector<pair<double, pair<int, int> > > edges;

		vector<int> x(N), y(N), z(N);

		for (int i = 0; i < N; ++i) {
			cin >> x[i] >> y[i] >> z[i];
			int vx, vy, vz;
			cin >> vx >> vy >> vz;
		}

		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < i; ++j) {
				double dx = x[i] - x[j];
				double dy = y[i] - y[j];
				double dz = z[i] - z[j];
				double len = sqrt(dx * dx + dy * dy + dz * dz);
				edges.push_back(make_pair(len, make_pair(i, j)));
			}
		}

		sort(edges.begin(), edges.end());

		for (int i = 0; i < edges.size(); ++i) {
			int a = edges[i].second.first, b = edges[i].second.second;
			U.unite(a, b);
			if (U.find(0) == U.find(1)) {
				ans = edges[i].first;
				break;
			}
		}

		printf("Case #%d: %0.9lf\n", nc, ans);
	}
	return 0;
}
