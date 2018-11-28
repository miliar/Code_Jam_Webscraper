/**
 * @name Counting Sheep
 */
#include <iostream>
#include <string>
#include <cassert>
using namespace std;

const uint32_t DIGIT_FLAGS_ALL = 0x3ff;

uint32_t get_digit_flags(uint32_t n)
{
	// Bits 0 to 9 indicate whether that digit has been found
	uint32_t digit_flags = 0;

	while (n != 0)
	{
		digit_flags |= 1 << (n % 10);
		n /= 10;
	}

	return digit_flags;
}

uint32_t count_sleep(uint32_t n)
{
	assert(n != 0);

	uint32_t cur = 0;
	uint32_t digit_flags = 0;

	while (digit_flags != DIGIT_FLAGS_ALL)
	{
		cur += n;
		digit_flags |= get_digit_flags(cur);
	}

	return cur;
}

/**
 * We can easily show that the only INSOMNIA case is n = 0:
 *
 *  - For every natural n, 0n = 0
 *
 *  - The sequence of numbers counted can be generated with
 *    the following function: { f(0) = N, f(i) = f(i - 1) + N }
 *
 *  - Any digit addition with carry will result in a number
 *    between 0 and 19, so the only possible carry value is 1.
 *
 *  - Following from the last two premises, the position occupied by
 *    the first zero to the left of the leftmost significant digit
 *    will be incremented to 1 due to a carry from the number to
 *    the right. Therefore, this position will cycle through all the
 *    posible digits.
 *    
 *  - From this, it follows that every non-zero number will always
 *    generate all the possible digits.
 */
string solve(uint32_t n)
{
	return (n == 0) ? "INSOMNIA" : to_string(count_sleep(n));
}

int main()
{
	size_t num_cases;
	cin >> num_cases;

	for (size_t c = 0; c < num_cases; ++c)
	{
		uint32_t n;
		cin >> n;

		cout << "Case #" << (c + 1) << ": " << solve(n) << endl;
	}
}
