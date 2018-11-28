#include <iostream>
#include <fstream>
using namespace std;

int main(){
	ifstream infile;
	infile.open("D-small-attempt2.in");
	if (!infile.is_open()) cout << "Failed to load file!" << endl;

	ofstream outfile;
	outfile.open("output5.txt");
	int T, K, C, S;
	infile >> T;

	for (int i = 1; i <= T; i++){
		infile >> K >> C >> S;
		if (C == 1){
			outfile << "Case #" << i << ": ";
			for (int j = 1; j <= K; j++) outfile << j << ' ';
			outfile << endl;
		}
		else if (K == 2) outfile << "Case #" << i << ": " << 2 << endl;
		else if (K == 3) outfile << "Case #" << i << ": " << 2 << ' ' << 6 << endl;
		else {
			outfile << "Case #" << i << ": ";
			for (int j = 1; j <= K; j++) outfile << j*K << ' ';
			outfile << endl;
		}
	}
	infile.close();
	outfile.close();
	system("pause");
	return 0;
}