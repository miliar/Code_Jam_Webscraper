#include <iostream>
#include <string>

int main()
{
	int testcases;
	std::cin >> testcases;
	for (int x = 1; x <= testcases; ++x)
	{
		int s_max;
		std::cin >> s_max;
		std::string shynessStr;
		std::cin >> shynessStr;
		//std::cout << shynessStr << std::endl;
		
		int y = 0;
		int total = shynessStr[0]-'0';
		for (int i = 1; i < shynessStr.length(); ++i)
		{
			int val = shynessStr[i]-'0';
			//std::cout << "I: " << i << " COUNT: " << val << " TOTAL : " << total << " Y: " << y << std::endl;
			if (val == 0) continue;
			if (total < i)
			{
				y += (i-total);
			}
			total += val + y;
		}
		std::cout << "Case #" << x << ": " << y << std::endl;
	}
}