//Joe Snider
//codejam 2015, qual A

#include <iostream>
#include <string>
#include <vector>
#include <stdlib.h>

using namespace std;

int clap(const vector<int>& seat) {
	int guest = 0;
	int standing = seat[0];
	
	for(int i = 1; i < seat.size(); ++i) {
		while(i > standing + guest) {
			//++guest;
			guest = i-standing;
		}
		standing += seat[i];
	}
	
	return guest;
}

int main() {
	int T, Smax;
	string S;
	cin >> T;
	for(int i = 0; i < T; ++i) {
		cin >> Smax >> S;
		//cout << "gh2 " << Smax << S << "\n";
		vector<int> seat;
		for(auto j = S.begin(); j != S.end(); ++j) {
			seat.push_back(*j-48);
		}
		cout << "Case #" << i+1 << ": " << clap(seat) << "\n";
	}
	
	return 0;
}
