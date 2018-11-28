#include<stdio.h>
#include<math.h>
bool is_palindrome(long long n) {
	long long m = n;
	long long p = 0;
	while(m) {
		p = p * 10 + m % 10;
		m /= 10;
	}
	return p == n;
}

int main() {
	int C;
	scanf("%d", &C);
	for(int i = 1; i <=C; i++) {
		long long A, B, l, h;
		scanf("%lld %lld", &A, &B);
		l = ceil(sqrt(A));
		h = floor(sqrt(B));
		long long count = 0;
		for(long long r = l; r <=h; r++) {
			if(is_palindrome(r) && is_palindrome(r * r)) {
				count++;
			}
		}
		printf("Case #%d: %lld\n", i, count);
	}
	//printf("%d %d", is_palindrome(123321), is_palindrome(2441));
}

