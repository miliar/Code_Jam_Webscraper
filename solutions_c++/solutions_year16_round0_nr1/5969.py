#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <sstream>
#include <vector>
using namespace std;

int main() {
	ifstream fin("A-large.in");
	ofstream fout("A-large.txt");
	int T;
	fin >> T;
	for(int step = 1; step <= T; step++) {
		long long num;
		fin >> num;
		string is = "FFFFFFFFFF"; // "0123456789"
		long long final = num;
		if (num != 0) {
			for(int i = 1; is.find("F") != std::string::npos; i++) {
				long long nnum = num*i;
				final = nnum;
				stringstream conv;
				conv << nnum;
				string rev = conv.str();
				for(int j = 0; j < 10; j++) {
					if(is[j] == 'T')
						continue;
					if(rev.find('0'+j) != std::string::npos)
						is[j] = 'T';
				}
			}
		}
		if (num != 0)
			fout << "Case #" << step << ": " << final << endl;
		else
			fout << "Case #" << step << ": " << "INSOMNIA" << endl;
	}
	return 0;
}


