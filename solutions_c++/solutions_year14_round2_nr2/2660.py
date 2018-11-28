#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>
using namespace std;

int main() {
	ofstream outfile;
	ifstream infile;
	infile.open("B-small-attempt0.in");	
	outfile.open("B.out");
	
	int A,B,K,T;
	
	infile >> T;
	for(int t = 0; t < T; t++) {
		infile >> A >> B >> K;	
		
		int count = 0;
		for(int a = 0; a < A; ++a) {
			for(int b = 0; b < B; ++b) {
				if((a&b) < K)
					count++;
			}
		}
		
		outfile << "Case #" << t+1 << ": " << count << "\n";
	}
	
	return 0;
}

