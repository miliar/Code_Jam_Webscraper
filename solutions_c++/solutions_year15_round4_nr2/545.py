#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <cstdio>
#include <cmath>
#include <iomanip>
#include <deque>
#include <ctime>
#include <cstring>

//#include <bits/stdc++.h>

using namespace std;

#define fr first
#define sd second
#define pb push_back
#define mp make_pair

#define endl '\n'

#define forr(i, n) for(ll (i) = 0LL; (i) < (n); (i)++)
#define mp3(a, b, c) mp(a, mp(b, c))

typedef long long ll;
typedef pair<ll, ll> pll;
typedef pair<ll, pll> plll;
typedef vector < vector < double > > vvd;
typedef vector < double > vd;
typedef vector < pair < double, double> > vdd;
typedef vector < vector < long long > > vvl;
typedef vector < long long > vl;
typedef vector < pll > vll;

int INT_MAX_VAL = (int)  0x3F3F3F3F;
int INT_MIN_VAL = (int) -0x3F3F3F3F;
ll LONG_MAX_VAL = (ll)   0x3F3F3F3F3F3F3F3F;
ll LONG_MIN_VAL = (ll)  -0x3F3F3F3F3F3F3F3F;

#define MAXN 500006
#define MOD 1000000007

#define EPS 1e-6


double solve_for_one(double V, double X, double R, double C)
{
	double t = V / R;
	if(abs(V * X - t * R * C) < EPS && abs(V - t * R) < EPS && abs(X - C) < EPS) {
		return t;
	} else {
		return -2;
	}

}

void solve(int test)
{
	cout << "Case #" << test << ": ";

	int n; cin >> n;
	double V, X; cin >> V >> X;

	double res = 0;

	if(n == 1) {
		double R, C; cin >> R >> C;
		res = solve_for_one(V, X, R, C);
	} else {

		double R1, C1, R2, C2; cin >> R1 >> C1 >> R2 >> C2;
		if(C1 > X && C2 > X) {
			res = -1;
		} else if(C1 < X && C2 < X) {
			res = -1;
		} else if(fabs(C1 - C2) < EPS) {
			//cout << C1 << " " << C2 << " " << abs(C1 - C2) << endl;
			res = solve_for_one(V, X, R1 + R2, C1);
		} else {


			double dd = R1 * C1 * R2 - R2 * C2 * R1;
			double d1 = R1 * C1 * V - V * X * R1;
			double d2 = V * X * R2 - R2 * C2 * V;

			double t2 = d1 / dd;
			double t1 = d2 / dd;

			//		cout << t1 << " " << t2 << endl;
			double Tr = t1 * R1 * C1 + t2 * R2 * C2;
			double Vr = t1 * R1 + t2 * R2;
/*
			cout << endl;
			cout << R1 << " " << C1 << "   " << R2 << " " << C2 << "  " << V << "  " << X << endl;
			cout << Tr << " " << V * X << endl;
			cout << Vr << " " << V << endl;
			cout << t1 << " " << t2 << endl;
*/
			if(fabs(Tr - V * X) > EPS  || t1 < -EPS || t2 < -EPS || fabs(Vr - V) > EPS) {
				res = -1;
			} else {
				res = max(t1, t2);
			}
		}
	}

	if(res < 0) {
		cout << "IMPOSSIBLE" << endl;
	} else {
		cout << setprecision(9) << fixed << res << endl;
	}


	//cout << res << endl;
}

int main()
{
	cin.tie(0);
	ios::sync_with_stdio(false);

	int t; cin >> t;
	for(int i = 1; i <= t; ++i) solve(i);

	return 0;
}
