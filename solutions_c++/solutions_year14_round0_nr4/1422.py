#include <iostream>
#include <fstream>
#include <cstdlib>
using namespace std;

int compare(const void* a, const void* b) {
	if((*(double*)a - *(double*)b) > 0) return 1;
	if((*(double*)a - *(double*)b) < 0) return -1;
	else return 0;
}
int compare2(const void* a, const void* b) {
	if((*(double*)a - *(double*)b) > 0) return -1;
	if((*(double*)a - *(double*)b) < 0) return 1;
	else return 0;
}

int main() {
	ifstream infile("dIn.txt");
	ofstream outfile("dOut.txt");
	int cases;
	infile >> cases;
	int currentCase = 0;
	while(currentCase++ < cases) {
		int blocks = 0;
		infile >> blocks;
		double naomi[blocks], ken[blocks];
		for(int i = 0 ; i < blocks ; i++) 
			infile >> naomi[i];
		for(int i = 0 ; i < blocks ; i++) 
			infile >> ken[i];
		qsort(naomi, blocks, sizeof(naomi[0]), compare);
		qsort(ken,  blocks, sizeof(ken[0]), compare);

		int war = 0, dWar = 0;
		int kenIdx = 0;
		int i ;
		bool done = false;
		bool kenUsedWar[blocks];
		for(int j = 0 ; j < blocks ; j++)
			kenUsedWar[j] = false;
		for(i = 0 ; i < blocks ; i++) {
			bool lost = false;
			for(int j = 0 ; j < blocks ; j++) {
				if(kenUsedWar[j]) continue;
				if(naomi[i] < ken[j]) {
					kenUsedWar[j] = true;
					lost = true;
					break;
				}
			}
			if(!lost) war++;
		}
		bool naomiUsedWar[blocks];
		for(int j = 0 ; j < blocks ; j++)
			naomiUsedWar[j] = false;

		for(i = 0 ; i < blocks ; i++) {
			bool win = false;
			for(int j = 0 ; j < blocks ; j++) {
				if(naomiUsedWar[j]) continue;
				if(ken[i] < naomi[j]) {
					naomiUsedWar[j] = true;
					win = true;
					break;
				}
			}
			if(win) dWar++;
		}

		outfile << "Case #" << currentCase << ": " << dWar << " " << war << endl;
	}
	infile.close();
	outfile.close();
	return 0;
}
