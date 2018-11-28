#include <iostream>
#include <fstream>

using namespace std;

int grid[4][4];
int cards[17];
int n,k,i,j,l,s,tmp;

int main(int argc, char **argv)
{
	ifstream test;
	test.open (argv[1]);
	ofstream odp;
	odp.open (argv[2]);
	test >> n;
	for (i=0; i<n; i++) {
		test >> k;
		for (j=0; j<17; j++) cards[j] = 0;
		for (j=0; j<4; j++) {
			for (l=0; l<4; l++) {
				test >> grid[j][l];
			}
		}

		for (j=0; j<4; j++) {
			cards[grid[k-1][j]]++;
		}
		
		test >> k;
		
		for (j=0; j<4; j++) {
			for (l=0; l<4; l++) {
				test >> grid[j][l];
			}
		}
		
		for (j=0; j<4; j++) {
			cards[grid[k-1][j]]++;
		}
		
		s = 0;
		for (j=1; j<17; j++) {
			if (cards[j] == 2) {
				s++;
				tmp = j;
			}
		}	
		if (s == 0) odp << "Case #" << i+1 <<": Volunteer cheated!" <<endl;
		else if (s == 1) odp << "Case #" << i+1 <<": "<< tmp <<endl;
		else odp << "Case #" << i+1 <<": Bad magician!" <<endl; 
	}
	test.close();
	odp.close();
	
	return 0;
}
