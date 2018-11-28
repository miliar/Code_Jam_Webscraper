#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("in");
ofstream fout("out");

int readRow() {
	int row = 0;
	int rowi; fin>>rowi;
	for(int i=0; i<4; i++) {
		for(int j=0; j<4; j++) {
			int card; fin>>card;
			if(rowi==i+1)
				row = row | (1<<(card-1));
		}
	}
	return row;
}

void printRow(int row) {
	for(int i=0; i<16; i++)
		cout << ((row>>i)&1);
	cout << endl;
}

int main() {
	int T; fin>>T;
	for(int t=1; t<=T; t++) {
		int row1 = readRow();
		int row2 = readRow();
		printRow(row1);
		printRow(row2);
		int candidates = row1 & row2;
		printRow(candidates);
		cout << endl;
		fout << "Case #" << t << ": ";
		if(candidates==0)
			fout << "Volunteer cheated!" << endl;
		else {
			int card = -1;
			bool bad = false;
			for(int i=0; i<16; i++) {
				if((candidates&(1<<i))!=0) {
					if(card==-1)
						card = i;
					else {
						bad = true;
						break;
					}
				}
			}
			if(bad)
				fout << "Bad magician!" << endl;
			else
				fout << (card+1) << endl;
		}
	}

	return 0;
}

