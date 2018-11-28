#include <cstdio>
#include <cmath>
using namespace std;

int isPal(long long X)
{
	long long reversedX = 0;
	long long copyX = X;
	while (copyX) {
		reversedX = reversedX * 10 + copyX % 10;
		copyX /= 10;
	}
	if (reversedX == X) return 1;
	return 0;
}

int main() {
	int T;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		printf("Case #%d: ", t);
		long long A, B;
		int sol = 0;
		scanf("%lld %lld", &A, &B);
		long long sqrtA, sqrtB;
		sqrtA = (long long)sqrt((double)A);
		sqrtB = (long long)sqrt((double)B);
		for (long long i = sqrtA; i <= sqrtB; i++) {
			if (!isPal(i)) continue;
			long long ii = i * i;
			if (ii >= A && ii <= B) sol += isPal(ii);
		}			
		printf("%d\n", sol);
	} 
	return 0;
}