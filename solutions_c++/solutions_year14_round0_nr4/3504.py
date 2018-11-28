#include<iostream>
#include<fstream>
#include<deque>
#include<map>

using namespace std;

int main(int argc, char *argv[])
{
	ifstream file;
	ofstream outputFile;
	
	int numberOfBlocks=0, intTestCases=0, intKenWinsDeceit=0, intKenWinsWar=0;
	deque<double> naomiBlocksWar, naomiBlocksDeceitWar, kenBlocksWar, kenBlocksDeceitWar;
	double x=0;
	
	outputFile.open(argv[2]);
	file.open(argv[1]);

	if(!file.eof())
	{
		file >> intTestCases;
	}

	for(int t=0; t<intTestCases; ++t)
	{
		intKenWinsDeceit=0;
		intKenWinsWar=0;
		
		file >> numberOfBlocks;
		
		for (int i=0; i<numberOfBlocks; ++i) {
			file >> x;
			naomiBlocksWar.push_back(x);
			naomiBlocksDeceitWar.push_back(x);
		}
		
		for (int i=0; i<numberOfBlocks; ++i) {
			file >> x;
			kenBlocksWar.push_back(x);
			kenBlocksDeceitWar.push_back(x);
		}
		
		std::sort (naomiBlocksWar.begin(), naomiBlocksWar.end());
		std::sort (naomiBlocksDeceitWar.begin(), naomiBlocksDeceitWar.end());
		std::sort (kenBlocksWar.begin(), kenBlocksWar.end());
		std::sort (kenBlocksDeceitWar.begin(), kenBlocksDeceitWar.end());
		
		for (int i=0; i<numberOfBlocks; ++i) {
			if(kenBlocksDeceitWar.front() > naomiBlocksDeceitWar.front()){
				intKenWinsDeceit++;
				naomiBlocksDeceitWar.pop_front();
				kenBlocksDeceitWar.pop_back();
			}else {
				naomiBlocksDeceitWar.pop_front();
				kenBlocksDeceitWar.pop_front();
			}
		}
		
		naomiBlocksDeceitWar.clear();
		kenBlocksDeceitWar.clear();
		
		for (int i=0; i<numberOfBlocks; ++i) {
			if(kenBlocksWar.back() < naomiBlocksWar.back()){
				kenBlocksWar.pop_front();
				naomiBlocksWar.pop_back();
			}else {
				kenBlocksWar.pop_back();
				naomiBlocksWar.pop_back();
				intKenWinsWar++;
			}
		}
		
		naomiBlocksDeceitWar.clear();
		kenBlocksDeceitWar.clear();
		
		if (t==0) {
			outputFile << "Case #" << t+1 << ": " << numberOfBlocks-intKenWinsDeceit << " " << numberOfBlocks-intKenWinsWar;
		}else {
			outputFile << "\nCase #" << t+1 << ": " << numberOfBlocks-intKenWinsDeceit << " " << numberOfBlocks-intKenWinsWar;
		}


	}
}