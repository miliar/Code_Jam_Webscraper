#include <iostream>
#include <string>
#include <fstream>
#include <sstream>

using namespace std;

int main(void){

	string line;
	int T, deck1[4][4], deck2[4][4], row1, row2, sameInt;

	ifstream f("1.txt");

	getline(f,line); 
	istringstream buf(line);
	buf >> T;

	for (int i=0; i<T; i++){
	
		getline(f,line); istringstream buf1(line); buf1 >> row1;
		for (int j=0; j<4; j++){		
		 getline(f,line); istringstream buf2(line); buf2 >> deck1[j][0] >> deck1[j][1] >> deck1[j][2] >> deck1[j][3];
		}
	

		getline(f,line); istringstream buf3(line); buf3 >> row2;
		for (int j=0; j<4; j++){		
		 getline(f,line); istringstream buf4(line); buf4 >> deck2[j][0] >> deck2[j][1] >> deck2[j][2] >> deck2[j][3];
		}

		cout << "Case #"<< i+1 <<": ";

		int found =0;
		int a;
		for (int k=0; k<4; k++)
		for (int l=0; l<4; l++){
			if ( deck1[row1-1][k] == deck2[row2-1][l]) { found++; a=deck2[row2-1][l];}
		}
		if (found == 0 ) cout << "Volunteer cheated!" << endl;
		if (found > 1) cout <<  "Bad magician!" << endl;
		if (found == 1) cout << a << endl;
	}
	


	return 0;
}
