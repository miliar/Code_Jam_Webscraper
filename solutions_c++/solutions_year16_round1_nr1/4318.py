#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(){
	ofstream file;
	ifstream inf;
	inf.open("A-large.in");
	file.open("output.txt");
	int T;
	inf >> T;

	for (int i = 1; i <= T; i++) {
		string s,t;
		inf >> s;
		file << "Case #" << i << ": ";
		
		for (char c : s){
			if (t.empty() || c < t.front()) {
				t += c;
			}
			else {
				t = c + t;
			}
		}

		file << t;
		file << endl;
	}
	return 0;
}