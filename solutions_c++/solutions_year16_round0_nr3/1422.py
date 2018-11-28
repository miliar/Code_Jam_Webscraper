#include <fstream>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <queue>
#include <cstdint>
#include <unordered_map>
#include <map>
#include <unordered_set>
#include <functional>

using namespace std;
typedef long long ll;

int main()
{
	string fileName = "input.txt";
	ifstream file(fileName.c_str());

	ofstream outputfile;
	outputfile.open("Output.txt");

	string line;
	int T = 0, N,J, counter=0;
	ll result;

	vector<ll> numberofFlips;
	char prevChar;

	if (file.is_open())
	{
		getline(file, line);
		T = stoi(line);

		numberofFlips.resize(T);

		for (int i = 0; i < T; ++i)
		{
			getline(file, line);
			istringstream ss(line);
			counter = 0;

			ss >> N >> J;

			outputfile << "Case #" << i+1 << ":" << endl;

			for (int k = 2; k < 4; ++k)
			{
				for (int m = k+2; m < 27; ++m)
				{
					for (int n = m+2; n < 29; ++n)
					{
						if (counter == 500)
						{
							break;
						}

						string num(N, '0');
						num[0] = '1';
						num[1] = '1';
						num[30] = '1';
						num[31] = '1';

						num[k + 1] = '1';
						num[k] = '1';

						num[m + 1] = '1';
						num[m] = '1';

						num[n + 1] = '1';
						num[n] = '1';

						outputfile << num << " ";

						for (size_t b = 2; b < 11; b++)
						{
							outputfile << b + 1 << " ";
						}
						outputfile << endl;

						counter++;
					}
				}
				
			}

		}
	}
	
	file.close();

	outputfile.close();

	return 0;
}