#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

double c, f, x;

int main() {
	int t; scanf("%d",&t);
	for(int k = 0; k < t; ++k) {
		scanf("%lf %lf %lf", &c, &f, &x);
		double base = 2, time = 0;
		while((x / base) > (x / (base + f)) + (c / base)) {
			time += c / base;
			base += f;
		}
		time += x / base;
		printf("Case #%d: %.7lf\n", k + 1, time);
	}
	return 0;
}
