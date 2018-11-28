#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <cstdlib>
using namespace std;

int main(int argc, char** argv){
	ifstream fin("A-small-attempt1.in");
	//ifstream fin("test.in");
	ofstream fout("test.out");
	int N;
	fin >> N;
	for (int i = 1; i <= N; ++i){
		int smax;
		fin >> smax;
		string aud;
		fin >> aud;
		int n_aud = aud[0] - '0';
		int fr = 0;
		for (int j = 1; j < smax + 1; ++j){
			if (aud[j] == '0') continue;
			if (n_aud >= j){
				n_aud += aud[j] - '0';
			}
			else{
				fr += j - n_aud;
				n_aud += fr + (aud[j] - '0');
			}
		}
		fout << "Case #" << i << ": " << fr << endl;
	}
	return 0;
}
