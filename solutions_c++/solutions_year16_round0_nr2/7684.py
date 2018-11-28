#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
	ofstream out_file;
	ifstream in_file;
	out_file.open("B_large_out.txt");
	in_file.open("B_large_in.txt");

	int T;
	//cin >> T;
	in_file >> T;

	for(int i = 1; i <= T; ++i) {
		int groups = 1;
		string s;
		//cin >> s;
		in_file >> s;

		if(s.length() != 1) {
			for(int j = 1; j < s.length(); ++j) {
				if(s[j] != s[j-1]) {
					groups++;
				}
			}
			if(s[s.length()-1] == '+') {
				groups--;
			}
 		}
 		if(s == "+") {
 			groups = 0;
 		}
		//cout << "Case #" << i << ": " << groups << endl;
		out_file << "Case #" << i << ": " << groups << endl;
	}

	in_file.close();
	out_file.close();
	return 0;
}