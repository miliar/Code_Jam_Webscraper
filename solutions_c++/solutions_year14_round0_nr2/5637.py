#include <cstdio>
#include <cstdlib>
#include <map>
#include <queue>
#include <cstring>
#include <string>
#include <cctype>
#include <algorithm>
#include <cmath>
#include <set>

using namespace std;

int n, t;

int main () {
	scanf("%d", &t);
	for (int _ = 1; _ <= t; _++){
		printf("Case #%d: ", _);
		double c, f, x;
		scanf("%lf %lf %lf", &c, &f, &x);
		double oldtime = 0;
		double best = x/2;
		for(int i = 0; i < 100000; ++i) {
			double rate = 2 + f*i;
			double newtime = c/rate;
			oldtime += newtime;
			rate += f;
			double total = oldtime + x/rate;
			if (total > best) break;
			best = total;
		}
		printf("%.7lf\n", best);
	}
return 0;
}