#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>

int calculateMinTime(std::vector<int> values, int specialMinutes)
{
	sort(values.begin(), values.end(), std::greater<int>());
	if (values[0] <= 3) return (values[0] + specialMinutes);

	std::vector<int> values2 = values;
	switch (values[0])
	{
	case 9:
		//Option 1: split 6-3
		values[0] = 6;
		values.push_back(3);
		//Option 2: split 5-4
		values2[0] = 5;
		values2.push_back(4);
		return std::min(9 + specialMinutes, std::min(calculateMinTime(values, specialMinutes+1), calculateMinTime(values2, specialMinutes+1)));
		break;
	case 8: //split 4-4
		values[0] = 4;
		values.push_back(4);
		return std::min(8 + specialMinutes, calculateMinTime(values, specialMinutes+1));
		break;
	case 7: //split 4-3
		values[0] = 4;
		values.push_back(3);
		return std::min(7 + specialMinutes, calculateMinTime(values, specialMinutes+1));
		break;
	case 6: //split 3-3
		values[0] = 3;
		values.push_back(3);
		return std::min(6 + specialMinutes, calculateMinTime(values, specialMinutes+1));
		break;
	case 5: //split 3-2
		values[0] = 3;
		values.push_back(2);
		return std::min(5 + specialMinutes, calculateMinTime(values, specialMinutes+1));
		break;
	case 4: //split 2-2
		values[0] = 2;
		values.push_back(2);
		return std::min(4 + specialMinutes, calculateMinTime(values, specialMinutes+1));
		break;
	}
}

int main(int argc, char* argv[])
{
	int numCases;
	std::cin >> numCases;
	for (int i=0; i<numCases; i++)
	{
		std::vector<int> values;
		int D;
		std::cin >> D;
		for (int j=0; j<D; j++)
		{
			int Dj;
			std::cin >> Dj;
			values.push_back(Dj);
		}

		int minTime = calculateMinTime(values, 0);

		std::cout << "Case #" << (i+1) << ": " << minTime << std::endl;

	}
	return 0;
}
