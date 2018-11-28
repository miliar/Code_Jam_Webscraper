#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
using namespace std;

#define double long double

const double eps = 1e-15;
const int maxn = 100 + 5;

int N;
double V, X;
pair<double, double> a[maxn];

double cross(double x0, double y0, double x1, double y1, double x2, double y2)
{
	x1 -= x0;
	y1 -= y0;
	x2 -= x0;
	y2 -= y0;
	return x1 * y2 - x2 * y1;
}

double solve(double x0, double y0, double x1, double y1, double x, double y)
{	
	double S1 = cross(x0, y0, x1, y1, 0, 0);
	double S2 = cross(x0, y0, x1, y1, x, y);
	if (S1 < eps)
		return x / max(x0, x1);
	else
		return (S1 - S2) / S1;
}

void work()
{
	cin >> N >> V >> X;
	for (int i = 0; i < N; ++i) 
		cin >> a[i].second >> a[i].first;	
	sort(a, a + N);
	if (X < a[0].first - eps || X > a[N - 1].first + eps) {
		cout << "IMPOSSIBLE" << endl;
		return;
	}	
	/*
	for (int i = N - 1; i >= 0; --i)
		if (abs(X - a[i].first) < eps) {
			cout << V / a[i].second  << endl;
			return;
		}
	*/	
	double ans = -1;
	double x = 0, y = 0;
	for (int i = 0; i < N; ++i) {
		double tx = x + a[i].second;
		double ty = y + a[i].second * a[i].first;
		if (y <= (X + eps) * x && ty >= (X - eps) * tx) {
			double s = solve(x, y, tx, ty, V, V * X);
			if (ans < 0 || s < ans)
				ans = s;
		}
		x = tx;
		y = ty;
	}
	x = 0;
	y = 0;
	for (int i = N - 1; i >= 0; --i) {
		double tx = x + a[i].second;
		double ty = y + a[i].second * a[i].first;
		if (ty <= (X + eps) * tx && y >= (X - eps) * x) {
			double s = solve(tx, ty, x, y, V, V * X);
			if (ans < 0 || s < ans)
				ans = s;
		}
		x = tx;
		y = ty;
	}
	if (ans < 0)
		cout << "IMPOSSIBLE" << endl;
	else
		cout << ans << endl;
}

int main()
{
    freopen("b1.in", "r", stdin);
    freopen("b1.out", "w", stdout);

	cout << fixed;
	cout.precision(9);
    int t2;
    cin >> t2;
    for (int t1 = 1; t1 <= t2; ++t1) {    	
    	//cerr << t1 << endl;
        printf("Case #%d: ", t1);
		work();        
    }
    
    return 0;
}

