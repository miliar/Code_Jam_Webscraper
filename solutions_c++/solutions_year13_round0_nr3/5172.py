
#include <iostream>
#include <string>
#include <list>
#include <stack>

__int64 countFairSquare(__int64 lowerBound, __int64 upperBound);
bool isPalindrome(__int64 number);
int countDigits(__int64 number);
__int64 sqrt(__int64 x);
__int64 tenExp(int x);
__int64 reverse(__int64 x);

#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))

int main() {
	std::string line;

	int numTestCases = 0;
	std::getline(std::cin, line);
	sscanf(line.c_str(), "%d", &numTestCases);

	for(int testCase = 0; testCase < numTestCases; testCase++) {
		__int64 lowerBound = -1, upperBound = -1;
		std::getline(std::cin, line);
		sscanf(line.c_str(), "%I64d %I64d", &lowerBound, &upperBound);

		std::cout << "Case #" << (testCase + 1) << ": " << countFairSquare(lowerBound, upperBound) << std::endl;
	}
}

__int64 countFairSquare(__int64 lowerBound, __int64 upperBound) {
	__int64 counter = 0;

	__int64 begin = sqrt(lowerBound);
	__int64 end = sqrt(upperBound);

	for(int digits = countDigits(begin); digits <= countDigits(end); digits++) {
		__int64 word = tenExp(digits / 2);

		__int64 lowerHigh = tenExp((digits - 1) / 2);
		__int64 upperHigh = tenExp((digits - 1) / 2 + 1) - 1;
		if(digits == countDigits(begin)) lowerHigh = begin / word;
		if(digits == countDigits(end)) upperHigh = end / word;

		for(__int64 high = lowerHigh; high <= upperHigh; high++) {
			__int64 low = 0;

			if(digits % 2 == 0) {
				low = reverse(high);
			} else {
				low = reverse(high / 10);
			}
			__int64 i = high * word + low;

			if(i * i >= lowerBound && i * i <= upperBound &&
				isPalindrome(i * i)) {
					counter++;
			}
		}
	}

	return counter;
}

bool isPalindrome(__int64 number) {
	int digits = countDigits(number);

	std::stack<int> s;
	for(int i = 0; i < digits / 2; i++) {
		s.push(number % 10);
		number /= 10;
	}
	if(digits % 2 == 1) {
		number /= 10;
	}
	for(int i = 0; i < digits / 2; i++) {
		if(number % 10 != s.top()) {
			return false;
		}
		s.pop();
		number /= 10;
	}

	return true;
}

int countDigits(__int64 number) {
	int digits = 0;
	
	__int64 tmp = number;
	while(tmp > 0) {
		tmp /= 10;
		digits++;
	}

	return digits;
}

__int64 sqrt(__int64 x) {
	__int64 y = (__int64)sqrt((double)x) - 1i64;

	while(y * y <= x) {
		y++;
	}

	return y - 1;
}

__int64 tenExp(int x) {
	__int64 y = 1;
	for(int i = 0; i < x; i++) {
		y *= 10;
	}
	return y;
}

__int64 reverse(__int64 x) {
	int y = 0;

	while(x > 0) {
		y *= 10;
		y += (x % 10);
		x /= 10;
	}

	return y;
}