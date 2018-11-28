#include <iostream>
#include <fstream>
#include <string>
using namespace std;

ifstream fin("b.in");
ofstream fout("b.out");

int getnflips(string pk) {

	int ndiff = 0;
	char ch = pk[0];
	for(int i=1; i<(int)pk.size(); i++) {
		if(pk[i]!=ch) {
			ndiff++;
			ch = pk[i];
		}
	}
	if(ch=='-') {
		ndiff++;
	}
	return ndiff;

}

int main() {
	int T;
	fin >> T;
	for(int t=1; t<=T; t++) {
		string pancakes;
		fin >> pancakes;
		int nflp = getnflips(pancakes);
		fout << "Case #" << t << ": " << nflp << endl;
	}

	return 0;
}

