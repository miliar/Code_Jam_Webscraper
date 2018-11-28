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
	In.open("A-small-attempt2.in");
	//In.open("A-small-practice.in");
	
	// Reads Number of cases //
	In >> NCases;
	
	// Opens output stream //
	ofstream Out;
	Out.open("A-small-attempt2.out");
	
	int i,j;

	for (i = 1; i <= NCases; i++) {
		
		int Smax;
		int Nova = 0, Nneed = 0;
		
		// Read Smax //
		In >> Smax;
		Out << "Case #" << i << ": ";
		for (j = 0; j <=Smax; j++) {
		
			char test;
			In >> test;
			int t1 = test - '0';
			
			if (t1 > 0) {
				if (Nova >= j) {
					Nova += t1;
				} else {
					Nneed += abs(j-Nova);
					Nova += Nneed;
					Nova += t1;
				}		
			}
		}

		Out << Nneed << endl;
		
	}
	
	// Close Input and Output Files //
	In.close();
	Out.close();
	

	return 0;

}
