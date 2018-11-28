#include <boost/range/irange.hpp>
#include <cstdio>
#include <iostream>

using namespace std;
using namespace boost;

bool done(short &present_digits, const long long &num)
{
	auto s = to_string(num);
	for (auto c : s)
		present_digits |= 1 << int(c - '0');

	return __builtin_popcount(present_digits) == 10;
}

int main()
{
    int t;
    scanf("%d", &t);

    for (int i : irange(1, t + 1))
   	{
   		long long n;
   		scanf("%lld", &n);

 		const int TESTS = 100'000;
 		short present_digits = 0;

 		int ind = 0;
 		while (!done(present_digits, n * (ind + 1)) and ++ind < TESTS);

 		if (ind >= TESTS)
 			printf("Case #%d: INSOMNIA\n", i);
 		else
 			printf("Case #%d: %lld\n", i, n * (ind + 1));
   	}
}