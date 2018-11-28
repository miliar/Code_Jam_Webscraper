#include <iostream>
#include <fstream>
using namespace std;


int main ( ) {
	 ifstream file("A-small-attempt1.in");
	 ofstream outFile("output.txt");

	int card1[4][4],card2[4][4] ;
	int testcase;
	int count = 1;
	file >> testcase;

	while(testcase--) {
		int row1, row2;
		 
		int fact = 0;
		int num;
		outFile << "case #"<< count++ << ":" ;

		file >> row1;

		for(int i = 0 ; i < 4 ; i++) {
			for(int j = 0 ; j < 4 ;j++) {
				file >> card1[i][j];
			}
		}
		
		file >> row2;

		for(int i = 0 ; i < 4 ; i++) {
			for(int j = 0 ; j < 4 ;j++) {
				file >> card2[i][j];
			}
		}
		
		for( int i = 0 ; i < 4 ; i ++) {
				for ( int j = 0; j < 4 ; j ++ ) {
		if ( card1[row1-1][i] == card2[row2-1][j]) {
				num = card1[row1-1][i];
				fact++;
				}
			}
		}
		if ( fact == 1) {
			outFile << " " << num << endl;
		}
		
		else if (fact == 0) {
			outFile << " Volunteer cheated!"<<endl ;
		}
		else {
			outFile << " Bad magician!"<< endl;
		}

	}
	return 0;
}