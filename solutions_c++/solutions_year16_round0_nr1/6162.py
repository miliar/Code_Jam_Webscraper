#include <stdio.h>
#include <iostream>
#include <fstream>
#include <map>

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	std::ios_base::sync_with_stdio(0); std::cin.tie(0);

	int T;
	std::cin >> T;

	int index = 0;
	while (T--)
	{
		index++;
		int N;
		std::cin >> N;

		std::map<int, int> intMap;

		int i = 0;
		int preNum = -1;

		bool isLoop = false;
		int finalNumber = -1;
		while (true)
		{
			i++;
			int curNum = i * N;
			if (curNum != preNum)
			{
				int tempNum = curNum;
				while (tempNum > 0)
				{
					int du = tempNum % 10;
					int thuong = tempNum / 10;
					
					if (intMap.count(du) == 0)
					{
						intMap[du] = 1;
					}

					if (intMap.size() == 10)
					{
						break;
					}

					tempNum = thuong;
				}

				if (intMap.size() == 10)
				{
					finalNumber = curNum;
					break;
				}
			}
			else
			{
				isLoop = true;
				break;
			}

			preNum = curNum;
		}

		if (isLoop)
		{
			std::cout << "Case #" << index << ": INSOMNIA" << std::endl;
		}
		else
		{
			std::cout << "Case #" << index << ": " << finalNumber << std::endl;
		}
		

	}
	return 0;
}