// GoogleCodeJam2015.cpp : 定義主控台應用程式的進入點。
//

#include "stdafx.h"
#include <iostream>
#include <string>

void A()
{
	int T = 0;
	std::cin >> T;

	for(int t=1; t<=T; ++t)
	{
		int s_max = 0;
		std::string s;
		std::cin >> s_max >> s;

		int invites = 0;
		int clapping = 0;

		for(int i=0; i<s.length(); ++i)
		{
			int p = s[i] - '0';

			if(i==0)
			{
				clapping = p;
				continue;
			}

			if(clapping >= i)
			{
				clapping += p;
				continue;
			}
			else
			{
				invites += (i-clapping);
				clapping += p + (i-clapping);
			}
		}
		
		std::cout << "Case #" << t << ": " << invites << std::endl;
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	A();
	return 0;
}

