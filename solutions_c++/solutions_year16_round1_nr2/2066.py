#include <string>
#include <fstream>
#include <vector>
#include <set>
#include <algorithm>
#include <iostream>
#include <stack>
#include "boost/multiprecision/cpp_int.hpp"

using namespace std;
using namespace boost::multiprecision;

using ll = long long;
using vs = vector<string>;
using vi = vector<int>;

int main(int argc, char** argv)
{
	int t, n;

	ifstream fi("input.in");
	ofstream fo("output.out");

	fi >> t;

	for (int i = 1; i <= t; ++i)
	{
		fi >> n;

		int m = (2 * n - 1) * n;

		vi d;

		int x;
		for (int i = 0; i < m; i++) {
			fi >> x;
			d.push_back(x);
		}

		sort(d.begin(), d.end());

		vi a;

		int y = d[0];
		int c = 0;
		for (int i = 0; i < d.size(); i++)
		{
			if (d[i] != y) {
				if (c % 2 == 1)
					a.push_back(y);
				y = d[i];
				c = 1;
			} else {
				c++;
			}
		}

		if (c % 2 == 1)
			a.push_back(d[d.size() - 1]);

		sort(a.begin(), a.end());

		fo << "Case #" << i << ": ";
		for (int i = 0; i < a.size(); i++)
			fo << a[i] << " ";
		fo << endl;
	}

	fi.close();
	fo.close();

	return 0;
}