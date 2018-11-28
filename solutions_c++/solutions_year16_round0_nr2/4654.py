#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main() {
	ifstream openfile;
	fstream outfile;
	openfile.open("B-large.in");
	outfile.open("1.out", ios::out);

	int T, i;
	string N;
	openfile >> T;
	for (int cases = 1; cases <= T; cases++) {
		outfile << "Case #" << cases << ": ";
		int ans = N[0] = '-' ? 1 : 0;
		openfile >> N;
		for (i = 1; N[i] != '\0'; i++) {
			if (N[i] != N[i - 1])ans++;
		}
		if (N[i - 1] == '+')ans--;
		outfile << ans << endl;
	}

	openfile.close();
	outfile.close();
	return 0;
}