#include <cstdio>

void markDigits(int n, bool arr[10]);
bool haveSeenAll(bool arr[10]);

int main() {
	int cases, ii;
	
	scanf("%d", &cases);
	for(ii=0; ii < cases; ii++) {
		
		int n;
		scanf("%d", &n);
		
		bool digits[10];
		for(int j = 0; j < 10; j++) digits[j] = false;
		
		int i = 0;
		
		do {
			markDigits(n*(++i), digits);
			if(n==0) break;
		} while(!haveSeenAll(digits));
		
		printf("Case #%d: ", ii+1);
		if(!haveSeenAll(digits)) {
			printf("INSOMNIA\n");
		} else {
			printf("%d\n", n*i);
		}
		
	}
	
	return 0;
}

void markDigits(int n, bool arr[10]) {
	// Mark last digit first, before base case;
	arr[n%10] = true;
	
	if(n/10 == 0) return;
	markDigits(n/10, arr);
}

bool haveSeenAll(bool arr[10]) {
	for(int i=0; i < 10; i++) if(!arr[i]) return false;
	return true;
}