#include <iostream>
#include <fstream>
#include <string>
#include <vector>

int main()
{
std::ifstream inFile;
std::ofstream outFile;
int testCases;
std::string str;

inFile.open("input.txt");
inFile >> testCases;

outFile.open("output.txt");

for (int i = 0; i < testCases; i++)
{
	char maxShyness;
	std::string maxStr;
	std::string str;

	inFile >> maxStr;
	
	inFile >> str;
	
	int total = 0;
	int friends = 0;
	
	for (int j = 0; j < str.length(); j++)
	{		
		int val = (int)str[j] -48;
		total += val;
		if (total < j + 1)
		{
			total++;
			friends++;
		}
	}
	outFile << "Case #" << i+1 << ": " << friends << std::endl;
}

inFile.close();
outFile.close();
}

