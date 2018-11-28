#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <iterator>
#include <cassert>

template <typename BidirIt>
bool isPalindrome(BidirIt begin, BidirIt end)
{
	--end; // Point to the last element, not beyond the end
	while (begin != end)
	{
		if (*begin != *end)
			return false;

		if (++begin == end)
			break;

		--end;
	}

	return true;
}

bool isPalindrome(unsigned i)
{
	std::ostringstream sout;
	sout << i;
	const auto s = sout.str();
	return isPalindrome(s.begin(), s.end());
}

void test(const unsigned id)
{
	unsigned BEGIN, END;
	std::cin >> BEGIN >> END;
	unsigned fairSquareCount = 0;

	for (unsigned i = sqrt(BEGIN); i*i <= END; ++i)
	{
		const unsigned square = i*i;
		if (isPalindrome(i) && isPalindrome(square) && BEGIN <= square && square <= END)
			++fairSquareCount;
	}

	std::cout << "Case #" << id << ": " << fairSquareCount << std::endl;
}

int main()
{
	unsigned testCount;
	std::cin >> testCount;

	for (unsigned i = 0; i < testCount; ++i)
		test(i+1);

	return 0;
}
