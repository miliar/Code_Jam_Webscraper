#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

double C, F, X; 

void solve(int cs) {
	scanf("%lf%lf%lf", &C, &F, &X);
	double wyn = 1e9;
	
	double ps = 2, tt = 0.f;
	
	for (int i = 0; i <= X; i++) {
		wyn = min(wyn, tt + X/ps);
		tt += C/ps;
		ps += F;
	}
	printf("Case #%d: %lf\n", cs, wyn);
}

int main() {
	int t; scanf("%d", &t);
	for (int i = 1; i <= t; i++) solve(i);
	return 0;
}