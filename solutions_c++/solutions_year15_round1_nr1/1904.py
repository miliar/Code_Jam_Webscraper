#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

int main(int argc, char* argv[])
{
	int numCases;
	std::cin >> numCases;
	for (int i=0; i<numCases; i++)
	{
		int N;
		std::cin >> N;
		std::vector<int> values;
		int maxValue = 0;
		for (int i=0; i<N; ++i)
		{
			int m;
			std::cin >> m;
			values.push_back(m);
			if (m > maxValue) maxValue = m;
		}
		
		//Algorithm 1
		long y = 0;
		for (int i=1; i<N; ++i)
		{
			if (values[i] < values[i-1])
				y += (values[i-1]-values[i]);
		}
		//Algorithm 2
		long z = 0;
		int rate = 0;
		for (int i=0; i<N-1; ++i)
		{
			if ((values[i]-values[i+1])> rate)
				rate = values[i]-values[i+1];
		}
		for (int i=0; i<N-1; ++i)
		{
			if (values[i] < rate)
				z += values[i];
			else
				z += rate;
		}

		std::cout << "Case #" << (i+1) << ": " << y << " " << z << std::endl;
	}
	return 0;
}
