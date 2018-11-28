#include<iostream>
#include<fstream>
#include<string>


using namespace std;


int main() {
	ifstream openfile;
	fstream outfile;
	openfile.open("B-large.in");
	outfile.open("output", ios::out);


	string s;
	int Text, i;
	
	openfile >> Text;
	for (int cases = 1; cases <= Text; cases++) {
		
		outfile << "Case #" << cases << ": ";
		int ans = s[0] = '-' ? 1 : 0;
		openfile >> s;
		
		for (i = 1; s[i] != '\0'; i++) {
			if (s[i] != s[i - 1])ans++;
		}
		if (s[i - 1] == '+')ans--;
		outfile << ans << endl;
	}

	openfile.close();
	outfile.close();
	return 0;
}
