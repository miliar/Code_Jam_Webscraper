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
	
	int T;
	string S;
	in >> T;
	
	
	for (int k = 1; k <= T; k++) {
		in >> S;
		
		int count = 0;
		bool up[S.length()];
		
		for (int j = 0; j < S.length(); j++) 
			up[j] = (S[j] == '+')? true : false;
		
		bool prev = up[0];
		
		for (int i = 1; i<S.length(); i++) {
			
			if (prev != up[i]) {
				for (int n = 0; n < i; n++)
					up[n] = !up[n];
				count++;
			}
			
			prev = up[i];
		}
		
		if (!up[0]) 
			count++;
		
		
		out << "Case #" << k << ": " << count << endl;
		
		
	}
	
	return 0;
}