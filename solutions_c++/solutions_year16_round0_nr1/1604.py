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
	string line;
	int T = 0, totalFoundDigits;
	ll N, currentNumber, tempNumber, result;

	bool foundDigits[10];
	vector<ll> lastSeenNumber;

	if (file.is_open())
	{
		getline(file, line);
		T = stoi(line);

		lastSeenNumber.resize(T);

		for (int i = 0; i < T; ++i)
		{
			for (size_t i = 0; i < 10; i++)
			{
				foundDigits[i] = false;
			}

			currentNumber = 0;
			totalFoundDigits = 0;
			result = 0;

			getline(file, line);
			istringstream ss(line);

			ss >> currentNumber;

			if (currentNumber == 0)
			{
				lastSeenNumber[i] = 0;
				continue;
			}

			result = currentNumber;
			tempNumber = result;

			while (tempNumber > 0)
			{
				if (!foundDigits[tempNumber%10])
				{
					foundDigits[tempNumber % 10] = true;
					totalFoundDigits++;
				}
				tempNumber /= 10;
			}

			while (totalFoundDigits < 10)
			{
				result += currentNumber;
				tempNumber = result;

				while (tempNumber > 0 && totalFoundDigits < 10)
				{
					if (!foundDigits[tempNumber % 10])
					{
						foundDigits[tempNumber % 10] = true;
						totalFoundDigits++;
					}
					tempNumber /= 10;
				}
			}
			
			lastSeenNumber[i] = result;
		}
	}
	
	file.close();

	ofstream outputfile;
	outputfile.open("Output.txt");

	for (int i = 0; i < T - 1; ++i)
	{
		if (lastSeenNumber[i] != 0)
		{
			outputfile << "Case #" << i + 1 << ": " << lastSeenNumber[i] << endl;
		}
		else
			outputfile << "Case #" << i + 1 << ": INSOMNIA" << endl;
	}
	if (lastSeenNumber[T - 1] != 0)
	{
		outputfile << "Case #" << T << ": " << lastSeenNumber[T - 1];
	}
	else
		outputfile << "Case #" << T << ": INSOMNIA";
	
	outputfile.close();


	return 0;
}