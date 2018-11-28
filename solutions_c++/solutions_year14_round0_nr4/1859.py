#include <iostream>
#include <string>
#include <set>

using namespace std;

int main(){
	int numCases;
	int currentCase = 0;
	int numCubes;
	double temp;
	int naomiPoints = 0;
	int kenPoints = 0;
	cin >> numCases;
	while(currentCase++ < numCases){
		//cerr << currentCase;
		naomiPoints = 0;
		kenPoints = 0;

		cin >> numCubes;
		set<double> naomiBlocks;
		set<double> kenBlocks;
		for(int i = 0; i < numCubes; ++i){
			cin >> temp;
			naomiBlocks.insert(temp);
		}
		for(int i = 0; i < numCubes; ++i){
			cin >> temp;
			kenBlocks.insert(temp);
		}

		auto naomiMin = naomiBlocks.cbegin();
		auto kenMin = kenBlocks.cbegin();
		auto naomiMax = naomiBlocks.cend();
		auto kenMax = kenBlocks.cend();
		naomiMax--;
		kenMax--;
		cerr << *naomiMin << " " << numCubes << " " << *naomiMax << endl;


		cout << "Case #" << currentCase << ": ";
		//ken in normal achieves same as a deceiful naomi
		//naomi normal war: find ken's points and find inverse to get naomi's
		while(naomiMax != naomiMin){
			if(*kenMin < *naomiMin){
				kenMin++;
				naomiMax--;
				cerr << *naomiMax << *naomiMin << endl;

			}
			else { //*kenMin > *naomiMin, would result in guaranteed point for ken
				kenPoints++;
				kenMin++;
				naomiMin++;
			}
		}
		if(*kenMin > *naomiMin){
			kenPoints++;
		}

		naomiMin = naomiBlocks.cbegin();
		kenMin = kenBlocks.cbegin();
		naomiMax = naomiBlocks.cend();
		kenMax = kenBlocks.cend();
		naomiMax--;
		kenMax--;
		//cerr << *naomiMin << " " << numCubes << " " << *naomiMax << endl;


		//just pretend deceitful becomes ken; the apprentice becomes the master
		while(naomiMax != naomiMin){
			if(*naomiMin < *kenMin){
				naomiMin++;
				kenMax--;
			}
			else{
				naomiPoints++;
				kenMin++;
				naomiMin++;
			}
		}
		if(*naomiMin > *kenMin){
			naomiPoints++;
		}
		cout << naomiPoints << " " << numCubes - kenPoints << "\n";
	}

	return 0;
}