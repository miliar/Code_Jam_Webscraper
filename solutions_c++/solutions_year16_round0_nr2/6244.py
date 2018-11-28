#include <stdio.h>
#include <iostream>
#include <string>

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	std::ios_base::sync_with_stdio(0); std::cin.tie(0);

	std::string tempString;
	std::getline(std::cin, tempString);
	int T;
	T = atoi(tempString.c_str());

	int index = 0;
	while (T--)
	{
		index++;
		std::string S;
		std::getline(std::cin, S);

		int finalResult = 0;		
		char preState = S.at(0);
		for (int i = 0; i < S.length(); i++)
		{			
			if (S.at(i) != preState)
			{
				finalResult++;
			}
			preState = S.at(i);
		}
		if (S.at(S.length() - 1) == '-')
		{
			finalResult++;
		}

		
		
		std::cout << "Case #" << index << ": " << finalResult  << std::endl;	

	}
	return 0;
}