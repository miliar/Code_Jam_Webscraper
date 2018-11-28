#pragma warning(disable:4996)
#include <stdio.h>
void printTestcase(int x, long long int y){
	printf("Case #%d: %lld\n", x, y);
}
long long int reverse(long long int n){
	long long int r = 0;
	while (n > 0){
		r *= 10;
		r += n % 10;
		n /= 10;
	}
	return r;
}
int digit(long long int n){
	int r = 0;
	while (n > 0){
		n /= 10;
		++r;
	}
	return r;
}
long long int arr[100];
int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i){
		scanf("%d", &arr[i]);
	}
	long long int count;
	for (int i = 0; i < t; ++i){
		count = 0;
		int length = digit(arr[i]);
		if (length == 1){
			printTestcase(i + 1, arr[i]);
			continue;
		}
		for (int j = 1, k = 0; j <= length - 1; ++j, ++count){
			if (j % 2){
				count += k;
				k = (k + 1) * 10 - 1;
				count += k;
			}
			else{
				count += k * 2;
			}
		}
		//1...0 까지 부름
		long long int yRev = 0, nRev = 0, minus = 1;
		for (int j = 0; j < length - 1; ++j){
			minus *= 10;
		}
		nRev = arr[i] - minus;
		if (arr[i] % 10 == 0){
			--arr[i];
			++yRev;
		}
		long long int high = arr[i];
		for (int j = 0; j < length / 2; ++j){
			high /= 10;
		}
		high = reverse(high);
		yRev += high;
		long long int low = 0;
		int divisor = 1;
		for (int j = 0; j < length / 2; ++j){
			divisor *= 10;
		}
		low = arr[i] % divisor;
		yRev += low;

		
		if (nRev < yRev){
			count += nRev;
		}
		else{
			count += yRev;
		}
		printTestcase(i + 1, count);
	}
	return 0;
}