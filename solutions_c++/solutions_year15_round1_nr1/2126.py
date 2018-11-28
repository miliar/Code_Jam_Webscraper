
#include <cstdio>
#include <iostream>
#include <vector>

void mushroom_monster ()
{
	int tcNum;
	std::cin >> tcNum;

	for (int tc = 0; tc < tcNum; ++tc)
	{
		int N;
		std::cin >> N;

		std::vector<int> ms;
		for (int i =0; i < N; ++i)
		{
			int m;
			std::cin >> m;
			ms.push_back(m);
		}
		int Y = 0;
		int maxDecrease = 0;
		for (unsigned int i = 1; i < ms.size(); ++i)
		{
			int dec = ms[i-1] - ms[i];
			if (dec > 0)
			{
				Y += dec;
				if (maxDecrease < dec)
				{
					maxDecrease = dec;
				}
			}
		}

		int Z = 0;
		int prev = ms[0];
		for (unsigned int i = 1; i < ms.size(); ++i)
		{
			if (prev > maxDecrease)
			{
				Z += maxDecrease;
			} else {
				Z += prev;
			}
			prev = ms[i];
		}
		printf ("Case #%d: %d %d\n", tc+1, Y, Z);

	}


}
