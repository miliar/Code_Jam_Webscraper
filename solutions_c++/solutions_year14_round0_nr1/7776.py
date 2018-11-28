#include <iostream>
#include <vector>
#include <algorithm>

int main(int argc, char* argv[])
{
	int numCases;
	std::cin >> numCases;
	for (int i=0; i<numCases; i++)
	{
		std::vector<int> values;
		int line1, line2;
		std::cin >> line1;
		for (int j=1; j<=4; ++j)
		{
			int a, b, c, d;
			std::cin >> a >> b >> c >> d;
			if(line1==j)
			{
				values.push_back(a);
				values.push_back(b);
				values.push_back(c);
				values.push_back(d);
			}
		}
		std::cin >> line2;
		for (int j=1; j<=4; ++j)
		{
			int a, b, c, d;
			std::cin >> a >> b >> c >> d;
			if(line2==j)
			{
				values.push_back(a);
				values.push_back(b);
				values.push_back(c);
				values.push_back(d);
			}
		}
		sort(values.begin(), values.end());
		int repeated = 0;
		int lastValue = -1;
		int result = -1;
		std::vector<int>::iterator it;
		for (it=values.begin(); it!= values.end(); ++it)
		{
			if ((*it) == lastValue)
			{
				repeated++;
				result = (*it);
			}
			lastValue = (*it);
		}

		switch(repeated)
		{
		case 0:
			std::cout << "Case #" << (i+1) << ": " << "Volunteer cheated!" << std::endl;
			break;
		case 1:
			std::cout << "Case #" << (i+1) << ": " << result << std::endl;
			break;
		default:
			std::cout << "Case #" << (i+1) << ": " << "Bad magician!" << std::endl;
			break;
		}
	}
	return 0;
}
