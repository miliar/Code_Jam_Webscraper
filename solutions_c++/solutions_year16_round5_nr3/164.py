#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>

using namespace std;

const int N = 2e5 + 6;
const double INF = 1e100;

double sqr(double x) {
	return x * x;
}

struct Node {
	double x, y, z;
	Node(double x, double y, double z) : x(x), y(y), z(z) {

	}
	double dist(const Node &o) {
		return sqrt(sqr(o.x - x) + sqr(o.y - y) + sqr(o.z - z));
	}
};

int n;
int s;
double f[N];

int main() {
	int tests;
	scanf("%d", &tests);
	while (tests--) {
		scanf("%d %d", &n, &s);
		vector<Node> points;
		for (int i = 0; i < n; i++) {
			double x, y, z;
			scanf("%lf %lf %lf", &x, &y, &z);
			points.push_back(Node(x, y, z));
			scanf("%lf %lf %lf", &x, &y, &z);
		}
		static int visit[N];
		fill(visit, visit + n, 0);
		fill(f, f + n, INF);
		visit[0] = 0;
		f[0] = 0;
		for (int i = 0; i < n; i++) {
			int p = -1;
			for (int j = 0; j < n; j++) {
				if (!visit[j] && (p == -1 || f[j] < f[p])) {
					p = j;
				}
			}
			visit[p] = 1;
			for (int j = 0; j < n; j++) {
				if (!visit[j]) {
					f[j] = min(f[j], max(f[p], points[p].dist(points[j])));
				}
			}
		}

		static int testCount = 0;
		printf("Case #%d: %.8f\n", ++testCount, f[1]);
	}
	return 0;
}
