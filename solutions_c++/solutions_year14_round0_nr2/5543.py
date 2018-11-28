#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
int TestCase;
double C, F, X;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &TestCase);
	for (int Case = 1; Case <= TestCase; Case ++) {
		scanf("%lf%lf%lf", &C, &F, &X);
		double Ret = X / 2.0;
		double V = 2.0, S = 0.0;
		for (int i = 1; i <= X; i ++) {
			S += C / V;
			V += F;
			Ret = min(Ret, S + X / V);
		}
		printf("Case #%d: %.8lf\n", Case, Ret);
	}
	return 0;
}
