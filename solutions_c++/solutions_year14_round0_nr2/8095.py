#include <cstdio>
#include <algorithm>
using namespace std;

int t;
long double res, time, cost, more, req, prod;

int main() {
	scanf("%d", &t);
	for(int i = 1; i <= t; i++) {
		scanf("%Lf%Lf%Lf", &cost, &more, &req);
		res = req;
		time = 0;
		prod = 2.;
		while(true) {
			if(time>res)
				break;
			res = min(res, req/prod + time);
			time+=cost/prod;
			prod+=more;
		}
		printf("Case #%d: %.7Lf\n", i, res);
	}
	return 0;
}
