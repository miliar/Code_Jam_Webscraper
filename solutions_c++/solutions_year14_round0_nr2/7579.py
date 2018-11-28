#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <utility>
#include <algorithm>

#define			OK			std::cout << "------------" << std::endl;
#define			DEBUG(x)		std::cout << #x << " = " << x << std::endl;

using namespace std;

int main()
{
	int T;
	double C, F, X;
	
	scanf("%d", &T);
	for (int _ = 1;_ <= T;_++) {
		printf("Case #%d: ", _);
		scanf("%lf%lf%lf", &C, &F, &X);
		double v = 2.;
		double ans = 0.;
		while (X/v > X/(v+F) + C/v) {
			ans += C/v;
			v += F;
		}
		ans += X/v;
		printf("%.10lf\n", ans);
	}
	return 0;
}
