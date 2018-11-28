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

		std::vector<int> v(N, 0);

		for(int kk = 0; kk < N; ++kk) 
		{
			std::cin >> v[kk];
		}

		std::string str = "";

		while(true)
		{
			int max = 0;
			int max2 = 0;
			int idx = -1;
			int idx2 = -1;

			std::vector<int> v2(N ,0);
			int idxof1 = -1;
			for(int jj = 0; N > 2 && jj < N; ++jj)
			{
				v2[jj] = v[jj];
				if(v2[jj] == 1)
				{
					idxof1 = jj;
				}
			}
			std::sort(v2.begin(), v2.end(), std::greater<int>());
			if(N > 2 && v2[0] == 1 && v2[1] == 1 && v2[2] == 1)
			{
				if((N > 3 && v2[3] == 0) || (N == 3))
				{
					char ch = 'A' + idxof1;
					str += " ";
					str += ch;
					v[idxof1]--;
					continue;
				}
			}

			for(int jj = 0; jj < N; ++jj)
			{
				if(v[jj] > 0 && v[jj] > max) 
				{
					max = v[jj];
					idx = jj;
				}
			}
			if(max == 0) 
			{
				std::cout << "Case #" << round << ":" << str << std::endl;
				break;
			}
			for(int jj = 0; jj < N; ++jj)
			{
				if(jj == idx)
				{
					continue;
				}
				if(v[jj] > 0 && v[jj] > max2) 
				{
					max2 = v[jj];
					idx2 = jj;
				}
			}

			if(max2 == 0) 
			{
				char ch = 'A' + idx;
				str += " ";
				str += ch;
				std::cout << "Case #" << round << ":" << str << std::endl;
				break;
			}
			char ch = 'A' + idx;
			char ch2 = 'A' + idx2;
			str += " ";
			str += ch;
			str += ch2;
			v[idx]--;
			v[idx2]--;
		}

	}

	return 0;
}
