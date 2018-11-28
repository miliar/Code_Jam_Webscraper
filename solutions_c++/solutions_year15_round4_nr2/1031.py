#include <stdio.h>
#include <iostream>
#include <string>
#include <math.h>

using namespace std;

int T, N;
double V, X;
double R[143], C[143];
double cpi = 1e-9;
int cmp(double a, double b) {
    if (fabs(a - b) < cpi)
        return 0;
    if (a < b) return -1;
    	else return 1;
}

int main() {
	freopen("input2.txt", "r", stdin);
	freopen("output2.txt", "w", stdout);
	cin >> T;
	for (int test = 1; test <= T; test++) {
		cin >> N >> V >> X;
        for (int i = 0; i < N; i++)
            cin >> R[i] >> C[i];
        double ans = -1;
        if (N == 1) {
            if (cmp(C[0], X) == 0)
            	ans = V / R[0];
        }
        else {
        	if (N == 2) {
        		if (cmp(C[0], C[1]) == 0) {
	        		if (cmp(C[0], X) == 0)	
	        			ans = V/(R[0]+R[1]);
	        	}
	        	else {
	        		double a = V * (X - C[1]) / (R[0] * (C[0] - C[1]));

	        		double b = (V - R[0]*a) / R[1];
	        		//printf("%.7lf %.7lf\n", a ,b);
	        		if (cmp(a,0) != -1 && cmp(b,0) != -1) {
						ans = a;
	        			if (b > ans) ans = b;	
	        		}
	        	}
        	}
        }
        if (ans < -cpi) cout << "Case #" << test << ": IMPOSSIBLE" << endl;
        	else printf("Case #%d: %.7lf\n", test, ans);
    }

	return 0;
}
