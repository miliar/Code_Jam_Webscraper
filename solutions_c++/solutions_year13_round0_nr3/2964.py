#include <algorithm>
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

using namespace std;


bool is_palindromes(int num) {
	vector<int> digits;
	
	while(num) {
		digits.push_back(num%10);
		num/=10;
	}
	for(int i=0; i<(int)digits.size()/2; i++) {
		if(digits.at(i) != digits.at(digits.size()-i-1)) {
			return false;
		}
	}
	return true;
}

int main() {
	int cn;
	double minn, maxn; 
	ifstream inf("C-small-attempt1.in");
	ofstream outf("C-small-attempt1.out");

	inf>>cn;
	for(int i=0; i <cn ; i++) {
		int count = 0;
		inf>>minn>>maxn;
		double min_s = ceil(sqrt(minn));
		double max_s = floor(sqrt(maxn));

		for(int j=(int)min_s; j<=(int)max_s; j++) {
			if(is_palindromes(j) && is_palindromes(j*j)) {
				count++;
			}
		}

		outf<<"Case #"<<i+1<<": "<<count<<endl;
	}
	return 0;
}
