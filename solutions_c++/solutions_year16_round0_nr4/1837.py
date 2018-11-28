
#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <sstream>

using namespace std;

int T,K,C,S,I;
ifstream input;
ofstream output;

typedef unsigned long long ull;

void solve() {
	if(K==S){//Small input, always look the first K tiles
		ostringstream s;
		s << "Case #" << I <<":";
		for(int i=1;i<=K;i++) {
			s << " " << i;
		}
		output << s.str() << endl;

	} else{//Large input
		//if complexity is C and there are missing at most C-1 student, then the input is solvable
		if(K-S<=C-1) {
			ostringstream s;
			s << "Case #" << I <<":";
			int j=1;
			for(int i=K*(C-1);j<=S;--i){
				s << " " << i;
				++j;
			}
			output << s.str() << endl;

		} else {
			output << "Case #" << I << ": IMPOSSIBLE" << endl;
		}

	}


}



int main(){
	input.open("D-small-attempt0.in", ifstream::in);
	output.open("output.txt", ofstream::out);

	input >> T;
	for(I=1;I<=T;++I){
		input >> K >> C >> S;
		cout << K << " " << C << " " << S << endl;
		solve();
		//output << "Case #" << i << ": " << sol << endl;
	}


	input.close();
	output.close();


	return 0;
}

