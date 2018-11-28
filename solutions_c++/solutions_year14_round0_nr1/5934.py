//============================================================================
// Name        : MagicTrick.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
using namespace std;
int t;
int grid1[4][4];
int grid2[4][4];

void compareRows(int row1[], int row2[]) {
	int matches = 0;
	int y = -1;
	for (int j = 0; j < 4; j++) {
		for (int k = 0; k < 4; k++) {
			if(row1[j]==row2[k]){
				matches++;
				y=row1[j];
			}
			//printf("%d %d %d\n",matches,row1[j],row2[k]);
		}
	}
	if(y==-1){
		printf("Volunteer cheated!");
	}
	else if(matches > 1){
		printf("Bad magician!");
	}
	else{
		printf("%d",y);
	}
}

int main() {
	 std::ifstream input("A-small-attempt0.in");
	input >> t;
	for (int i = 0; i < t; i++) {
		int a1, a2;
		input >> a1;
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				input >> grid1[j][k];
			}
		}
		input >> a2;
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				input >> grid2[j][k];
			}
		}
		printf("Case #%d: ",i+1);
		compareRows(grid1[a1-1], grid2[a2-1]);
		printf("\n");
	}
	return 0;
}
