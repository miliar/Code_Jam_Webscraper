#include<iostream>
#include<fstream>
#include<string>
#include<vector>
using namespace std;
int main() {
	ifstream openfile;
	fstream outfile;
	openfile.open("A-large.in");
	outfile.open("out.txt", ios::out);
	int t;
	openfile >> t;

	for (int cases = 1; cases <= t+1; cases++) {
		string in1;
		getline(openfile, in1);
		if (cases > 1) {
			outfile << "Case #" << cases-1 << ": ";
			string new1 = in1;
			for (int i = 1; i < in1.length(); i++) {
				in1 = new1;
				string temp1 = "", temp2 = "";
				if (in1[i] >= in1[0]) {
					new1 = "";
					temp1 = in1[i];
					for (int j = 0; j < in1.length(); j++) {
						if (i != j) {
							temp2 += in1[j];
						}
					}
					new1 += temp1;
					new1 += temp2;
				}
			}
			outfile << new1 << endl;
			//cout << new1 << endl;
			//outfile << in1 << endl;
		}
	}
}