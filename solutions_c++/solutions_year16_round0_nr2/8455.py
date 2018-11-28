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

	std::string str;

	for(int round = 1; round <= T; ++round)
	{
		std::cin >> str;
		int N = 0;
		while(true) 
		{
			int len = str.length() - 1;
			while(str[len] == '+') 
			{
				len--;
				if (len == -1)
				{
					break;
				}
			}
			if(len == -1) 
			{
				std::cout << "Case #" << round << ": " << N << std::endl;
				break;
			}

			std::vector<char> v(len + 1, 0);

			int flag = 1;
			for(int i = 0; i < len + 1; i++)
			{
				v[i] = str[i];
				if(str[i] == '+')
				{
					flag = 0;
				}
			}
		
			if(flag) 
			{
				std::cout << "Case #" << round << ": " << N + 1 << std::endl;
				break;
			}

			if(v[0] == '-')
			{
				str = std::string(v.begin(), v.end());
				for(int i = 0; i < len + 1; i++)
				{
					if(v[len - i] == '+')
					{	
						str[i] = '-';
					}
					else
					{
						str[i] = '+';
					}

				}
				
				N++;
				continue;
			}
	
			for(int i = 0; i < len + 1; i++)
			{
				if(v[i] == '+')
				{	
					v[i] = '-';
				}
				else
				{
					break;
				}

			}

			str = std::string(v.begin(), v.end());
			N++;
		}

	}

	return 0;
}
