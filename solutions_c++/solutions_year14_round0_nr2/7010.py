#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

std::vector<std::string> &split(const std::string &s, char delim, std::vector<std::string> &elems)
{
	std::stringstream ss(s);
	std::string item;
	while (std::getline(ss, item, delim)) {
		elems.push_back(item);
	}
	return elems;
}


std::vector<std::string> split(const std::string &s, char delim)
{
	std::vector<std::string> elems;
	split(s, delim, elems);
	return elems;
}

int main()
{
	std::ifstream input("input.txt");
	std::ofstream output("output.txt");

	if (!input.is_open())
		return printf("Failed to open file\n");

	int cases = 0;

	std::string line;
	getline(input, line);

	cases = atoi(line.c_str());

	for (int i = 0; i < cases; ++i)
	{
		double F = 0;

		double C = 0;

		double X = 0;

		std::string line;
		getline(input, line);
		auto keks = split(line, ' ');
		C = atof(keks.at(0).c_str());
		F = atof(keks.at(1).c_str());
		X = atof(keks.at(2).c_str());

		double production = 2.0;

		double totalTime = 0;
		
		double timeForNextFarm = (C) / production;

		while ((X / production) + totalTime > (X / (production + F)) + totalTime + timeForNextFarm)
		{
			totalTime += timeForNextFarm;
			production += F;
			timeForNextFarm = (C) / production;
		}	
		totalTime += (X / production);
		printf("%.7f\n", totalTime);
		char szKeks[256];
		sprintf(szKeks, "Case #%d: %.7f\n", i+1, totalTime);
		output.write(szKeks, strlen(szKeks));
		output.flush();
	}

	output.close();

	std::cin >> line;

	return 0;
}