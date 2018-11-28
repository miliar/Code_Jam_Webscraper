#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>

#define rep(i,n) for(int i=0;i<(int)n;i++)
#define rep2(i,m,n) for(int i=(int)m;i<(int)n;i++)

using namespace std;

long long int solution() {
	long long int r, t, q, c;
	scanf("%lld %lld", &r, &t);
	c = 0;
	q = 0;
	while(t >= q) {
		c++;
		q += 2*(r+2*c-1)-1;
	}
	return c-1;
}

int main() {
	int tc;
	scanf("%d", &tc);
	rep(i,tc) {
		printf("Case #%d: %lld\n", i+1, solution());
	}
	return 0;
}