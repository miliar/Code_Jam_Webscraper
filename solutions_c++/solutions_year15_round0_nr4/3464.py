# include <iostream>
# include <cmath>
# include <vector>
# include <string>
# include <algorithm>
# include <ostream>
# include <fstream>

using namespace std;

typedef vector<int> vi;
typedef vector<vector<int> > vii;


int main() {

	int NCases; 
	ifstream In;
	In.open("D-small-attempt0.in");
	//In.open("D-large-attemp0.in");
	
	// Reads Number of cases //
	In >> NCases;
	
	// Opens output stream //
	ofstream Out;
	Out.open("D-small-attempt0.out");
	//Out.open("D-large-attempt0.out");
	
	int i,j;

	for (i = 1; i <= NCases; i++) {
		
		int X, R, C;
		
		In >> X;
		In >> R;
		In >> C;

		Out << "Case #" << i << ": ";
		cout << "Case #" << i << ": ";
		
		if ((R*C)%X == 0 && ((R >= X && C >= X-1) || (C >=X && R >=X-1)) ) {
			Out << "GABRIEL" << endl;	
			cout 	<< "GABRIEL" << endl;	
		} else {
			Out << "RICHARD" << endl;		
			cout << "RICHARD" << endl;		
		}		

	}
	// Close Input and Output Files //
	In.close();
	Out.close();

	return 0;

}
