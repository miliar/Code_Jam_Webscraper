#include<bits/stdtr1c++.h>
using namespace std;
typedef long long LL;
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <complex>
#include <iostream>
using namespace std;

typedef complex<double> point;
#define sz(a) ((int)(a).size())
#define all(n) (n).begin(),(n).end()
#define EPS 1e-9
#define OO 1e9
#define X real()
#define Y imag()
#define vec(a,b) ((b)-(a))
#define polar(r,t) ((r)*exp(point(0,(t))))
#define angle(v) (atan2((v).Y,(v).X))
#define length(v) ((long double)hypot((v).Y,(v).X))
#define lengthSqr(v) (dot(v,v))
#define dot(a,b) ((conj(a)*(b)).real())
#define cross(a,b) ((conj(a)*(b)).imag())
#define rotate(v,t) (polar(v,t))
#define rotateabout(v,t,a)  (rotate(vec(a,v),t)+(a))
#define reflect(p,m) ((conj((p)/(m)))*(m))
#define normalize(p) ((p)/length(p))
#define same(a,b) (lengthSqr(vec(a,b))<EPS)
#define mid(a,b) (((a)+(b))/point(2,0))
#define perp(a) (point(-(a).Y,(a).X))
#define colliner pointOnLine

enum STATE {
	IN, OUT, BOUNDRY
};

bool intersect(const point &a, const point &b, const point &p, const point &q,
		point &ret) {

	//handle degenerate cases (2 parallel lines, 2 identical lines,   line is 1 point)

	double d1 = cross(p - a, b - a);
	double d2 = cross(q - a, b - a);
	ret = (d1 * q - d2 * p) / (d1 - d2);
	if (fabs(d1 - d2) > EPS)
		return 1;
	return 0;
}

bool pointOnLine(const point& a, const point& b, const point& p) {
	// degenerate case: line is a point
	return fabs(cross(vec(a,b), vec(a,p))) < EPS;
}

bool pointOnRay(const point& a, const point& b, const point& p) {
	//IMP NOTE: a,b,p must be collinear
	return dot(vec(a,p), vec(a,b)) > -EPS;
}

bool pointOnSegment(const point& a, const point& b, const point& p) {
	if (!colliner(a, b, p))
		return 0;
	return pointOnRay(a, b, p) && pointOnRay(b, a, p);
}

double pointLineDist(const point& a, const point& b, const point& p) {
	// handle degenrate case: (a,b) is point

	return fabs(cross(vec(a,b),vec(a,p)) / length(vec(a,b)));
}

double pointSegmentDist(const point& a, const point& b, const point& p) {
	if (dot(vec(a,b),vec(a,p)) < EPS)
		return length(vec(a,p));
	if (dot(vec(b,a),vec(b,p)) < EPS)
		return length(vec(b,p));
	return pointLineDist(a, b, p);
}
struct cmp {
	point about;
	cmp(point c) {
		about = c;
	}
	bool operator()(const point& p, const point& q) const {
		double cr = cross(vec(about, p), vec(about, q));
		if (fabs(cr) < EPS)
			return make_pair(p.Y, p.X) < make_pair(q.Y, q.X);
		return cr > 0;
	}
};

void sortAntiClockWise(vector<point>& pnts) {
	point mn(1 / 0.0, 1 / 0.0);
	for (int i = 0; i < sz(pnts); i++)
		if (make_pair(pnts[i].Y, pnts[i].X) < make_pair(mn.Y, mn.X))
			mn = pnts[i];

	sort(all(pnts), cmp(mn));
}

void convexHull(vector<point> pnts, vector<point> &convex) {
	sortAntiClockWise(pnts);
	convex.clear();
	convex.push_back(pnts[0]);
	if (sz(pnts) == 1)
		return;
	convex.push_back(pnts[1]);
	if (sz(pnts) == 2) {
		if (same(pnts[0], pnts[1]))
			convex.pop_back();
		return;
	}
	for (int i = 2; i <= sz(pnts); i++) {
		point c = pnts[i % sz(pnts)];
		while (sz(convex) > 1) {
			point b = convex.back();
			point a = convex[sz(convex) - 2];
			if (cross(vec(b, a), vec(b, c)) < -EPS)
				break;
			convex.pop_back();
		}
		if (i < sz(pnts))
			convex.push_back(pnts[i]);
	}
}

bool check(point &a,vector<point> &p)
{
	vector<point>conv;
	convexHull(p,conv);
	int t=conv.size();
	for(int i=0;i<t;i++)
	{
		int j=(i+1)%t;
		if(pointOnSegment(conv[i],conv[j],a))
			return 1;
	}
	return 0;
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("2.in", "r", stdin);
	freopen("2.out","w",stdout);
#endif // ONLINE_JUDGE	ios::sync_with_stdio(false);	cin.tie(NULL);
	cout.tie(NULL);
	int tc;
	int ic = 1;
	cin >> tc;
	while (tc--) {

		int n;
		vector<point> v;
		cin >> n;
		int a,b;
		for (int i = 0; i < n; i++) {
			cin >> a >> b;
			v.push_back(point(a, b));
		}
		cout << "Case #" << ic++ << ":" << endl;
		if (n <= 3) {
			for (int i = 0; i < n; i++)
				cout << 0 << endl;
			continue;
		}
		vector<point> t;
		for (int i = 0; i < n; i++) {
			int mini = n-1;
			for (int j = 0; j < (1 << (n)); j++) {
				if (!(j & (1 << i)))
					continue;
				t.clear();
				int c = 0;
				for (int p = 0; p < n; p++) {
					if (!(j & (1 << p))) {
						c++;
						continue;
					} else
						t.push_back(v[p]);
				}
				if(check(v[i],t))
					mini=min(mini,c);
			}
			cout<<mini<<endl;
		}

	}
	return 0;

}
