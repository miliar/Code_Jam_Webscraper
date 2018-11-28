#include <iostream>
#include <fstream>
using namespace std;

int main () {
	int t;
	int r1;
	int r2;
	int R1[16];
	int R2[16];
	int card;
	int counter;
	ifstream infile;
	infile.open("A-small-attempt1.in");
	ofstream outfile;
	outfile.open ("Problem_A_result.txt");
	infile >> t;
	for(int j=1;j<=t;j++){
		counter = 0;
		infile >> r1;
		r1=(r1-1)*4;
		for(int i=0;i<16;i++){
			infile >> R1[i];
		}
		infile >> r2;
		r2=(r2-1)*4;
		for(int i=0;i<16;i++){
			infile >> R2[i];
		}
		for(int i=0;i<4;i++){
			if(R1[r1+i]==R2[r2]||R1[r1+i]==R2[r2+1]||R1[r1+i]==R2[r2+2]||R1[r1+i]==R2[r2+3]){
				card = R1[r1+i];
				counter++;
			}
		}
		outfile << "Case #" << j << ": ";
		if(counter == 0){
			outfile << "Volunteer cheated!\n";
		}
		if(counter == 1){
			outfile << card << "\n";
		}
		if(counter > 1){
			outfile << "Bad magician!\n";
		}
	}
	infile.close();
	outfile.close();
	return 0;
}
