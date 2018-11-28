#include <cstdio>
#include <cmath>

using namespace std;

int main(){
	int tc, caseNum=1;
	unsigned long long r1, r2, t, cirCount, needed;
	freopen("C:\\googlecj\\bullsmall.in", "r", stdin);
	freopen("C:\\googlecj\\bullsmall.out", "w", stdout);


	scanf("%d", &tc);
	while( tc-- ){
		scanf("%llu %llu", &r1, &t);
		cirCount = 0;
		r2 = r1+1;
		needed = r2*r2 - r1*r1;
		while( needed<=t ){
			cirCount ++;
			t -= needed;
			r1 += 2;
			r2 = r1+1;
			needed = r2*r2 - r1*r1;
		}

		printf("Case #%d: %llu\n", caseNum++, cirCount);
	}

	return 0;
}

