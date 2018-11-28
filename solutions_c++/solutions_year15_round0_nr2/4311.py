#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;
int main()
{

	std::ifstream infile("B-small-attempt6.in");

	ofstream myfile("infinite.out");
	int tests;
	infile >> tests;
	tests++;
	for (int t = 1; t < tests; t++)
	{
		int d;
		infile >> d;
		vector <int> plates;
		for (int i = 0; i < d; i++)
		{
			int p;
			infile >> p;
			plates.push_back(p);
		}

		sort(plates.rbegin(), plates.rend());
		int max = plates[0];
		int minutes = 0;
		int minMax= plates[0];
		int i = 0;
		while (plates[0] > 1)
		{
			if (plates[0] > 8)
			{
				if (plates.size() > 1)
				{
					if (plates[1] < 4 || plates[1] == 6)
					{
						int temp = plates[0] / 3;
						plates.push_back(temp);
						plates.push_back(plates[0] - temp);
						plates.erase(plates.begin() + 0);
						sort(plates.rbegin(), plates.rend());
						i++;
						if (plates[0] + i < max)
						{
							max = plates[0] + i;
							minMax = max;
						}
						else
						{
							if (max > minMax)
							{
								break;
							}
						}
					}
				}
				else
				{
					int temp = plates[0] / 3;
					plates.push_back(temp);
					plates.push_back(plates[0] - temp);
					plates.erase(plates.begin() + 0);
					sort(plates.rbegin(), plates.rend());
					i++;
					if (plates[0] + i < max)
					{
						max = plates[0] + i;
						minMax = max;
					}
					else
					{
						if (max > minMax)
						{
							break;
						}
					}
				}
			}
			int temp = plates[0] / 2;
			plates.push_back(temp);
			plates.push_back(plates[0] - temp);
			plates.erase(plates.begin() + 0);
			sort(plates.rbegin(), plates.rend());
			i++;
			if (plates[0] + i < max)
			{
				max = plates[0] + i;
				minMax = max;
			}
			else
			{
				if (max > minMax)
				{
					break;
				}
			}
		}
		myfile << "Case #" << t << ": " << max << endl;
	}
	myfile.close();
	infile.close();
	return 0;
}
