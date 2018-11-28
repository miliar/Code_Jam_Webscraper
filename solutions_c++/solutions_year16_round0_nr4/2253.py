#include <iostream>
#include <fstream>

using namespace std;



int main() {
	ifstream in;
	ofstream out;
	string fname;
	cout << "Input file: ";
	cin >> fname;
	
	in.open(fname.c_str());
	out.open("outl.txt");
	
	int T, K, C, S;
	
	in >> T;
	
	for (int k = 1; k <= T; k++) {
		in >> K >> C >> S;
		
		out << "Case #" << k << ":";
		for (int i = 1; i <= K && i <= S ; i++) 
			out << " " << i;
		out << endl;
	}
	
	
	return 0;
}