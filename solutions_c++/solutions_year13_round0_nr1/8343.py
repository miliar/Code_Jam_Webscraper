#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h> 

using namespace std;

bool sameAs(char src, char chk){
		if( src != '.'  && src == chk || src == 'T' || chk  == 'T'){
			return true;
		}
		return false;
}

int main(int argc, char* argv[])  {
	string infile = argv[1];
	string cases;
	int casenum;
	string trash;
	ifstream myReadFile;
	string grid[4] ;
	myReadFile.open(infile.c_str());
	if (myReadFile.is_open()) {
		std::getline(myReadFile,cases);
		casenum = atoi(cases.c_str());
		for(int i = 1; i <= casenum; i++) {
			for(int j = 0; j < 4; j++){
				myReadFile >> grid[j];
			}
			bool cont = false;
			for(int h = 0; h < 4; h++){
				if(sameAs(grid[h][0], grid[h][1])){
					if(sameAs(grid[h][2], grid[h][3])){
						if(sameAs(grid[h][1], grid[h][3])){
							if(grid[h][0] != 'T'){
								cout << "Case #" << i << ": " << grid[h][0] << " won" << endl;
							} else {
								cout << "Case #" << i << ": " << grid[h][3] << " won" << endl;
							}
							cont = true;
						}
					}
				} 
			}
			if(!cont){
				for(int h = 0; h < 4; h++){
					if(sameAs(grid[0][h], grid[1][h])){
						if(sameAs(grid[2][h], grid[3][h])){
							if(sameAs(grid[1][h], grid[3][h])){
								if(grid[0][h] != 'T'){
									cout << "Case #" << i << ": " << grid[0][h] << " won" << endl;
								} else {
									cout << "Case #" << i << ": " << grid[3][h] << " won" << endl;
								}	
								cont = true;
							}
						}
					} 
				}
			}
			if(!cont){
				if(sameAs(grid[0][0], grid[1][1]) && sameAs(grid[2][2], grid[3][3]) && sameAs(grid[3][3], grid[1][1]) ){
					if(grid[0][0] != 'T'){
						cout << "Case #" << i << ": " << grid[0][0] << " won" << endl;
					} else {
						cout << "Case #" << i << ": " << grid[3][3] << " won" << endl;
					}
					cont = true;
				}
			}
			if(!cont){
				if(sameAs(grid[0][3], grid[3][0]) && sameAs(grid[1][2], grid[2][1]) && sameAs(grid[3][0], grid[2][1]) ){
					if(grid[0][3] != 'T'){
						cout << "Case #" << i << ": " << grid[0][3] << " won" << endl;
					} else {
						cout << "Case #" << i << ": " << grid[3][0] << " won" << endl;
					}
					cont = true;
				}
			}
			if(!cont){
				for(int h = 0; h < 4; h++){
					for(int k = 0; k < 4; k++){
						if(!cont && grid[h][k] == '.'){
							cout << "Case #" << i << ": Game has not completed" << endl;
							cont = true;
						}
					}
				}
			}
			if(!cont){
				cout << "Case #" << i << ": Draw" << endl;
			}
			if(!myReadFile.eof()){
				getline(myReadFile, trash);
			}
		}
	}
	cout << endl;
	myReadFile.close();
	return 0;
}
