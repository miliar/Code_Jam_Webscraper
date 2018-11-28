#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>

using std::string;
using std::vector;


int main()
{
	int T;
	std::cin >> T;

	int N;

	for(int round = 1; round <= T; ++round)
	{
		std::cin >> N;
		std::vector<int> v(10, 0);
		if(N == 0)
		{
			std::cout << "Case #" << round << ": " << "INSOMNIA" << std::endl;
			continue;
		}
		int mul = 1;
		while(true) 
		{
			int num = mul * N;
			while(num >= 10) {
				v[num % 10] = 1;
				num /= 10;
			}
			v[num] = 1;
			int flag = 1;
			for(int ii = 0; ii < 10; ii++)
			{
				if(v[ii] == 0) 
				{
					flag = 0;
					break;
				}
			}
			if(flag) 
			{
				std::cout << "Case #" << round << ": " << mul * N << std::endl;
				break;
			}
			else
			{
				mul++;
			}
		}

	}

	return 0;
}
