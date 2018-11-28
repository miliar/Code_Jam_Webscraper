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
	//In.open("A-small-prac.in");
	In.open("A-small-attempt5.in");
	//In.open("A-large.in");
	
	// Reads Number of cases //
	In >> NCases;
	
	// Opens output stream //
	ofstream Out;
	//Out.open("A-small-prac.out");
	Out.open("A-small-attempt5.out");
	//Out.open("A-large-attempt0.out");
	
	int i,j;
	
	for (i = 1; i <= NCases; i++) {
		
		int R, C, W;
		
		In >> R >> C >> W;
		
		if (C == W) {
			
			Out << "Case #" << i << ": " << W + (R-1) << endl;
			cout << "Case #" << i << ": " << W + (R-1) << endl;
		} else if (W == 1) {
			
			Out << "Case #" << i << ": " << R*C << endl;
			cout << "Case #" << i << ": " << R*C << endl;
		
		} else {
			
			Out << "Case #" << i << ": " << (int)ceil((double)(C-W)/(double)W) + W  << endl;
			cout << "Case #" << i << ": " << (int)ceil((double)(C-W)/(double)W) + W  << endl;
		
		}
		
		

	}
	
	// Close Input and Output Files //
	In.close();
	Out.close();

	return 0;

}
