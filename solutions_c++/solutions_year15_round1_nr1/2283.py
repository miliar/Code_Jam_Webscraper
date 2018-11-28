#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <math.h>
#include <vector>

using namespace std;


long long getAmount1(vector<int> plates);
long long getAmount2(vector<int> plates);
int main(int argc, char* argv[])
{
	string name = "in.in";
	ifstream inFile;
	if (argc > 0)
		name = argv[1];
	inFile.open(name);
	if (name.size() >= 3)
		name.erase(name.size() - 2, 2);
	ofstream outFile(name + ".out");

	int cases;
	inFile >> cases;
	for (int c = 1; c <= cases; ++c)
	{
		int N;
		inFile >> N;
		vector<int> plates;
		for (int i = 0; i < N; ++i)
		{
			int amt;
			inFile >> amt;
			plates.push_back(amt);
		}
		outFile << "Case #" << c << ": " << getAmount1(plates) << " " << getAmount2(plates);
		if (c != cases)
			outFile << endl;
	}
	inFile.close();
	outFile.close();
	return 0;
}

long long getAmount1(vector<int> plates)
{
	long long total = 0;
	for (int i = 1; i < plates.size(); ++i)
	{
		if (plates[i] < plates[i - 1])
			total += plates[i - 1] - plates[i];
	}
	return total;
}

long long getAmount2(vector<int> plates)
{
	long long total = 0;
	int maxDiff = 0;
	for (int i = 1; i < plates.size(); ++i)
	{
		if (plates[i] < plates[i - 1])
		{
			int difference = plates[i - 1] - plates[i];
			if (difference > maxDiff)
				maxDiff = difference;
		}
	}
	
	for (int i = 0; i < plates.size()-1; ++i)
	{
		if (plates[i] < maxDiff)
			total += plates[i];
		else
			total += maxDiff;
	}
	return total;
}