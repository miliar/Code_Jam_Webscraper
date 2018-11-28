#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>

using namespace std;

bool isPalindrome(int x) {

	int aux = x;
	int rev = 0;

	while (aux) {
		rev = rev * 10 + aux % 10;
		aux /= 10;
	}

	return rev == x;
}

int main() {

	int t;
	scanf("%d", &t);

	for (int testCase = 1; testCase <= t; ++testCase) {
		int a, b;
		scanf("%d %d", &a, &b);

		int count = 0;
		int square = 1;
		for (int i = 3; i < 1000; i += 2) {
			if (square >= a && square <= b && isPalindrome(square) && isPalindrome(sqrt(square))) {
				++count;
			}

			square += i;
		}

		printf("Case #%d: %d\n", testCase, count);
	}

	return 0;
}
