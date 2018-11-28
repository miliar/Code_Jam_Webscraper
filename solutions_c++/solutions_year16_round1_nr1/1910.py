#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <cmath>
#include <vector>

using namespace std;

int main() {
	ofstream ofile;
	ofile.open("./A.out");
	ifstream ifile;
	ifile.open("./A-small-attempt0.in");
	int t, tt, n, i;
	tt = 0;
	ifile >> t;
	string s, res;
	while(tt < t)
	{
		ifile >> s;
		n = s.size();
		res = s.substr(0, 1);
		for(i = 1; i < n; ++i)
		{
			if(s[i] >= res[0])
				res = s.substr(i, 1) + res;
			else
				res += s.substr(i, 1);
		}
		ofile << "Case #" << tt + 1 << ": " << res << "\n";
		tt++;
	}
	ifile.close();
	ofile.close();
	return 0;
}