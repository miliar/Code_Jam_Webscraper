#include <iostream>

using namespace::std;

#define INSOMNIA	10000

int digits[10] = {0};
int number_of_digits_encountered = 0;

void zero_digits() {
	for(int i=0; i<10; i++) {
		digits[i] = 0;
	}
}

void count_digits(long long n) {
	int reminder = 0;
	while (n!=0) {
		reminder = n % 10;
		if(digits[reminder] == 0) {
			// keep track of number of digits globally
			// to save us from scanning the digits
			// table
			number_of_digits_encountered++;
		}
		digits[reminder] = 1;
		n/=10;
	}
}

void print_output(int T, long long counter) {
	if(counter == -1)
		cout << "Case #" << T << ": INSOMNIA" << endl;
	else
	 	cout << "Case #" << T << ": " << counter << endl;
}

long long count_sheep() {
	long N = 0;
	long long named_number = 0;

	cin >> N;

	zero_digits();
	number_of_digits_encountered = 0;

	//known cases of insomnia.
	if (N==0)
		return -1;

	for(long i=1;;i++) {
		named_number = i*N;
		count_digits(named_number);

		if (number_of_digits_encountered == 10)
			return named_number;

		//this is redundant .... ?
		if(i > INSOMNIA)
			return -1;
	}
}

int main() {
	int T;
	long long result = 0;

	cin >> T;
	for(int t=0; t<T; t++) {
		result = count_sheep();
		print_output(t+1, result);
	}
}

/*
void scan_small_dataset_for_potential_insomniacs() {
	for (int N=0; N<=200; N++) {
		if (count_sheep(N)==-1) {
			cout << N << endl;
		}
	}
}

void scan_large_dataset_for_potential_insomniacs() {
	for (int N=0; N<=1000000; N++) {
		if (count_sheep(N)==-1) {
			cout << N << endl;
		}
	}
}
*/
