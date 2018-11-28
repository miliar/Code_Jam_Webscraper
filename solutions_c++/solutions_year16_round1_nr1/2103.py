#include <string>
#include <fstream>
#include <vector>
#include <set>
#include <algorithm>
#include <iostream>
#include <stack>
#include <deque>
#include "boost/multiprecision/cpp_int.hpp"

using namespace std;
using namespace boost::multiprecision;

using ll = long long;
using vs = vector<string>;
using vi = vector<int>;
using vl = vector<long long>;

int main(int argc, char** argv)
{
	int t;

	ifstream fi("input.in");
	ofstream fo("output.out");

	fi >> t;
	fi.ignore(numeric_limits<streamsize>::max(), '\n');

	for (int i = 1; i <= t; ++i)
	{
		string w;
		getline(fi, w);

		string f;
		f += w[0];
		for (int i = 1; i < w.length(); ++i)
		{
			if (w[i] >= f[0])
				f.insert(f.begin(), w[i]);
			else
				f += w[i];
		}

		fo << "Case #" << i << ": " << f << endl;
	}

	fi.close();
	fo.close();

	return 0;
}