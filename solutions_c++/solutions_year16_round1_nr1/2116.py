#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char** argv) {
	ifstream File("txt.in");

	if (File.is_open()) {
		ofstream ofile("txt.out");
		string out = "";
		int test;
		File >> test;
		for (int i = 1; i <= test; ++i) {
			out += "Case #" + to_string(i) + ": ";
			string S;
			File >> S;
			string lastword = "";
			lastword += S[0];
			for (int j = 1; j < S.length(); ++j) {
				if (S[j] >= lastword[0]) {
					lastword = S[j] + lastword;
				}
				else
				{
					lastword += S[j];
				}
			}
			out += lastword + '\n';
		}

		ofile.clear();
		ofile << out;
		ofile.close();
		File.close();
	}

	return 0;
}