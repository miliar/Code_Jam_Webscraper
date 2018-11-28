
#include <iostream>
#include <fstream>
#include <cmath>
#include <bitset>
#include <string>
#include <sstream>

using namespace std;

int T,N,J;
ifstream input;
ofstream output;

#define NUM_N 32
#define HALF_N NUM_N/2

unsigned long long horner(bitset<HALF_N> jam, int base) {

	unsigned long long p = jam[jam.size()-1];
	for(int i=jam.size()-2;i>=0;i--) {
		p = jam[i] + p*base;
	}

	return p;
}
unsigned long long horner(bitset<NUM_N> jam, int base) {

	unsigned long long p = jam[jam.size()-1];
	for(int i=jam.size()-2;i>=0;i--) {
		p = jam[i] + p*base;
	}

	return p;
}



void solve() {

	int half = NUM_N/2;

	//Create a number of the form 100..001 with "half" bits

	int num = 1 << (half-1);++num;
//	cout << bitset<NUM_N> (num) << endl;

	// Generate J coins
	int num_coins = 0;
	for(int i=num;;i=i+2) {
		ostringstream s;
		//i is the expected factor, no matter the base
		int coin = i << half;
		coin+=i;

		cout << bitset<NUM_N> (coin);
		s << bitset<NUM_N> (coin);
		for(int j=2;j<=10;j++) {
			unsigned long long h = horner(bitset<HALF_N> (i), j);
			s << " " << h;
			cout << " " << horner(bitset<NUM_N> (coin), j);
		}

		cout << endl;

		output << s.str() << endl;

		if(++num_coins == J) break;
	}




}



int main(){
	input.open("C-large.in", ifstream::in);
	output.open("output.txt", ofstream::out);

	input >> T;
	//cout <<T<<endl;
	for(int i=1;i<=T;++i){
		input>>N >> J;
		output << "Case #" << i << ":" << endl;
		solve();
		cout <<N << " " << J << endl;
	}


	input.close();
	output.close();


	return 0;
}




