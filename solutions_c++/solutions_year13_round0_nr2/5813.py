#include <iostream>
#include <fstream>
#define  INPUTFILE "B-small-attempt0.in"
#define  OUTPUTFILE "B-small-attempt0.out"

using namespace std;

int main () {
	ifstream inf (INPUTFILE, ios::in);
	ofstream outf (OUTPUTFILE, ios::out);

	int T, M, N;
	bool isPosC, isPosR, isPos;
	bool all = true;
	int lawn[101][101] = {0};
	while (inf >> T) {
		for (int i=1; i<=T; ++i) {
			isPosC = true;
			isPosR = true;
			isPos = true;
			inf >> N >> M;
			for (int row=0; row<N; ++row) {
				for (int col=0; col<M; ++col) {
					inf >> lawn[row][col];
				}
			}

			if (M==1 || N==1) {
				outf << "Case #" << i << ": " << "YES" << endl;
				continue;
			}

			for (int col=0; col<M; ++col) {
				isPosC = true;
				if (lawn[0][col]!=2) {
					for (int r=0; r<N; ++r) {
						if (lawn[r][col] == 2) { 
							isPosC = false;
							break;
						}
					}
					if (isPosC) for (int r=0; r<N; ++r) lawn[r][col] = 3;
				}
			}
			for (int row=0; row<N; ++row) {
				isPosR = true;
				if (lawn[row][0]!=2) {
					for (int c=0; c<M; ++c) {
						if (lawn[row][c] == 2) {
							isPosR = false;
							break;
						}
					}
					if (isPosR) for (int c=0; c<M; ++c) lawn[row][c] = 3;
				}
			}

			for (int row=0; row<N; ++row) {
				for (int col=0; col<M; ++col) {
					if (lawn[row][col]==1) {
						isPos = false;	
						break;
					}
				}
				if (!isPos) break;
			}
			if (!isPos) 
				outf << "Case #" << i << ": " << "NO" << endl;
			else outf << "Case #" << i << ": " << "YES" << endl;
		}
	}
	return 0;
}
