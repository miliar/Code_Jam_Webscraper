#include <iostream>
#include <cmath>

using namespace std;

static bool
is_palindrome(unsigned long long number)
{
	//unsigned long long orig = number;
	//cout << "Is " << number << " pal?" << endl;
	while (number > 0) {
		unsigned int ndigits = log(number)/log(10) + 1;
		//cout << number << " has " << ndigits << " digits" << endl;
		if (ndigits == 1) {
			//cout << orig << " pal by one digit" << endl;
			return true;
		}
		unsigned int ppow = pow(10.0, (int)ndigits - 1);
		unsigned int first = floor(number / ppow);
		unsigned int last = number % 10;
		//cout << first << " ... " << last << endl;
		if (first != last) {
			//cout << orig << " not pal" << endl;
			return false;
		}
		if (ppow / 10 > 0)
			number %= ppow / 10;
		number = floor(number / 10);
	}
	//cout << orig << " is pal" << endl;
	return true;
}

static inline bool
is_square(unsigned long long number)
{
	unsigned long long sroot = sqrt(number);
	//if ((sroot * sroot) == number)
		//cout << number << " is square" << endl;
	return (sroot * sroot) == number;
}

/*
static bool
is_prime(unsigned long long number)
{
	for (int i = 2; i < sqrt(number); i++) {
		if (number % i)
			return false;
	}

	return true;
}
*/

static unsigned long long
fair_and_square(unsigned long long start, unsigned long long end)
{
	unsigned long long count = 0;
	for (unsigned long long n = start; n <= end; n++)
		if (is_palindrome(n) && is_square(n) && is_palindrome(sqrt(n)))
			count++;
	return count;
}

int
main(int argc, const char *argv[])
{
	int ncases;

	cin >> ncases;
	for (int _case = 0; _case < ncases; _case++) {
		unsigned long long start, end;
		cin >> start >> end;
		//cout << "[" << start << ", " << end << "]" << endl;
		unsigned long long count = fair_and_square(start, end);
		cout << "Case #" << _case + 1 << ": " << count << endl;
	}
	return 0;
}
