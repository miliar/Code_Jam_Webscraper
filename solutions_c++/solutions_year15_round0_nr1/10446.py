// standing_ovation_1.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <fstream>

int main()
{
	std::ifstream infile ("D:\\mine\\input1.txt");
	std::ofstream outfile ("D:\\mine\\output1.txt");
	
	std::string line; 
	std::getline(infile, line);
	int testCaseNum = std::stoi(line);

	std::vector<std::map<int, int>> testData;
	for (int n = 0; n < testCaseNum; n++)
	{
		std::map<int, int> audience;
		std::getline(infile, line);
		const char *testCaseInput = line.c_str();
		int maxShyness = testCaseInput[0] - '0';
		for (int i = 0; i <= maxShyness; i++)
		{
			audience[i] = testCaseInput[i+2] - '0';
		}
		testData.push_back(audience);
	}

	for (int n = 0; n < testCaseNum; n++)
	{
		std::map<int, int> audience = testData.at(n);
		int friends = 0;
		int sumOvation = 0;
		for (int i = 1; i < audience.size(); i++)
		{
			sumOvation += audience.at(i - 1);
			if (i > sumOvation)
			{
				friends++;
				sumOvation++;
			}
		}
		std::cout << "Case #" << n + 1 << ": " << friends << std::endl;
		outfile << "Case #" << n + 1 << ": " << friends << std::endl;
	} 
	outfile.close();
	infile.close();
	return 0;
}

