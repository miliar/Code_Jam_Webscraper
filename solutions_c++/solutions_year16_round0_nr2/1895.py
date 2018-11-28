
#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <sstream>

using namespace std;

int T;
string S;
ifstream input;
ofstream output;

#define NUM_N 32
#define HALF_N NUM_N/2

int solve() {

	int flips = 0;
	char last = S[0];
	for(int i=1;i<S.length();++i){
		if(last != S[i])
			++flips;

		last = S[i];
	}

	if(last == '-')
		++flips;
	return flips;


}



int main(){
	input.open("B-large.in", ifstream::in);
	output.open("output.txt", ofstream::out);

	input >> T;
	for(int i=1;i<=T;++i){
		input >> S;
		cout << S << endl;
		int sol = solve();
		output << "Case #" << i << ": " << sol << endl;
	}


	input.close();
	output.close();


	return 0;
}

