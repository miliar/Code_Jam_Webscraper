#include <iostream>
int main()
{
	std::ios_base::sync_with_stdio(false);
	//std::cin.tie(false);

	int t;
	std::cin >> t;
	for(int i = 0;i < t;++ i)
	{
		std::string input;
		std::cin >> input;
		int res = 0;

		if(input.size() == 1 and input[0] == '+')
		{
			res = 0;
		}
		else if(input.size() == 1 and input[0] == '-')
		{
			res = 1;
		}
		else
		{
			bool upTillNow = (input[0] == '+');
			for(int i = 1;i < input.size();++ i)
			{
				if(upTillNow and input[i] == '-')
				{
					res ++;
					upTillNow = !upTillNow;
				}
				else if(!upTillNow and input[i] == '+')
				{
					res ++;
					upTillNow = !upTillNow;
				}
			}
			if(!upTillNow)
				res ++;
		}

		std::cout << "Case #" << i+1 << ": " << res << '\n';
	}

	return 0;
}
