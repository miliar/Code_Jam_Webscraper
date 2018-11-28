#include <fstream>
#include <iostream>
#include <vector>

using namespace std;



int main(){
	ifstream fin("D-small.in");
	ofstream fout("D-output.txt");

	int T;
	fin >> T;
	for (int t = 1; t <= T; t++){
		int k, c, s;
		fin >> k >> c >> s;
		fout << "Case #" << t << ":";
		for (int i = 1; i <= s; i++){
			fout << " " << i;
		}
		fout << endl;
	}
	fout.close();
	return 0;
}