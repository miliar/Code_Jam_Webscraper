
#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <sstream>

using namespace std;

int T,I;
string S;
ifstream input;
ofstream output;

typedef unsigned long long ull;

void solve() {

	string last(S.begin(),S.begin()+1);

	for(unsigned int i=1;i<S.length();++i) {
		if(last[0]<=S[i]) {
			last = S[i] + last;
		} else {
			last = last + S[i];
		}
	}
	output << "Case #" << I << ": " << last << endl;
}



int main(){
	input.open("A-large.in", ifstream::in);
	output.open("output.txt", ofstream::out);

	input >> T;
	for(I=1;I<=T;++I){
		input >> S;
		cout << S << endl;
		solve();
		//output << "Case #" << i << ": " << sol << endl;
	}


	input.close();
	output.close();


	return 0;
}




