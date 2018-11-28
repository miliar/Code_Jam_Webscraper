#include <complex>
#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <stdio.h>
#include  <stack>

using namespace std;
typedef complex<long long> point;
#define X real()
#define Y imag()
#define vec(a,b) ((b)-(a))
#define cross(a,b) (-(((a) * conj((b))).imag()))
#define dot(a,b) (((a) * conj((b))).real())
#define ccw(a,b,c) (cross(vec((a),(b)),vec((a),(c))))
#define sz(a) (int)((a).size())
#define sqrdist(a,b) (dot(vec(a,b),vec(a,b)))
bool safe(point &a, point &b, point &c) {
	long long cp = ccw(a,b,c);
	return cp > 0 || (cp == 0 && sqrdist(a,b) < sqrdist(b,c));
}
void CH(vector<point> &points, vector<point> &hull) {
	if(points.size() <= 2){
		for(int i = 0;i<points.size();i++){
			hull.push_back(points[i]);
		}
		return;
	}
	int n = sz(points);
	int min = 0;
	for (int i = 1; i < n; i++)
		if (points[i].Y < points[min].Y
				|| (points[i].Y == points[min].Y && points[i].X < points[min].X))
			min = i;
	vector<int> hull_index;
	hull_index.push_back(min);
	while (hull_index[hull_index.size() - 1] != min || hull_index.size() == 1) {
		int last = hull_index[hull_index.size() - 1];
		int temp = (last + 1) % n;
		for (int j = 0; j < n; j++)
			if (j != last && safe(points[temp], points[last], points[j]))
				temp = j;
		hull_index.push_back(temp);
	}
	for (int i = 0; i < sz(hull_index) - 1; i++)
		hull.push_back(points[hull_index[i]]);
}

bool point_on_segment_ab(point &p, point &a, point &b) {
	bool x = p.X <= max(a.X, b.X) && p.X >= min(a.X, b.X);
	bool y = p.Y <= max(a.Y, b.Y) && p.Y >= min(a.Y, b.Y);
	return x && y && cross(vec(p,a),vec(p,b)) == 0;
}
bool point_in_convex_polygon(point & p, vector<point> &polygon) {
	bool in = true;
	int n = sz(polygon);
	for (int i = 0; i < n && in; i++) {
		in = in && ccw(p,polygon[i],polygon[(i+1)%n]) > 0;
		if (point_on_segment_ab(p, polygon[i], polygon[(i + 1) % n]))
			return true;
	}
	return in;
}
int bitcount(int n){
	int r = 0;
	while(n!=0){
		r++;
		n&=n-1;
	}
	return r;
}
int main(int argc, char **argv) {
	int tc;
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	scanf("%d", &tc);
	for(int cc=1;cc<=tc;cc++){
		int n;
		scanf("%d", &n);
		vector<point> pts;
		vector<int> minima;
		for(int i = 0;i<n;i++){
			int x, y;
			scanf("%d %d", &x, &y);
			pts.push_back(point(x, y));
			minima.push_back(n-1);
		}
		for(int i = 0;i<1<<n;i++){
			vector<point> current;
			for(int j = 0;j<n;j++)
				if(i & 1<<j)
					current.push_back(pts[j]);
			vector<point> hull;
			CH(current, hull);
			for(int j = 0;j<pts.size();j++){
				for(int k = 0;k<hull.size();k++){
					if(point_on_segment_ab(pts[j], hull[k], hull[(k + 1)%hull.size()]))
						minima[j]=min(minima[j], n - bitcount(i));

				}
			}
		}
		printf("Case #%d:\n", cc);
		for(int i = 0;i<n;i++)
			printf("%d\n", minima[i]);
	}
	return 0;
}
