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
	ifile.open("./B-large.in");
	int t, k = 0, res, i;
	char c;
	string cake;
	ifile >> t;
	while(k < t)
	{
		ifile >> cake;
		c = '-';
		res = 0;
		i = cake.size() - 1;
		while(i >= 0 && cake[i] == '+')
			--i;
		while(i >= 0)
		{
			while(i >= 0 && cake[i] == c)
				--i;
			if(c == '+')
				c = '-';
			else
				c = '+';
				++res;
		}
		ofile << "Case #" << k + 1 << ": " << res << "\n";
		k++;
	}
	ifile.close();
	ofile.close();

	return 0;
}