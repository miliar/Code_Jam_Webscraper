#include <cstdio>
#include <algorithm>
#include <set>
#include <cmath>

std::set<long long> S;

long long reverse(long long x) {
	long long result = 0;
	while(x > 0) {
		result *= 10;
		result += x % 10;
		x /= 10;
	}
	
	return result;
}

void prepare() {
	long long max = std::pow(10, 7);
	for(long long x = 1; x < max; ++x) {
		if(x == reverse(x) && x * x == reverse(x * x)) {
			//printf("%lld\n", x*x);
			S.insert(x*x);
		}
	}
}

int carryOut() {
	long long A, B;
	
	scanf("%lld %lld", &A, &B);
	//printf("%d %d\n", A, B);
	if(A == B)
		return 0 + (S.find(A) != S.end() ? 1 : 0);
	return std::distance(S.upper_bound(A), S.lower_bound(B)) + (S.find(A) != S.end() ? 1 : 0) + (S.find(B) != S.end() ? 1 : 0);
}

int main() {
	prepare();
	
	int T;
	
	/*long long x;
	scanf("%lld", &x);
	printf("%lld\n", reverse(x));*/
	
	scanf("%d", &T);
	for(int testCase = 1; testCase <= T; ++testCase) {
		printf("Case #%d: %d\n", testCase, carryOut());
	}
}
