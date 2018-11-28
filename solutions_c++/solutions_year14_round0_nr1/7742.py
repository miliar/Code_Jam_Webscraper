#include <iostream>
#include <fstream>

using namespace std;

int grid1[4], grid2[4], row1, row2;
int n1, n2, n3, n4;

int main(int argc, char **argv)
{
	fstream in, out;
	in.open("A-small-attempt0.in", ios::in);
	out.open("output.txt", ios::out);
	int ncase, bidone, nsoluz=0, numeroDaIndovinare;
	in >> ncase;
	
	for(int i=1; i<=ncase; i++) {
		// GET DATAS
		in >> row1;
		//cout << row1 << endl;
		for(int x=0; x<4; x++) {
			for(int y=0; y<4; y++) {
				if(x == (row1 - 1)) {
					in >> grid1[y];
					//cout << grid1[y] << " ";
				} else in >> bidone;
			}
		}
		//cout << endl;
		in >> row2;
		for(int x=0; x<4; x++)
			for(int y=0; y<4; y++)
				if(x == (row2 - 1))
					in >> grid2[y];
				else in >> bidone;
		
		// BEGIN TO SOLVE
		/*
		 * per ogni numero nella grid1
		 * lo controlli nella grid2
		 * ricompare--> numeri++
		 * se numeri == 0 -> volche
		 * se numeri == 1 -> ok qual è il numero
		 * se numeri >= 1 -> stop, bad magician
		 * 
		 */
		 for(int j=0; j<4; j++) {
			for(int k=0; k<4; k++)
				if(grid1[j] == grid2[k]) {
					if(nsoluz == 0)
						numeroDaIndovinare = grid1[j];
					nsoluz++;
				}
		}
		
		out << "Case #" << i << ": ";
		if(nsoluz == 0)
			out << "Volunteer cheated!";
		else if(nsoluz == 1)
			out << numeroDaIndovinare;
		else if(nsoluz > 1)
			out << "Bad magician!";
		out << endl;
		nsoluz = 0;
	}
	
	return 0;
}
