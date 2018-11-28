#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

bool isPalindrome(int n) {
	int nrev = 0;
	int number = n;

	while (number > 0) {
		nrev = nrev*10 + (number % 10);
		number/= 10;
	}
	if (nrev == n) 
		return true;
	return false;
}

int main() {
	int n;
	int a, b;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		int res = 0;
		scanf("%d %d", &a, &b);
		for (int j = a; j <= b; j++) { 
			int teste = sqrt(j);
			if (teste*teste == j && isPalindrome(j) && isPalindrome(teste)) {
				res++;
			}
		}
		printf("Case #%d: %d\n", (i+1), res);

	}
	return 0;
}