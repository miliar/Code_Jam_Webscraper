#include <iostream>
#include <fstream>
#include <queue>

using namespace std;

struct coord {
	int x;
	int y;
	int flag;
};


int main() {
	fstream fin("D-large.in",ios::in);
	fstream fout("D-large.out",ios::out);
	int T;
	fin>>T;
	int i;
	double naomi[1000];
	double ken[1000];
	for(i = 1;i <= T;i++) {
		int honest = 0, cheat = 0;
		int N;
		fin>>N;
		int j;
		for(j = 0;j < N;j++) {
			fin>>naomi[j];
		}
		for(j = 0;j < N;j++) {
			fin>>ken[j];
		}
		int m, n;
		for(m = 0;m < N;m++) {
			for(n = m;n < N;n++) {
				if(naomi[m] < naomi[n]) {
					double t = naomi[m];
					naomi[m] = naomi[n];
					naomi[n] = t;
				}
			}
		}
		for(m = 0;m < N;m++) {
			for(n = m;n < N;n++) {
				if(ken[m] < ken[n]) {
					double t = ken[m];
					ken[m] = ken[n];
					ken[n] = t;
				}
			}
		}
		int indexNaomi = 0;
		int frontKen = 0, endKen = N-1;
		for(indexNaomi = 0;indexNaomi < N;indexNaomi++) {
			if(naomi[indexNaomi] > ken[frontKen]) {
				honest++;
				endKen--;
			}
			else {
				frontKen++;
			}
		}

		frontKen = 0;
		endKen = N-1;
		for(indexNaomi = N-1;indexNaomi >= 0;indexNaomi--) {
			if(naomi[indexNaomi] > ken[endKen]) {
				cheat++;
				endKen--;
			}

		}


		fout<<"Case #"<<i<<": "<<cheat<<" "<<honest<<endl;


	}

	return 0;
}