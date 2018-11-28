#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;

int MinimunInvitedFriend(int Smax, const string &peoples){
	int need = 0;
	int sum = 0;
	for(int i = 0; i <= Smax; ++i){
		if(sum < i){
			need += i - sum;
			sum = i;
		}
		sum += peoples[i] - '0';
	}
	return need;
}

int main() {
	
	ifstream infile{"A-large.in"};
	ofstream outfile{"A-large.out"};

	int t;
	infile >> t;

	int smax;
	string peoples;
	for(int i = 1; i <= t; ++i){
		infile >> smax >> peoples;
		outfile << "Case #" << i << ": " << MinimunInvitedFriend(smax, peoples) << endl;
	}
}