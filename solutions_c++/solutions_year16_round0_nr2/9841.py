
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <fstream>

using namespace std;

std::string countingSheep(long N);
void pancakeManeuvers(std::string pancakes, int &maneuvers);
std::string flipMe(std::string pancakeStack);

int main() {
	int numTestCases;
	//long N;
	std::string pancakeStack;
	//std::ifstream infile("large_input.txt");
	std::ifstream infile("large_input_pancakes.txt");
	infile >> numTestCases;
	int coutadjuster = 1;
	for (int coutadjuster = 1; coutadjuster <= numTestCases; coutadjuster++)
	{
		//infile >> N;
		//std::string pancakeStack;
		infile >> pancakeStack;
		int maneuvers = 0;
		pancakeManeuvers(pancakeStack, maneuvers);
		cout << "Case #" << coutadjuster << ": " << maneuvers << endl; //countingSheep(N) << endl;
	}
	return 0;
}

void pancakeManeuvers(std::string pancakes, int &maneuvers) {
	if (pancakes.length() == 0)
	{
		return;
	}
	std::string newpancakes(pancakes);
	if (newpancakes.back() == '-') {
		if (newpancakes[0] == '+')
		{
			for (int i = 0; i < newpancakes.length(); i++)
			{
				if (newpancakes[i] == '-')
				{
					for (int j = i - 1; j >= 0; j--)
					{
						newpancakes[j] = '-';
					}
					break;
				}
			}
			maneuvers++;			
		}
		newpancakes = flipMe(newpancakes);
		maneuvers++;
		
	}
	pancakeManeuvers(newpancakes.substr(0, pancakes.length() - 1), maneuvers);
}

std::string flipMe(std::string pancakeStack) {
	std::reverse(pancakeStack.begin(), pancakeStack.end());
	std::string newcakes(pancakeStack);
	for (int i = 0; i < newcakes.length(); i++)
	{
		if (newcakes[i] == '-')
		{
			newcakes[i] = '+';
		}
		else
		{
			newcakes[i] = '-';
		}
	}
	return newcakes;
}


std::string countingSheep(long N)
{
	std::vector<int> digits = { 0,1,2,3,4,5,6,7,8,9 };
	if (N == 0)
	{
		return "INSOMNIA";
	}
	long multiplier = 1;
	while (digits.size() != 0)
	{
		long long result = multiplier * N;
		std::ostringstream intStream;
		intStream << result;
		std::string intString(intStream.str());
		std::string returnResult(intString);
		std::for_each(intString.begin(), intString.end(), [&digits](char c) {
			auto iter = std::find(digits.begin(), digits.end(), c - '0');
			if (iter != digits.end())
			{
				digits.erase(iter);
			}
		});

		if (digits.size() == 0)
		{
			return returnResult;
		}
		multiplier++;
	}
}