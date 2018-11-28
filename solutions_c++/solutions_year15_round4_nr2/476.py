#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <cstdlib>
#include <cstdio>
using namespace std;

typedef unsigned long long ULL;
#define INF (1<<30)

int N;
double X, V;

struct water
{
	double R, C;
};
water W[100];

void input()
{
	cin >> N >> V >> X;
	for (int i=0; i< N; ++i) cin >> W[i].R >> W[i].C;
}


bool valid()
{
	int large = 0, small = 0, equal = 0;
	for (int i=0;i<N;++i) {
		if (W[i].C == X) ++ equal;
		else if (W[i].C > X) ++ large;
		else ++ small;
	}
	if (equal == 0 && large * small == 0) return false;
	return true;
}

double equal()
{
	double R = 0;
	for (int i=0;i<N;++i) {
		if (W[i].C == X) R += W[i].R;
	}
	if (R > 1e-8) {
		return V/R;
	}
	return (double)INF;
}

double diff()
{
	water S = W[0], L = W[1];
	if (S.C > L.C) {
		S = W[1], L = W[0];
	}
	if (S.C >= X || L.C <= X) return (double)INF;

	double Vl = V * (S.C - X) / (S.C - L.C);
	double Vs = V * (L.C - X) / (L.C - S.C);

	double Tl = Vl / L.R;
	double Ts = Vs / S.R;

//	printf(">>>Small: (C: %.4f, R: %.4f, V: %.4f, T: %.4f)\n", S.C, S.R, Vs, Ts);
//	printf(">>>Large: (C: %.4f, R: %.4f, V: %.4f, T: %.4f)\n", L.C, L.R, Vl, Tl);


	return (Tl > Ts?Tl: Ts);
}

double solve()
{
	if (!valid()) return -1.0;
	double eq = equal();
	double df = diff();

	return (eq < df? eq: df);
}

int main()
{
	int T, nCase = 1;
	cin >> T;
	while (T--) {
		input();
		cout << "Case #" << nCase ++ << ": ";
		double ans = solve();
		if (ans < 0) cout << "IMPOSSIBLE";
		else printf("%.9f", ans);
		cout << endl;
	}

	return 0;
}

