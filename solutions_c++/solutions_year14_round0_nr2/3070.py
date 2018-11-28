#include <iostream>
#include <cstdio>
#include <string.h>
#include <algorithm>
#include <queue>
#include <set>
#include <vector>
using namespace std;

typedef long long ll;

double c, f, x;

int main(){
	int _, cas=0;
	scanf("%d", &_);
	while (_--) {
		scanf("%lf%lf%lf", &c, &f, &x);
		int num = 0;
		double ans = x / 2;
		double cont = 0;
		double now = 2;
		while (1) {
			++num;
			cont += c / now;
			now += f;
			double ret = cont + x / now;
			if (ret > ans) break;
			ans = ret;
		}
		printf("Case #%d: %.8f\n", ++cas, ans);
	}
	return 0;
}
