#include <fstream>
#include <limits>
#include <string>
#include <math.h>
#include <bitset>
#include <iostream>
#include <vector>
#include <map>

using namespace std;

const int BASE_MIN = 2;
const int BASE_MAX = 10;
const int BIN_PLACES_MAX = 32;

string toBinString(int dec, int length) {
	return bitset<BIN_PLACES_MAX>(dec).to_string().erase(0, BIN_PLACES_MAX - length);
}

long unsigned getNontrivialDivisor(string bin, int base) {
	long unsigned decRep = stol(bin, nullptr, base);
	for (long unsigned i = 2; i < (long unsigned) sqrt(decRep) + 1; i++) {
		if (decRep % i == 0) {
			return i;
		}
	}
	return 0;
}

string computeCase(istream &is) {
	int binLength;
	vector<vector<long unsigned>>::size_type reqSolQ;
	is >> binLength;
	is >> reqSolQ;
	int maxI = pow(2, binLength - 2);
	int i = 0;
	map<string, vector<long unsigned>> solutions;
	while (i < maxI && solutions.size() < reqSolQ) {
		string binI = '1' + toBinString(i, binLength - 2) + '1';
		vector<long unsigned> nontrivialDivisors;
		for (int j = BASE_MIN; j <= BASE_MAX; j++) {
		 	int nontrivialDivisor = getNontrivialDivisor(binI, j);
		 	if (nontrivialDivisor == 0) {
		 		continue;
		 	}
		 	nontrivialDivisors.push_back(nontrivialDivisor);
		}
		if (nontrivialDivisors.size() == (BASE_MAX - BASE_MIN + 1)) {
			solutions[binI] = nontrivialDivisors;
		}
		i++;
	}
	string ret;
	for (auto it = solutions.begin(); it != solutions.end(); it++) {
		ret += "\n" + it->first;
		for (auto jt = it->second.begin(); jt < it->second.end(); jt++) {
			ret += " " + to_string(*jt);
		}
	}
	return ret;
}

int main() {

	ifstream inF("in");
	fstream outF("out", fstream::out);
	int caseCount;
	inF >> caseCount;
	inF.ignore(numeric_limits<streamsize>::max(), '\n');
	for (int caseNum = 1; caseNum <= caseCount; caseNum++) {
		outF << "Case #" << caseNum << ": " << computeCase(inF) << endl;
	}
	return 0;

}
