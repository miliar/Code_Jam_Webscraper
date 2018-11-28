#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
using namespace std;

bool isPalindrome(unsigned long long n, unsigned int base)
{
	if (base == 0) return false;
	if (n == 0) return true;

	std::vector<unsigned int> digitList;
	while (n > 0) {
		digitList.push_back(n % base);
		n /= base;
	}

	// compare digits at each end to see if it's a palindrome
	bool isPalindrome = true;
	const size_t numDigits = digitList.size();
	for (size_t i = 0; isPalindrome && (i < (numDigits / 2)); ++i)
	{
		// 7: [0,6], [1,5], [2,4] - no need to test [3,3]
		// 6: [0,5], [1,4], [2,3]
		if (digitList[i] != digitList[numDigits - (i + 1)]) isPalindrome = false;
	}

	return isPalindrome;
}

void main() {
	ifstream in("D:\\fs1.txt");
	ofstream out("D:\\fs1out.txt");
	int numRanges;
	in >> numRanges;
	for (int i = 1; i <= numRanges; ++i) {
		unsigned long long start;
		unsigned long long end;
		in >> start >> end;
		int startRange = ceil(sqrtl(start));
		int endRange = floor(sqrtl(end));
		unsigned long long numberOfFairSquare = 0;
		for (unsigned long long j = startRange; j <= endRange; ++j) {
			if (isPalindrome(j, 10) && isPalindrome(j * j, 10)) {
				++numberOfFairSquare;
			}
		}
		out << "Case #" << i << ": " << numberOfFairSquare << endl;
	}

	in.close();
	out.close();
}


