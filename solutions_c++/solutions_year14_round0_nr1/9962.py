#include <iostream>
#include <fstream>
using namespace std;

int main(){

	ifstream input("A-small-attempt0.in");
	ofstream output("A-small-attempt0.out");
	int card1[4][4], card2[4][4];
	int T;
	int r1, r2;
	int cnt, last;
	input >> T;
	for(int i=0; i<T; i++){
		input >> r1;
		for(int r=0; r<4; r++)
			for(int c=0; c<4; c++)
				input >> card1[r][c];
		input >> r2;
		for(int r=0; r<4; r++)
			for(int c=0; c<4; c++)
				input >> card2[r][c];
		cnt = 0;
		last = -1;
		for(int c1=0; c1<4; c1++){
			for(int c2=0; c2<4; c2++){
				if(card1[r1-1][c1] == card2[r2-1][c2]){
					cnt++;
					last = card1[r1-1][c1];
				}
			}
		}
		output << "Case #" << i+1 << ": ";
		if(cnt == 1) output << last << endl;
		else if(cnt > 1) output << "Bad magician!" << endl;
		else output << "Volunteer cheated!" << endl;
	}

	return 0;
}