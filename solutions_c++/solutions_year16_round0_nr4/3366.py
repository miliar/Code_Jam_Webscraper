#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <cmath>
#include <vector>

using namespace std;

int main() {
	ofstream ofile;
	ofile.open("./B.out");
	ifstream ifile;
	ifile.open("./D-small-attempt0.in");
	int t, tt, k, c, s;
	tt = 0;
	ifile >> t;
	while(tt < t)
	{
		ifile >> k >> c >> s;
		ofile << "Case #" << tt + 1 << ": ";
		for(int i = 1; i < k; ++i)
			ofile << i << " ";
		ofile<< k << "\n";
		tt++;
	}
	ifile.close();
	ofile.close();

	return 0;
}