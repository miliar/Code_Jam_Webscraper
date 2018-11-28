#include <algorithm>
#include <cmath>
#include <cstring>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

using namespace std;

template <class T>
T split(string str, char delim) {
	T t;
	string token;
	stringstream ss(str);
	while (getline(ss, token, delim))
		t.push_back(stoull(token));
	return t;
}

bool checkFS(string s) {
	for (string::iterator l=s.begin(), r = s.end()-1; r>l; l++, r--)
		if (*l != *r) return false;
	return true;

}

int main(int argc, char **argv) {
	// Setup input and output files
	if (argc != 2) {
		cout << "Input file!" << endl;
		return 1;
	}
	string filename(argv[1]);
	ifstream is(filename);
	ofstream os(filename.replace(filename.end()-2, filename.end(), "out"));

	string buf;

	// Loop over test cases
	getline(is, buf);
	int numTests = stoi(buf);
	for (int n=1; n<=numTests; n++) {
		os << "Case #" << n << ": ";
		cout << "Case #" << n << ": ";

		int count = 0;
		getline(is, buf);
		vector<unsigned long long int> range = split<vector<unsigned long long int> >(buf, ' ');
		for (unsigned long long int i=range[0]; i<=range[1]; i++) {
			stringstream ss1; ss1 << i;
			if (checkFS(ss1.str()) && !(sqrt(i)-(unsigned long long int)sqrt(i))) {
					stringstream root; root << (unsigned long long int)sqrt(i);
					if (checkFS(root.str()))
					++count;
			}
		}
		os << count << endl;
		cout << count << endl;
	}

	// wrap it up
	is.close();
	os.close();
	return 0;
}

// USEFULL STUFF
// for (XXX::iterator it=XXX.begin(); it!=XXX.end(); it++) {
