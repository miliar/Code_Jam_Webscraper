#include <vector>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

const double EPS = 1e-5;

int T, N;
double V, X;
double R[101], C[101];

int main() {
	int T;
	cin >> T;
	for (int times = 1; times <= T; ++times) {
		cin >> N;
		cin >> V >> X;
		for (int i = 0; i < N; ++i) cin >> R[i] >> C[i];
		
		printf("Case #%d: ", times);
		if (N == 1) {
		    if (fabs(X - C[0]) < EPS) {
			    printf("%.8lf\n", V / R[0]);
				continue;
			} else {
			    printf("IMPOSSIBLE\n");
				continue;
			}
		}
		if (N == 2) {
		    if (fabs(C[0] - X) < EPS && fabs(C[1] - X) < EPS) {
				printf("%.8lf\n", V / (R[0] + R[1]));
				continue;
			}
			if (fabs(C[0] - X) < EPS) {
				printf("%.8lf\n", V / R[0]);
				continue;
			}
			if (fabs(C[1] - X) < EPS) {
				printf("%.8lf\n", V / R[1]);
				continue;
			}
			
		    if (C[0] > X + EPS && C[1] > X + EPS) {
			    printf("IMPOSSIBLE\n");
				continue;
			}
		    if (C[0] < X - EPS && C[1] < X - EPS) {
			    printf("IMPOSSIBLE\n");
				continue;
			}
			double y1 = (X - C[1]) / (C[0] - C[1]);
			double y2 = 1 - y1;
			printf("%.8lf\n", max(V * y1 / R[0], V * y2 / R[1]));
		}
	}
    return 0;
}