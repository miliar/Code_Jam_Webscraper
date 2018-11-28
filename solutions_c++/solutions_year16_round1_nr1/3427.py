#include <iostream>
#include <fstream>

using namespace std;


int main() {
	
	ifstream in;
	ofstream out;
	string fname, num;
	cout << "Input file: ";
	cin >> fname;
	
	in.open(fname.c_str());
	out.open("out1.txt");
	
	int T;
	string S;
	
	in >> T;
	getline(in, S);
	for (int k = 1; k<=T; k++) {
		
		out << "Case #" << k << ": ";
		
		getline(in, S);
		string last = S.substr(0,1);
		
		for (int i = 1; i < S.length(); i++) {
			last = (S[i]<last[0]? last + S.substr(i,1) : S.substr(i,1) + last);
		}
		
		out << last << endl;
	}
	
	
	
	return 0;
}