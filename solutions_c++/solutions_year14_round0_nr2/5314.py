#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

#define eps (1e-9)
#define fless(a,b) ((a)+eps<(b))
#define fleq(a,b) ((a)-eps<(b))

double solve(double C, double F, double X)
{
	double a = C*F;
	double b = C*F + 2*C -F*X;
	if (fleq(0, b)) {
		return X/2;
	} else {
		double n = -b / a;
		int low = max(0, (int)floor(n-2));
		int high = floor(n+2);
		double ans = 1e40;
		for (int i = low; i <= high; i++) {
			double cur = 0;
			for (int j = 0; j < i; j++)
				cur += C/(2+j*F);
			cur += X/(2+i*F);
			ans = min(cur, ans);
		}
		return ans;
	}
	return 0;
}

int main()
{
	int T; scanf ("%d", &T);
	double C, F, X;
	for (int cc = 1; cc <= T; cc++) {
		scanf ("%lf %lf %lf", &C, &F, &X);
		printf ("Case #%d: %.7lf\n", cc, solve(C,F,X));
	}
	return 0;
}
