#include <iostream>
#include <fstream>
#include <memory.h>
using namespace std;


int main() {	
	int a[4][4];
	int ans;
	int T;	
	int solvs[4];
	int result;
	ifstream inFile;
	ofstream outFile;

	inFile.open("A-small-attempt1.in");
	outFile.open("A-small-attempt1.out");

	
	inFile >> T;

	for(int i=0;i<T;i++){
		result = 0;
		inFile >> ans;
		for(int j=0;j<4;j++) {
			for(int k=0;k<4;k++) {
				inFile >> a[j][k];
			}
		}
		memcpy(solvs, a[ans-1], sizeof(solvs));
		
		inFile >> ans;
		for(int j=0;j<4;j++) {
			for(int k=0;k<4;k++) {
				inFile >> a[j][k];
			}			
		}

		int cnt=0;
		for(int j=0;j<4;j++) {
			for(int k=0;k<4;k++) {	
				if(a[ans-1][j] == solvs[k]) {
					cnt++;
					result = solvs[k];
				}
			}
		}
		
		if(cnt == 0) {
			outFile << "Case #" << i+1 << ": Volunteer cheated!" << endl;
		} else if(cnt==1) {
			outFile << "Case #" << i+1 << ": " << result << endl;
		} else if(cnt>1) {
			outFile << "Case #" << i+1 << ": Bad magician!" << endl;
		}
	}	
	return 0;
}
