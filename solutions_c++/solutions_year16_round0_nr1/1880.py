#include <iostream>

using namespace std;

void clearDigits (int num[]);
void updateCount(unsigned long int N, int num[], int *count);

int main () {
	int T, mul, count, i, j;
	long unsigned int num, N;
	int digits[10] = {0,0,0,0,0,0,0,0,0,0};
	
	
	cin >> T;
	
	for (i=1;i<=T;i++) {
		cin >> N;
		
		if (N == 0) {
			cout << "Case #" << i << ": INSOMNIA" << endl;
			continue;
		}
		
		clearDigits(digits);
		count = 0;
		mul = 1;
		num = N;
		while (count < 10) {
			updateCount(num, digits, &count);
			//cout << "num " << num << " mul " << mul << " count " << count << endl;
			mul++;
			num = N*mul;
		}
		
		cout << "Case #" << i << ": " << num-N << endl; 
	}
	
	return 0;
}

void clearDigits (int num[]) {
	int i;
	for (i=0;i<10;i++) {
		num[i] = 0;
	}
	
	return;
}

void updateCount(unsigned long int N, int num[], int *count) {
	int rem;
	while (N!=0) {
		rem = N%10;
		N = N/10;
		if (num[rem] == 0) {
			(*count)++;
			num[rem] = 1;
		}
	}
	
	return;
}
