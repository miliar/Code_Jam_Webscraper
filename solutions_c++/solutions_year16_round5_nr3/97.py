#include<cstring>
#include<cstdio>
#include<vector>
#include<map>
#include<algorithm>
#include<cmath>
using namespace std;
double eps(1e-10);
double mid;
const int N(1011);
bool cmp(const pair<double, double> & a, const pair<double, double> & b) {
	return a.first + eps < b.first;
}
vector<pair<double, double> > itvs[N];;
pair<double, double> go[N][N];
vector<int> num[N];
struct Point {
	double x, y, z;
	Point() {
	}
	void scan() {
		scanf("%lf%lf%lf", &x, &y, &z);
	}
	double sqrlen() const {
		return x * x + y * y + z * z;
	}
	double len() const {
		return sqrt(max(0., sqrlen()));
	}
	Point(const double & x, const double & y, const double & z) : x(x), y(y), z(z) {
	}
};
int rela[N * N];
Point a[N], v[N];
__inline Point operator - (const Point & a, const Point & b) {
	return Point(a.x - b.x, a.y - b.y, a.z - b.z);
}
__inline Point operator * (const Point & a, const Point & b) {
	return Point(a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z, a.x * b.y - a.y * b.x);
}
__inline double operator % (const Point & a, const Point & b) {
	return a.x * b.x + a.y * b.y + a.z * b.z;
}
pair<double, double> calc(const Point & s, const Point & d) {
	if(d.len() < eps) {
		if((Point(0, 0, 0) - s).len() < mid + eps) {
			return make_pair(0, 1e9);
		}else {
			return make_pair(1e9, 0);
		}
	}
	double len((s * d).len() / d.len());
	if(len > mid + eps) {
		return make_pair(1e9, 0);
	}
	//dis(s + lambda * d, Point(0, 0, 0)) = mid;
	double A(d.sqrlen()), B(2 * (s % d)), C(s.sqrlen() - mid);
	if(B * B - 4 * A * C <= 0) {
		double t(-B / 2 / A);
		if(t >= 0) {
			return make_pair(t, t);
		}else {
			return make_pair(1e9, 0);
		}
	}
	double le((-B - sqrt(B * B - 4 * A * C)) / 2 / A);
	double ri((-B + sqrt(B * B - 4 * A * C)) / 2 / A);
	if(ri < 0) {
		return make_pair(1e9, 0.);
	}
	if(le < 0) {
		return make_pair(0., ri);
	}else {
		return make_pair(le, ri);
	}
}
int getr(int x) {
	int p(x), p1, p2;
	while(rela[p] != p) {
		p = rela[p];
	}
	p1 = p; p = x;
	while(rela[p] != p) {
		p2 = rela[p];
		rela[p] = p1;
		p = p2;
	}
	return p1;
}
int main() {
	int tests;
	scanf("%d", &tests);
	for(int qq(1); qq <= tests; qq++) {
		printf("Case #%d: ", qq);

		int n, s;
		scanf("%d%d", &n, &s);
		for(int i(0); i < n; i++) {
			a[i].scan();
			v[i].scan();
		}
		double le(0), ri(2000);
		for(int _(0); _ < 50; _++) {
			mid = (le + ri) / 2;
			for(int i(0); i < n; i++) {
				itvs[i].clear();
				num[i].clear();
				for(int j(0); j < n; j++) {
					go[i][j] = make_pair(1e9, 0);
				}
			}
			for(int i(0); i < n; i++) {
				for(int j(i + 1); j < n; j++) {
					if(i == j) {
						continue;
					}
					pair<double, double> itv(calc(a[j] - a[i], v[j] - v[i]));
					if(itv.first < itv.second + eps) {
						go[i][j] = go[j][i] = itv;
						//printf("%f %d %d %f %f\n", mid, i, j, itv.first, itv.second);
						itvs[i].push_back(itv);
						itvs[j].push_back(itv);
					}
				}
			}
			int cur(0);
			for(int i(0); i < n; i++) {
				if(i == 1) {
					itvs[i].clear();
					itvs[i].push_back(make_pair(0., 1e9));
					num[i].push_back(cur++);
					continue;
				}
				if(i != 0 && itvs[i].empty()) {
					continue;
				}
				sort(itvs[i].begin(), itvs[i].end());
				static vector<pair<double, double> > tmp;
				tmp.clear();
				double bg, ed;
				if(i == 0) {
					bg = ed = 0;
				}else {
					bg = -1;
					ed = -1;
				}
				for(int j(0); j < (int)itvs[i].size(); j++) {
					if(bg == -1) {
						bg = itvs[i][j].first;
						ed = itvs[i][j].second;
					}else if(itvs[i][j].first < ed + s + eps) {
						ed = max(ed, itvs[i][j].second);
					}else {
						tmp.push_back(make_pair(bg, ed));
						bg = ed = -1;
					}
				}
				if(bg != -1) {
					tmp.push_back(make_pair(bg, ed));
				}
				itvs[i] = tmp;
				//printf("%d %d %d\n", i, tmp.size(), cur);
				for(int j(0); j < (int)itvs[i].size(); j++) {
					num[i].push_back(cur++);
				}
			}
			//printf("!!%d\n", cur);
			for(int i(0); i < cur; i++) {
				rela[i] = i;
			}
			for(int i(0); i < n; i++) {
				for(int j(i + 1); j < n; j++) {
					if(i == j) {
						continue;
					}
					if(go[i][j] != make_pair(1e9, 0.)) {
						int x(upper_bound(itvs[i].begin(), itvs[i].end(), go[i][j], cmp) - 1 - itvs[i].begin());
						x = num[i][x];
						int y(upper_bound(itvs[j].begin(), itvs[j].end(), go[i][j], cmp) - 1 - itvs[j].begin());
						y = num[j][y];
						//printf("%d %d\n",x, y);
						rela[getr(x)] = getr(y);
					}
				}
			}
			//printf("%d %d %d\n", getr(0), getr(1), getr(2));
			if(getr(num[0][0]) == getr(num[1][0])) {
				ri = mid;
			}else {
				le = mid;
			}
		}
		printf("%.10f\n", mid);
	}
}
