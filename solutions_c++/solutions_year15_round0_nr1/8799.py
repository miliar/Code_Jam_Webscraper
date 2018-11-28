#include <bits\stdc++.h>

using namespace std;

int main() {
	int t, fr, curlev, n;
	string str;
	ifstream fin("A-large.in");
	ofstream fout("output.out");
	fin >> t;
	for (int j=0;j < t;j++) {
		fin >> n;
		fin >> str;
		curlev = str[0] - 48;
		fr = 0;
		for (int i=1;i < n + 1;i++) {
			if (i > curlev) {
				fr += i - curlev ;
				curlev = i + str[i] - 48;
			}
			else curlev += str[i] - 48;
		}
		fout << "Case #"<< j+1 << ": " << fr << endl;
	} 
	fin.close();
	fout.close();	
	return 0;
}
