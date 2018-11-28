#include <cstdio>
#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ifstream infile("in.txt");
	ofstream outfile("aOut.txt");
	int cases;
	infile >> cases;
	int currentCase = 0;
	while(currentCase++ < cases) {
		int ans1, ans2;
		int cards1[4][4], cards2[4][4];
		infile >> ans1;
		for(int i = 0 ; i < 4 ; i++) {
			for(int j = 0 ; j < 4 ; j++) {
				infile >> cards1[i][j] ;
			}
		}

		infile >> ans2;
		for(int i = 0 ; i < 4 ; i++) {
			for(int j = 0 ; j < 4 ; j++) {
				infile >> cards2[i][j] ;
			}
		}
		
		int check = 0;
		int card = -1;
		for(int i = 0 ; i < 4 ; i++) {
			for(int j = 0 ; j < 4 ; j++) {
				if(cards1[ans1-1][i] == cards2[ans2-1][j]) {
					card = cards1[ans1-1][i];
					check++;
				}
			}
		}
	
		outfile << "Case #" << currentCase << ": ";
		if(check == 0) {
			outfile << "Volunteer cheated!" << endl;
		} else if(check == 1) {
			outfile << card << endl;
		} else {
			outfile << "Bad magician!" << endl;
		}
	}
	infile.close();
	outfile.close();
	return 0;
}
