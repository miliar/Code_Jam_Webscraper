//============================================================================
// Name        : Practice.cpp
// Author      : Code 08
// Version     :
// Copyri   :
// Description :
//============================================================================

#include <cstring>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <math.h>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <list>
#include <climits>
#include <cctype>
#include <bitset>
#include <iostream>
#include <complex>

using namespace std;

typedef stringstream ss;
typedef long long ll;
typedef pair<ll, ll> ii;
typedef vector<vector<ii> > vii;
typedef vector<string> vs;
typedef vector<ll> vi;
typedef vector<double> vd;
typedef long double ld;
typedef vector<vector<ll> > matrix;
typedef complex<double> point;

#define all(v) v.begin(), v.end()
#define rall(v) v.rbegin(), v.rend()
#define sz(v) ((ll)v.size())
#define clr(v, d) memset(v, d, sizeof(v))
#define polar(r,t) ((r)*exp(point(0,(t))))
#define length(a) hypot((a).real(),(a).imag())
#define angle(a) atan2((a).imag() , (a).real())
#define vec(a,b) ((b)-(a))
#define dot(a,b) ((conj(a)*(b)).real())
#define cross(a,b) ((conj(a)*(b)).imag())
#define lengthSqr(a) dot(a,a)
#define rotate(v,t) ((v)*exp(point(0,t)))
#define rotateAbout(v,t,a) (rotate(vec(a,v),t)+(a))
#define reflect(v,m) (conj((v)/(m))*m)
#define dist(a,b) (sqrt(pow((a).real()-(b).real(),2.0)+pow((a).imag()-(b).imag(),2.0)))
#define normalize(a) ((a)/length(a))

int dx[] = { 1, -1, 0, 0 };
int dy[] = { 0, 0, 1, -1 };
double PI = 3.1415926535897932384626433832795;

const ll oo = (ll) 1e9 + 1;
const double eps = 1e-9;
const ll mod = 1000000007;

//bool PointOnRay(const point &a, const point & b, const point &p) {
//	return fabs(cross(vec(a,b), vec(a,p))) < eps
//			&& dot(vec(a,b),vec(a,p)) > -eps;
//}
//
//bool PointOnline(const point &a, const point &b, const point &p) {
//	return fabs(cross(vec(a,b), vec(a,p))) < eps;
//}
//
//bool PointOnSegment(const point &a, const point & b, const point &p) {
//	if (lengthSqr(vec(a,b)) < eps)
//		return lengthSqr(vec(a,p)) < eps;
//	return PointOnRay(a, b, p) && PointOnRay(b, a, p);
//}
//
//bool intersectSeg(const point &a, const point &b, const point &p,
//		const point &q, point & ret) {
//	double d1 = cross(p - a, b - a);
//	double d2 = cross(q - a, b - a);
//	ret = (d1 * q - d2 * p) / (d1 - d2);
//	if (PointOnSegment(a, b, p) || PointOnSegment(a, b, q)
//			|| PointOnSegment(p, q, a) || PointOnSegment(p, q, b))
//		return true;
//	return fabs(d1 - d2) > eps && PointOnSegment(a, b, ret)
//			&& PointOnSegment(p, q, ret);
//}
//
//double PointLineDistance(const point &a, const point &b, const point &p,
//		point &res) {
//	double scale = dot(vec(a,b),vec(a,p)) / lengthSqr(vec(a,b));
//	res.real() = a.real() + scale * (b.real() - a.real());
//	res.imag() = a.imag() + scale * (b.imag() - a.imag());
//	return dist(p, res);
//}
//
//double pointSegmentDistance(const point &a, const point &b, const point &p,
//		point &res) {
//	double det = dot(vec(a,b),vec(a,p)) / lengthSqr(vec(a,b));
//	if (det < 0) {
//		res = a;
//		return dist(a, p);
//	}
//	if (det > 1) {
//		res = b;
//		return dist(b, p);
//	}
//	return PointLineDistance(a, b, p, res);
//}

//freopen("in.txt","r",stdin);
//freopen("out.txt","w",stdout);

int main() {

	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int test;
	cin>>test;
	int tc=0;
	while(test--){
		tc++;
		ll n;
		cin>>n;
		ll a[n];
		ll res1=0;
		ll res2=0;
		ll mx=0;
		for(int i=0;i<n;i++){
			cin>>a[i];
			if(i>0){
				if(a[i] < a[i-1]){
					res1+=a[i-1]-a[i];
					mx = max(mx , a[i-1]-a[i]);
				}
			}
		}

		for(int i=0;i<n-1;i++){
			res2+=min(mx,a[i]);
		}
		cout<<"Case #"<<tc<<": "<<res1<<" "<<res2<<endl;
	}
	return 0;

}
























