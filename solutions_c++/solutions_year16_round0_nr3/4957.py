#include<stdio.h>
#include<iostream>
#include<string>
#include<deque>
#include<algorithm>
using namespace std;
int T, N, J;
char base[100];
void print_binary(unsigned n,char str[32]) {
	int c = 32;
	char* p = str;
	bool b = false;
	while (c--){
		if ((n >> 31) + 48 == '1'){
			b = true;
		}
		if (b == true){
			*p = (n >> 31) + 48;
			*p++;
		}
		n <<= 1;
	}
}
int isPrime(long long n) {
	long long i = 5;
	if (!(n & 1))
		return n == 2;
	if (n % 3 == 0)
		return n == 3;
	long long sn = sqrt(n);
	while (i<=sn){
		if (n%i++ == 0)return 0;
	}
	return n != 1;
}
int isjam() {
	long long arr[10];
	memset(arr, -1,sizeof(long long)*10);
	for (int i = 2; i <= 10; i++){
		int j = N - 1;
		long long digit = 0;
		while (j>-1){
			digit += pow(i, N - j - 1)*(base[j] - 48);
			j--;
		}
		if (isPrime(digit) == 0){
			for (long long k = 2; k <= digit; k++){
				if (digit%k == 0){
					arr[i - 2] = k;
					break;
				}
			}
		}
		else{
			return 0;
		}
	}
	printf("%s ", base);
	for (int i = 0; i < 9; i++){
		printf("%d ", arr[i]);
	}
	return 1;
}
int main() {
	scanf("%d", &T);
	for (int i = 1; i <=T; i++){
		printf("Case #%d:\n", i);
		cin >> N >> J;
		//=======
		unsigned int n = 1 << (N - 1);
		while (J != 0){
			if (n & 1){
				print_binary(n, base);
				
				if (isjam() == 1){
					putchar('\n');
					J--;
				}
			}
			n++;
		}
	}
	return 0;
}