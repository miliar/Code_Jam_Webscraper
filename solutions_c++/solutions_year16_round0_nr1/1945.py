#include <iostream>
#include <vector>

std::vector<bool> digits(10);
inline void initDigits()
{
	for (int i = 0; i < 10; i++) {
		digits[i] = false;
	}
}
inline void setDigit(const int digit) {
	digits[digit] = true;
}
inline bool checkDigits()
{
	for (int i = 0; i < 10; i++) {
		if (digits[i] == false) { return false;  }
	}
	return true;
}
inline int countDigits() {
	int result = 0;
	for (int i = 0; i < 10; i++) {
		if (digits[i]) { result++;  }
	}
	return result;
}
inline void setDigitsForNum(const int num) {
	int div = num;
	while (div > 0) {
		int mod = div % 10; div = div / 10;
		setDigit(mod);
	}
}

int countSheep(const int num)
{
	initDigits();
	int n = num; int i = 1;
	if (n == 0) { return -1; }
	while (n > 0) {
		setDigitsForNum(n);
		if (checkDigits()) { /* std::cout << i << std::endl; */  return n; }
		i++; n = i*num;
	}
	return -1;
}

int main()
{
	int NumTests = 0;
	std::cin >> NumTests;
	for (int i = 1; i <= NumTests; i++) {
		int N = 0;
		std::cin >> N;
		int result = countSheep(N);
		std::cout << "Case #" << i << ": ";
		if (result > 0) {
			 std::cout << result;
		} else {
			std::cout << "INSOMNIA";
		}
		std::cout << std::endl;
	}
	/*
	for (int i = 0; i < 1000000; i++) {
		int result = countSheep(i);
		std::cout << "Case #" << i << ": " << result << std::endl;
		//if (result == -1) { std::cout << "Check!" << std::endl;  return -1; }
	}
	*/
	return 0;
}