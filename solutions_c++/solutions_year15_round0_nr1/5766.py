#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(){
	ifstream fin("A-large.in");
	ofstream fout("output.txt");

	int T;
	fin >> T;
	for (int t = 1; t <= T; t++){
		int max;
		string s;
		fin >> max >> s;
		int standing = 0;
		int add = 0;
		for (int i = 0; i <= max; i++){
			int n = s[i] - '0';
			if (standing < i && n != 0){
				add += (i - standing);
				standing += (i - standing);
			}
			standing += n;
		}
		fout << "Case #" << t << ": " << add << endl;
	}
	fout.close();
	return 0;
}