#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;


int main(int argc, char **argv) {
	ifstream ifs( argv[1] );
	ofstream ofs( "output.out" );
	int T;
	ifs >> T;
	for (int ccc = 1; ccc <= T; ccc++){
		int N;
		ifs >> N;
		N++;
		string shy;
		ifs >> shy;
		int i = 0,
			prefixsum = 0,
			need = 0;
		for (char c : shy){
			int val = c - '0';
			if (prefixsum < i && val != 0){
				need += i - prefixsum;
				prefixsum = i;
			}
			i++;
			prefixsum += val;
		}
		ofs << "Case #" << ccc << ": " << need << endl;
	}
	return 0;
}
