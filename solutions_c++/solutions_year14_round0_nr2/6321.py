#include <cstdio>
#include <cstring>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

int main() {
	int T;
	double C, F, X;
	scanf("%d", &T);
	for(int it = 1;it <= T; ++it) {
		scanf("%lf%lf%lf", &C, &F, &X);
		double pro = 2.0, total = 0;
		double ret = 0.0;
		while(1) {
			double not_buy = X / pro;
			double buy = C / pro + X / (pro + F);
			if(buy < not_buy) {
				ret += C / pro;
				pro += F;
				total = 0;
			} else {
				ret += not_buy;
				break;
			}
		}
		printf("Case #%d: %.7lf\n", it, ret);
	}
}
