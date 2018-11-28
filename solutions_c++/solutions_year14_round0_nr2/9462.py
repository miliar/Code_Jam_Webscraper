
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <map>
#include <set>
#include <queue>
#include <climits>
#include <cstdlib>
#include <sstream>
#include <stack>

using namespace std;

int main()
{
		int test, tst;
		double C, F, X;
		double t1, t2;
		double R;

		scanf("%d", &test);

		for (int tst = 1; tst <= test; tst++) {
			double time = 0;
			scanf("%lf%lf%lf", &C, &F, &X);
			R = 2;
			t1 = X/R;
			t2 = C/R + X/(R + F);
			while ( (t2-t1) <= 1e-7) {
				time += C/R;
				R += F;
				t1 = X/R;
				t2 = C/R + X/(R + F);
			}
			time += t1;
			printf("Case #%d: %.7lf\n", tst, time);
		}

		return 0;
}


