#include<iostream>

using namespace std;

void get_digits(int *arr, int &digit_count, long long int num) {
	while(num > 0) {
		int digit = num % 10;
		if (arr[digit] == 0) {
			arr[digit] = 1;
			digit_count++;
		}
		num = num / 10;
	}
}

int main() {
	int T;
	cin >> T;
	for (int _ = 0; _ < T; _++) {
		int multiplier = 1;
		int digit_count = 0;
		int arr[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
		long long int N;
		cin >> N;
		if (N == 0)
			cout << "Case #" << _ + 1 << ": INSOMNIA" << endl;
		else {
			while(digit_count < 10) {
				get_digits(arr, digit_count, multiplier * N);
				multiplier++;
			}
			cout << "Case #" << _ + 1 << ": " << (multiplier - 1) * N << endl;
		}
	}
	return 1;
}
