#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <string>
#include <cstdlib>

const std::string inputFile = "A-large.in";
const std::string outputFile = "A.out";

using namespace std;

int main() {
	fstream f;
	f.open(inputFile.data());

	ofstream out(outputFile.data());

	int t;
	f >> t;
	for(int i=1; i<=t; i++) {
		out << "Case #" << i << ": ";
		int n;
		f >> n;
		if(n==0) {
			out << "INSOMNIA";
		}
		else {
			bool seen[10];
			for(int j=0; j<10; j++) {
				seen[j] = false;
			}
			int cur = 0;
			while(true) {
				cur+=n;
				string curseen = to_string(cur);
				for(int j=0; j<curseen.length(); j++) {
					seen[(int)curseen[j] - (int)'0'] = true;
				}
				bool foundRes = true;
				for(int j=0; j<10; j++) {
					if(seen[j] == false) foundRes = false;
				}
				if(!foundRes) continue;
				out << cur;
				break;
			}
		}
		out << endl;
	}

	f.close();
	out.close();

	return 0;
}
