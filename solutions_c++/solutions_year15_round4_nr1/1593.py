#include <iostream>
#include <algorithm>
#include <vector>
#include<fstream>
#include<string>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

int main(){
	int T;
	ifstream input;
	ofstream output;
	input.open("a.txt");
	output.open("output.txt");
	input >> T;
	forn (i, T){
		printf("break\n");
		output << "Case #"<< i+1 <<": ";
		int R,C;
		input >> R >> C;
		string in[R];
		forn (j, R){
			input >> in[j];
			//printf("%s\n",in[j].c_str());
		}
		bool poss = 1;
		int count = 0;
		forn (j, R)
			forn (k , C){
				if (in[j][k] == '.') continue;
				bool left = 0;
				bool right = 0;
				bool up = 0;
				bool down = 0;
				int l = k-1;
				while (l >= 0){
					if (in [j][l] != '.'){
						left = 1;
						break;
					}
					l = l-1;
				}
				l = k+1;
				while (l <C){
					if (in [j][l] != '.'){
						right = 1;
						break;
					}
					l = l+1;
				}
				l = j-1;
				while (l >=0){
					//printf("%d\n", l);
					if (in [l][k] != '.'){
						up = 1;
						break;
					}
					l = l-1;
				}
				l = j+1;
				while (l < R){
					if (in [l][k] != '.'){
						down = 1;
						break;
					}
					l = l+1;
				}
				if (!(left | right | up | down))
					poss = 0;
				if (in [j][k] == '^' & !up){
					 count = count +1;
					//printf("%d%d\n", j,k);
				}
							
				if (in [j][k] == 'v' & !down){
					 count = count +1;
					//printf("%d%d\n", j,k);
				}
				if (in [j][k] == '>' & !right){
					 count = count +1;
					//printf("%d%d\n", j,k);
				}
				if (in [j][k] == '<' & !left) {
					 count = count +1;
					//printf("%d%d\n", j,k);
				}
			}
		if (poss)	output << count << endl;
		else output << "IMPOSSIBLE" << endl;
	}
}	

