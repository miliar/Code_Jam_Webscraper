#include <iostream>
#include <fstream>
#include <stdint.h>
#include <set>
#include <string>
#include <algorithm>

using namespace std;

void ReadBlocksMasses(ifstream& source, multiset<double>& destination, multiset<double>& copyDestination, uint64_t blocksCount)
{
	for (uint64_t i = 0; i < blocksCount; ++i)
	{
		double blockMass = 0.0;
		source>>blockMass;
		destination.insert(blockMass);
		copyDestination.insert(blockMass);
	}
}
uint64_t GetFairWarPoints(multiset<double>& naomiBlocks, multiset<double>& kenBlocks)
{
	uint64_t points = 0;
	while(!naomiBlocks.empty())
	{
		if (*naomiBlocks.begin() > *kenBlocks.rbegin())
		{
			return points + naomiBlocks.size();
		}
		else if (*naomiBlocks.rbegin() < *kenBlocks.begin())
		{
			return points;
		}
		else if (*naomiBlocks.rbegin() > *kenBlocks.rbegin())
		{
			naomiBlocks.erase(--naomiBlocks.end());
			kenBlocks.erase(kenBlocks.begin());
			points++;
		}
		else
		{
			naomiBlocks.erase(--naomiBlocks.end());
			kenBlocks.erase(find_if(kenBlocks.begin(), kenBlocks.end(),
				[&](double d){return d > *naomiBlocks.rbegin();}));
		}
	}
	return points;
}
uint64_t GetDeceitfulWarPoints(multiset<double>& naomiBlocks, multiset<double>& kenBlocks)
{
	uint64_t points = 0;
	while(!naomiBlocks.empty())
	{
		if (*naomiBlocks.begin() > *kenBlocks.rbegin())
		{
			return points + naomiBlocks.size();
		}
		else if (*naomiBlocks.rbegin() > *kenBlocks.begin())
		{
			naomiBlocks.erase(find_if(naomiBlocks.begin(), naomiBlocks.end(), 
				[&](double d){return d > *kenBlocks.begin();}));
			kenBlocks.erase(kenBlocks.begin());
			points++;
		}
		else 
		{
			return points;
		}
	}
	return points;
}

int main(int argc, char* argv[])
{
	ifstream inputFile;
	inputFile.open(argv[1]);

	ofstream outputFile;
	outputFile.open(argv[2]);

	uint64_t casesCount = 0;
	inputFile>>casesCount;

	for (uint64_t caseNumber = 1; caseNumber <= casesCount; ++caseNumber)
	{
		multiset<double> naomiBlocks;
		multiset<double> naomiBlocksCopy;
		multiset<double> kenBlocks;
		multiset<double> kenBlocksCopy;

		uint64_t blocksCount = 0;

		inputFile>>blocksCount;
		ReadBlocksMasses(inputFile, naomiBlocks, naomiBlocksCopy, blocksCount);
		ReadBlocksMasses(inputFile, kenBlocks, kenBlocksCopy, blocksCount);
		
		outputFile<<"Case #"<<caseNumber<<": "<<GetDeceitfulWarPoints(naomiBlocks, kenBlocks)<<" "<<GetFairWarPoints(naomiBlocksCopy, kenBlocksCopy)<<endl;
	}

	inputFile.close();
	outputFile.close();

	return 0;
}