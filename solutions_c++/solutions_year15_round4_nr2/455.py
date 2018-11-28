#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <unistd.h>
#include <algorithm>
#include <map>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <string>

#define pb push_back
#define mp make_pair
#define ll long long
#define FOR(i, A, N) for(int (i) = (A); (i) < (N); (i)++)
#define REP(i, N) for(int (i) = 0; (i) < (N); (i)++)
#define eps 0.000000001
using namespace std;
long double R[111], C[111];
long double babs(long double q) {
	if(q < 0)
		return -q;
	return q;
}
int main() {
	int T;
	scanf("%d", &T);
	for(int testc = 1; testc <= T; testc++) {
		long double V, X;
		int n;
		long double ans = 1<<30;
		bool ok = true;
		scanf("%d %Lf %Lf", &n, &V, &X);
		REP(i, n) scanf("%Lf %Lf", R+i, C+i);
		if(n == 1) {
			if(babs(C[0]-X) < eps)
				ans = V/R[0];
			else
				ok = false;
		} else {
			if(C[0] > C[1]) {
				swap(C[0], C[1]);
				swap(R[0], R[1]);
			}
			if(X < C[0]-eps || X > C[1]+eps)
				ok = false;
			else {
				if(babs(C[0]-X) < eps) {
					if(babs(C[1]-X) < eps) {
						ans = V/(R[0]+R[1]);
					} else {
						ans = V/R[0];
					}
				} else if(babs(C[1]-X) < eps) {
					ans = min(ans, V/R[1]);
				} else {
					long double v1 = ((V*X-C[0]*V)/C[0])/(C[1]/C[0]-1);
					long double v0 = V-v1;
					ans = max(v1/R[1], v0/R[0]);
				}
					/*
				//X*V == v0x0+v1x1
				long double kx = X/(C[0]+C[1]);
				long double t1 = V/(R[0]*C[0]/kx), t2 = V/(R[1]*(C[1]/kx));
				ans = max(t1, t2);*/
			}
		}

		if(!ok) {
			printf("Case #%d: IMPOSSIBLE\n", testc);
		}
		else
			printf("Case #%d: %.12Lf\n", testc, ans);
	}
	return 0;
}
