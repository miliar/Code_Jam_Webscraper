#include <set>
#include <iostream>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <cmath>
using namespace std;

struct Rect {
	double x0, x1, y0, y1;
	double s;
	Rect(int x0, int x1, int y0, int y1)
		: x0(x0-0.5), x1(x1+0.5), y0(y0-0.5), y1(y1+0.5), s(100000.0)
	{
	}
	bool operator<(const Rect& other) const {
		return this->s < other.s;
	}
};

void dpr(const Rect& r, double x, double y, double& ret)
{
	double d;
	double x2, y2;
	if (r.x0 > x) x2 = r.x0;
	else if (r.x1 < x) x2 = r.x1;
	else x2 = x;
	if (r.y0 > y) y2 = r.y0;
	else if (r.y1 < y) y2 = r.y1;
	else y2 = y;
//	d = hypot(x - x2, y - y2);
	d = max(abs(x - x2), abs(y - y2));
	if (ret > d) ret = d;
}

int main(void)
{
	int tn;
	cin >> tn;
	for (int ti = 1; ti <= tn; ti++) {
		int w, h, b;
		cin >> w >> h >> b;
		int n = b+2;
		vector<Rect> v;
		v.reserve(n);
		v.push_back(Rect(-1, -1, 0, h-1));
		v.push_back(Rect(w, w, 0, h-1));
		for (int i = 0; i < b; i++) {
			int x0, x1, y0, y1;
			cin >> x0 >> y0 >> x1 >> y1;
			v.push_back(Rect(x0, x1, y0, y1));
		}
		vector<vector<double>> d(n, vector<double>(n, 0.0));
		for (int i = 0; i < n; i++) {
			for (int j = i+1; j < n; j++) {
				double dm = 100000.0;
				dpr(v[i], v[j].x0, v[j].y0, dm);
				dpr(v[i], v[j].x0, v[j].y1, dm);
				dpr(v[i], v[j].x1, v[j].y0, dm);
				dpr(v[i], v[j].x1, v[j].y1, dm);
				dpr(v[j], v[i].x0, v[i].y0, dm);
				dpr(v[j], v[i].x0, v[i].y1, dm);
				dpr(v[j], v[i].x1, v[i].y0, dm);
				dpr(v[j], v[i].x1, v[i].y1, dm);
				d[i][j] = d[j][i] = dm;
//cerr << i << " " << j << ": " << dm << endl;
			}
		}
		v[0].s = 0.0;
		set<pair<double, int>> s;
		s.insert(make_pair(0.0, 0));
		while (!s.empty()) {
			auto it = s.begin();
			int i = it->second;
			s.erase(it);
			for (int j = 0; j < n; j++) {
				double d2 = v[i].s + d[i][j];
				if (d2 < v[j].s) {
					auto it = s.find(make_pair(v[j].s, j));
					if (it != s.end()) {
						s.erase(it);
					}
					v[j].s = d2;
					s.insert(make_pair(d2, j));
				}
			}
		}

		cout << "Case #" << ti << ": " << v[1].s << endl << flush;
	}
	return 0;
}
