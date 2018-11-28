#include <iostream>
#include <fstream>
using namespace std;

int w,h;

int board[100][100];
int cut[100][100];

int check(int h, int w) {
	for(int z = 100; z > 0; z--) {
		for (int i=0;i<w;i++) {
			int count = 0;
			for (int j=0;j<h;j++) {
				if (board[j][i]<=z) count++;
			}
			if (count == h) {
				for (int j=0;j<h;j++) {
					cut[j][i] = cut[j][i] < z ? cut[j][i] : z;
				}
			}
		}
		for (int i=0;i<h;i++) {
			int count = 0;
			for (int j=0;j<w;j++) {
				if (board[i][j]<=z) count++;
			}
			if (count == w) {
				for (int j=0;j<w;j++) {
					cut[i][j] = cut[i][j] < z ? cut[i][j] : z;
				}
			}
		}
	}
	for (int i=0;i<h;i++){
		for (int j=0;j<w;j++) {
			if (cut[i][j] != board[i][j]) return 2;
		}
	}
	return 1;
}


int main () {
	int num,result;

	ifstream infile;
	infile.open ("D:/in.txt");
	ofstream outfile;
	outfile.open ("D:/B.txt");

	infile >> num;

	for (int i=1;i<=num;i++) {
		infile >> h; infile >> w;
		for (int k=0;k<h;k++) for(int j=0;j<w;j++) { infile >> board[k][j]; cut[k][j] = 100;}

		result = check(h,w);

		outfile << "Case #" << i << ": ";
		switch (result)
		{
		case 1: outfile << "YES" << endl; break;
		case 2: outfile << "NO" << endl; break;
		default:
			break;
		}
		cout << "   " << i << endl;
	}

	outfile.close();
	infile.close();

	return 0;
}