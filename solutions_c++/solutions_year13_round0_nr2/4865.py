#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

typedef vector<int> intVec;
typedef vector<intVec> intVec2d;
typedef vector<intVec2d> set;

int main(int argc, char* argv[]) {
	//variables
	ifstream fin;
	fin.clear();
	int numberOfLawns;
	set allLawns;
	ofstream fout;
	fout.open("output.out");
	
	
	if(argc>1) fin.open(argv[1]);
	
	if(!fin.good()) {
		fout<<"Bad file"<<endl;
		return 0;
	}

	//load the data
		//get number of data
		fin>>numberOfLawns;
		for(int lawnIndex=0;lawnIndex<numberOfLawns;lawnIndex++) {
			int cols,rows;
			fin>>rows>>cols;
			intVec2d thisBoard;
			for(int y=0;y<rows;y++) {
				intVec thisRow;
				for(int x=0;x<cols;x++) {
					int temp;
					fin>>temp;
					thisRow.push_back(temp);
				}
				thisBoard.push_back(thisRow);
			}
			allLawns.push_back(thisBoard);
		}
		
	//test: print data
/*	for(int i=0;i<numberOfLawns;i++) {
		for(int y=0;y<allLawns[i].size();y++) {
			for(int x=0;x<allLawns[i][y].size();x++) {
				fout<<allLawns[i][y][x];
			}
			fout<<endl;
		}
		fout<<endl;
	}*/
	
	//loop through each lawn
	for(int lawnIndex=0;lawnIndex<numberOfLawns;lawnIndex++) {
		// for each place in the lawn
		bool possible = true;
		fout<<"Case #"<<lawnIndex+1<<": ";
		for(int y=0;y<allLawns[lawnIndex].size() && possible;y++) {
			for(int x=0;x<allLawns[lawnIndex][y].size() && possible;x++) {
				// check that every element in that row and 
				// column is at most as tall as that place
				int thisPlace = allLawns[lawnIndex][y][x]; 
				bool yPossible=true;
				bool xPossible=true;
				for(int yCheck=0;yCheck<allLawns[lawnIndex].size()&&yPossible;yCheck++) {
					if(!(thisPlace>=allLawns[lawnIndex][yCheck][x])) {
//						fout<<"("<<x<<" "<<y<<")="<<allLawns[lawnIndex][y][x]<<" <=("<<x<<" "<<yCheck<<")="<<allLawns[lawnIndex][yCheck][x]<<endl;
						yPossible = false;
//						fout<<"NO"<<endl;
					}
				}
				for(int xCheck=0;xCheck<allLawns[lawnIndex][y].size() && xPossible;xCheck++) {
					if(!(thisPlace>=allLawns[lawnIndex][y][xCheck])) {
//						fout<<"("<<x<<" "<<y<<")="<<allLawns[lawnIndex][y][x]<<" <=("<<xCheck<<" "<<y<<")="<<allLawns[lawnIndex][y][xCheck]<<endl;
						xPossible = false;
//						fout<<"NO"<<endl;
					}
				}
				if(!(yPossible || xPossible)) {
					possible = false;
					fout<<"NO"<<endl;
				}
			}
		}
		if(possible) fout<<"YES"<<endl;
	}
}
