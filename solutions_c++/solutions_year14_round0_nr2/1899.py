#include <stdio.h>
#include <stdlib.h>
#include <iostream>

using namespace std;

int main() {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int tc, count = 0;
	double X, C, F;
	cin >> tc;
	while (tc--) {
		cin >> C >> F >> X;
		int i = 0;
		while (i + 1 < X/C - 2.0/F) i++;
		double t = X / (2.0 + (double)i * F);
		for (int j = 0; j < i; j++) t += C / (2.0 + (double)j * F);
		printf("Case #%d: %.7lf\n",++count,t);
	}
}
