#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

#define PI 3.141592653589

int main()
{
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	int T;
	fin >> T;
	for (int t = 1; t <= T; t++) {
		long long r, p;
		fin >> r >> p;
		long long cost = 2*r+1;
		int y = 0;
		while (p - cost >= 0) {
			y++;
			p -= cost;
			cost += 4;
		}
		fout << "Case #" << t << ": " << y << endl;
	}
}