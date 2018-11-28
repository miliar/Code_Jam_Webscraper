#include <cstdio>
#include <iostream>
#include <vector>
#include <assert.h>
#include <algorithm>
#include <stack>

#define getchar_custom _fgetc_nolock

char c;

template <typename T>
inline T read_custom() {

	c = getchar_custom(stdin);

	while (c<'0' || c>'9')
	{
		c = getchar_custom(stdin);
	}

	T returnValue = 0;
	while (c >= '0' && c <= '9') {
		returnValue = (returnValue << 3) + (returnValue << 1) + c - 48;
		c = getchar_custom(stdin);
	}

	return returnValue;
}

long long GCD(long long a, long long b)
{
	long long x;

	do
	{
		x = b;
		b = a % b;
		a = x;
	} while (b);

	return a; 
}

int generation_solve(long long left, long long right, int* total_generation) {

	int generation = 0;

	while (generation > -1 && left < right) {
		generation += 1;
		left *= 2;

		long long gcd = GCD(left, right);
		left /= gcd;
		right /= gcd;

		if ((right != 1) && ((right % 2) > 0 || ((right > 3) && right % 4 != 0))) {
			return -1;
		}

		if (left > right) {
			long long rest = left - right;
			long long rest_m = right;
			long long local_gcd = GCD(rest, rest_m);

			rest_m /= local_gcd;
			rest /= local_gcd;

			int local_generations = generation_solve(rest, rest_m, total_generation);

			if (local_generations > -1) {
				*total_generation += generation;
				return generation;
			} else {
				return -1;
			}
		}

	}

	*total_generation += generation;

	return generation;

}

int main() {

	int testCasesNo = read_custom<int>();

	for (int caseNo = 1; caseNo <= testCasesNo; caseNo++) {

		long long l = read_custom<long long>();
		long long m = read_custom<long long>();

		int total_generation = 0;
		int generation = generation_solve(l, m, &total_generation);
			

		if (generation > 0 && generation <= 40 && total_generation <= 40)
		{
			std::cout << "Case #" << caseNo << ": " << generation << std::endl;
		}
		else 
		{
			std::cout << "Case #" << caseNo << ": impossible" << std::endl;
		}

	}


}