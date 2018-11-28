#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main() {
	ifstream openfile;
	fstream outfile;
	openfile.open("B-large.in");
	outfile.open("out.txt", ios::out);
	int t, i;
	string in1;
	openfile >> t;
	for (int cases = 1; cases <= t; cases++) {
		outfile << "Case #" << cases << ": ";
		int ans = in1[0] = '-' ? 1 : 0;
		openfile >> in1;
		for (i = 1; in1[i] != '\0'; i++) {
			if (in1[i] != in1[i - 1])ans++;
		}
		if (in1[i - 1] == '+')ans--;
		outfile << ans << endl;
	}
}