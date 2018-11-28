#include <iostream>
using namespace std;

inline long long sqr(long long number) {
	return number * number;
}

long long reverse(long long number) {
	long long rev = 0;
	while (number) {
		rev = rev * 10 + number % 10;
		number /= 10;
	}
	return rev;
}

int main() {
	int T;
	cin >> T;
	for (int cas = 1; cas <= T; ++cas) {
		long long A, B, count = 0;
		cin >> A >> B;
		for (int i = 1; i <= 9; ++i) {
			int number = sqr(i);
			if (A <= number && number <= B && reverse(number) == number) {++count;}
		}
		for (int left = 1; left <= 9; ++left) {
			int right = left;
			long long number = sqr(right * 10 + left);
			if (A <= number && number <= B && reverse(number) == number) {
				++count;
			}
			for (int mid = 0; mid < 9; ++mid) {
				int number = sqr(right * 100 + mid * 10 + left);
				if (A <= number && number <= B && reverse(number) == number) {
					++count;
				}
			}
		}
		for (int left = 10; left <= 99; ++left) {
			int right = reverse(left);
			long long number = sqr(right * 100 + left);
			if (A <= number && number <= B && reverse(number) == number) {
				++count;
			}
			for (int mid = 0; mid < 9; ++mid) {
				int number = sqr(right * 1000 + mid * 100 + left);
				if (A <= number && number <= B && reverse(number) == number) {
					++count;
				}
			}
		}
		for (int left = 100; left <= 999; ++left) {
			int right = reverse(left);
			long long number = sqr(right * 1000 + left);
			if (A <= number && number <= B && reverse(number) == number) {
				++count;
			}
			for (int mid = 0; mid < 9; ++mid) {
				int number = sqr(right * 10000 + mid * 1000 + left);
				if (A <= number && number <= B && reverse(number) == number) {
					++count;
				}
			}
		}
		cout << "Case #" << cas << ": " << count << endl;
	}
	return 0;
}
