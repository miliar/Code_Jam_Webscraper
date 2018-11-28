#include <iostream>
#include <cmath>

using namespace std;

unsigned long long int isDivisible (unsigned long long int n);
unsigned long long int computeNum (int arr[], int size, int base);
int computeDiv (int arr[], int size, int base, unsigned long long int divisor);
int increase (int arr[], int level, int size, int limit);
void initArr (int arr[], int size);
void initDivisArr (int arr[], int size, int base);

int main () {
	int T, N, J, divisArrSize, count, res, divisorFound, i, j;
	unsigned long long int divisor;
	unsigned long long int divisors[9];
	unsigned long long int numbers[9];
	int digits[32];
	int divisArr[16];
	
	cin >> T;
	
	for (i = 1; i <= T; i++) {
		cin >> N >> J;
		divisArrSize = N/2;
		initArr(digits, N);
		count = 0;
		
		//increase(digits, 0, N);
		cout << "Case #" << i << ":" << endl;
		do {
			/*
			cout << "checking Num: ";
			for (j=N-1;j>=0;j--) {
				cout << digits[j];
			}
			cout << endl;
			*/
			
			for (j = 2; j <=10; j++) {
				initDivisArr(divisArr, divisArrSize, j);
				divisorFound = 0;
				do {
					divisor = computeNum(divisArr, divisArrSize, j);
					res = computeDiv(digits, N, j, divisor);
					if (res == 1) {
						divisors[j-2] = divisor;
						divisorFound = 1;
						break;
					}
				} while (increase(divisArr, 0, divisArrSize, j-1) && divisor < 10000);
				
				if (divisorFound != 1) {
					break;
				}
			}
			
			if (j == 11) {
				count++;
				for (j=N-1;j>=0;j--) {
					cout << digits[j];
				}
				for (j=0;j<9;j++) {
					//cout << " "<< j+2 << ":" << numbers[j] << ":" << divisors[j];
					cout << " " << divisors[j];
				}
				cout << endl;
			}
			
		} while (increase(digits, 1, N, 1) && count < J);
	}
	
	return 0;
}

void initArr (int arr[], int size) {
	int i;
	for (i=0;i<size;i++) {
		arr[i] = 0;
	}
	arr[0] = 1;
	arr[size-1] = 1;
}

void initDivisArr (int arr[], int size, int base) {
	int i;
	for (i=0;i<size;i++) {
		arr[i] = 0;
	}
	if (base > 2) {
		arr[0] = 2;
	} else {
		arr[1] = 1;
	}
}

int increase (int arr[], int level, int size, int limit) {
	if (arr[level] == limit) {
		if (level == size-1) {
			return 0;
		}
		arr[level] = 0;
		return increase(arr, level+1, size, limit);
	} else {
		arr[level]++;
		return 1;
	}
}

unsigned long long int computeNum (int arr[], int size, int base) {
	int i;
	unsigned long long int sum = 0, mul = 1;
	for (i = 0; i < size; i++) {
		sum += arr[i]*mul;
		mul *= base;
	}
	
	return sum;
}

int computeDiv (int arr[], int size, int base, unsigned long long int divisor) {
	int i;
	unsigned long long int rem = 0, posrem = 1;
	for (i=0;i<size;i++) {
		rem = (rem + posrem*arr[i])%divisor;
		posrem = (posrem*base)%divisor;
	}
	
	if (rem == 0) {
		return 1;
	} else {
		return 0;
	}
}

unsigned long long int isDivisible (unsigned long long int n) {
	unsigned long long int i;
	unsigned long long int sqrtNum = sqrt(n);
	
	//cout << "number " << n << " sqrt " << sqrtNum << endl;
	
	for (i=2;i<=sqrtNum;i++) {
		if (n%i == 0) {
			return i;
		}
	}
	
	return 0;
}
