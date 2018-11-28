#include <bits/stdc++.h>
using namespace std;

#define fileName "B-large"
int caseNum = 0;

double comp(double cc, double ff, int n) {
	double res = 0.0;
	for(int i = 0; i < n; i++) {
		res += cc / ((ff * (double) i) + 2.0);
	}
	return res;
}

double comp2(double ff, double xx, int n) {
	return (xx / (((double) n * ff) + 2));
}

void solve() {
    printf("Case #%d: ", ++caseNum);
	double c, f, x;
	double totalSec = 0.0, prevSec, minSec;
	bool found = false;
		
	scanf("%lf %lf %lf", &c, &f, &x);
	
	int nn = 0;
	
	while(1) {
		if(totalSec == 0.0) {
			totalSec = comp(c, f, nn) + comp2(f, x, nn);
		}
		else {
			prevSec = totalSec;
			totalSec = comp(c, f, nn) + comp2(f, x, nn);
			if (totalSec > prevSec)
				break;
		}
		nn++;
	}
	
	printf("%.7f\n", prevSec);
}

int main() {
    freopen(fileName ".in", "r", stdin);
    freopen(fileName ".txt", "w", stdout);
    
    int T;
    scanf("%d", &T);
	while(T--) {
        solve();
    }
    return 0;
}