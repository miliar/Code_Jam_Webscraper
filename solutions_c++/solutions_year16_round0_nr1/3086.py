#include <iostream>
#include <fstream>
#include <limits>

typedef unsigned long long Number;

Number find_n(Number n)
{
	if (n == 0)
		return 0;
	int k = 0;
	bool found[10] = {};
	int left = 10;
	while(n * k <= std::numeric_limits<Number>::max() - n)
	{
		++k;
		Number t = n * k;
		while(t > 0)
		{
			int digit = t % 10;
			if(!found[digit])
			{
				found[digit] = true;
				--left;
				if (left == 0)
					return n * k;
			}
			t /= 10;
		}
	}
	return 0;
}
int main()
{
	int n;
	std::ifstream is("L:/A-small-attempt0.in");
	is >> n;
	int c = 1;
	while(n-- > 0)
	{
		Number b;
		is >> b;
		Number res = find_n(b);
		std::cout << "Case #" << c++ << ": ";
		if(res == 0)
			std::cout << "INSOMNIA" << std::endl;
		else
			std::cout << res << std::endl;
	}
	return 0;
}