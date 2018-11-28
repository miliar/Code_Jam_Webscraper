#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;

int numberOfPersonsToInvite(int maxShy, string shynesses) {
	int need = 0;
	int standing = shynesses[0]-'0';
	for (int i = 1 ; i < maxShy+1 ; i++) {
		if (standing < i) {
			cout << "i=" << i << ", lack " << i-standing << endl;
			need += i-standing;
			standing += i-standing;
		}
		standing += shynesses[i]-'0';
	}
	return need;
}

int main()
{
	/*
	string s("2000007");
	cout << numberOfPersonsToInvite(6, s);
	*/

	ifstream is("input.txt");
	ofstream os("output.txt");
	string line;
	getline(is, line);
	stringstream ss(line);
	int caseAmount;
	ss >> caseAmount;

	int caseNo = 1;
	while (caseNo <= caseAmount) {
		std::getline(is, line);
		stringstream ss(line);
		int s_max;
		string shynesses;
		if (ss >> s_max >> shynesses) {
			cout << "s_max = " << s_max << ", shynesses = " << shynesses << endl;
			os << "Case #" << caseNo << ": "
				<< numberOfPersonsToInvite(s_max, shynesses) << endl;
		} else {
			// TODO
		}
		caseNo++;
	}
	is.close();
	os.close();
}
