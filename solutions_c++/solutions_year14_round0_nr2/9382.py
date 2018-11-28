#include<cstdio>
#include<iostream>
#include<cstring>

using namespace std;

int T;
double mtm, C, F, X;

int main() {
	//freopen("D://B-small-attempt0.in", "r", stdin);
	//freopen("D://B-small-attempt0.out", "w", stdout);
	scanf("%d", &T);
	for (int id = 1; id <= T; ++id) {
		double nps = 2.0, t, nt = 0;
		scanf("%lf%lf%lf", &C, &F, &X);
		t = X / nps + nt;
		do {
			mtm = t;
			nt += C / nps;
			nps += F;
			t = X / nps + nt;
		} while(t < mtm);
		printf("Case #%d: %.7lf\n", id, mtm);
	}
	//system("pause");
	return 0;
}
