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


vi get_splits(int Max) {
	
	vi splits;
	
	splits.push_back(0);
	
	for (int i = 1; i <= Max; i++) {
		int minsplit = 100000;
		int minsteps = i+1;
		for (int j = 0; j < (int)ceil((double)i/2.0); j++) {
			if ((int)ceil((double)i/((double)j+1.0)) + j < minsteps ) {
				minsplit = j;
				minsteps = (int)ceil((double)i/((double)j+1.0)) + j;
			}
		}
		
		splits.push_back(minsplit);		
		
	}
	
	
	return splits;
}


int main() {

	int Max = 9;
	vi splits = get_splits(Max);

	int NCases; 
	ifstream In;
	In.open("B-small-attempt1.in");
	//In.open("B-large-attemp0.in");
	
	// Reads Number of cases //
	In >> NCases;
	
	// Opens output stream //
	ofstream Out;
	Out.open("B-small-attempt1.out");
	//Out.open("B-large-attempt0.out");
	
	int i,j;

	for (i = 1; i <= NCases; i++) {
		
		int D;
		vi P;
		vi count;
		int maxP;
		
		In >> D;
		maxP = 0;
		
		for (j = 0; j <= Max; j++){
			count.push_back(0);
		}
		
		for (j = 0; j < D; j++) {
			int tmp;
			In >> tmp;
			P.push_back(tmp);
			if (tmp > maxP){
				maxP = tmp;
			}
			count[tmp] += 1;	
		}

		Out << "Case #" << i << ": ";
		
		int maxcurrent = 0;
		int totalcuts = 0;
		
		vii combs;
		
		int minutes = 1000000;
		
		vi jj;
		for (j = 0; j <=Max; j++) {
			jj.push_back(0);
		}
		
		for (jj[4] = 0; jj[4] <= ((count[4]>0)?splits[4]:0); jj[4]++) {
			for (jj[5] = 0; jj[5] <= ((count[5]>0)?splits[5]:0); jj[5]++) {
				for (jj[6] = 0; jj[6] <= ((count[6]>0)?splits[6]:0); jj[6]++) {
					for (jj[7] = 0; jj[7] <= ((count[7]>0)?splits[7]:0); jj[7]++) {
						for (jj[8] = 0; jj[8] <= ((count[8]>0)?splits[8]:0); jj[8]++) {
							for (jj[9] = 0; jj[9] <= ((count[9]>0)?splits[9]:0); jj[9]++) {
								
								int tmin = 0;
								int cuts = 0;
								int mind = 0;
								for (int k = 1; k <=Max; k++) {
									if (count[k] > 0) {
										int tmp=(int)ceil((double)k/((double)jj[k]+1.0));
										if (tmp > mind){
											mind = tmp;
										}
										cuts += count[k]*jj[k];
									}
								}
								
								if (cuts + mind < minutes) {
									minutes = cuts + mind;
								}
																
							}
						}	
					}
				}
			}		
		}
		
		Out << minutes << endl;			

	}
	// Close Input and Output Files //
	In.close();
	Out.close();

	return 0;

}
