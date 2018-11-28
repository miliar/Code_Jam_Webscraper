#include<bits/stdc++.h>
using namespace std;
double eps = 1e-9;
int dcmp(double x, double y) {
	if (fabs(x - y) <= eps)
		return 0;
	return (x < y ? -1 : 1);
}
double r[105], x[105];



int main() {
	freopen("/home/ahmed_ossama/Round 2/Task B/B-small-attempt1.in", "r", stdin);
	freopen("/home/ahmed_ossama/Round 2/Task B/B-small-attempt1.out", "w", stdout);


	int t;
	int id = 1;
	cin >> t;
	while (t--) {
		int n;
		double vout, xout;
		cin >> n >> vout >> xout;
		for (int i = 0; i < n; i++)
			cin >> r[i] >> x[i];
		printf("Case #%d: ", id++);
		if (n == 1) {
			if (dcmp(x[0], xout) == 0)
				printf("%.9lf\n", vout / r[0]);
			else
				printf("IMPOSSIBLE\n");
			continue;
		}
		else {
			double ans = 1e15;
			if (dcmp(x[0], xout) == 0)
				ans = min(ans,  vout / r[0]);
			if (dcmp(x[1], xout) == 0)
				ans = min(ans,  vout / r[1]);

			if (dcmp(x[0], xout) == 0 && dcmp(x[1], xout) == 0)
				ans = min(ans, vout / (r[1] + r[0]));

			double v0 = vout * (xout - x[1]) / (x[0] - x[1]);
			double v1 = vout - v0;


			if (dcmp(x[0], x[1]) != 0 && dcmp(v0, 0.0) >= 0 && dcmp(v1, 0.0) >= 0)
				ans = min(ans, max(v0 / r[0] ,v1 / r[1]));

			if (ans < 1e15)
				printf("%.9lf\n", ans);
			else
				printf("IMPOSSIBLE\n");

		}


	}


}

