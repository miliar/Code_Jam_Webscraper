#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
	int ncases, k, c, s;
	vector<int> v;
	ifstream in;
	ofstream out;
	in.open("D/D-small-attempt0.in");
	out.open("D/D-small-results.out");

	in >> ncases;

	for (int t = 1; t <= ncases; t++)
	{
		out << "Case #" << t << ":";
		in >> k >> c >> s;
		v.clear();
		if (c == 1)
		{
			for (int i = 1; i <= k; i++)
				v.push_back(i);
		}
		else if (k == 1)
		{
			v.push_back(1);
		}
		else
		{
			for (int i = 2; i <= k; i++)
				v.push_back(i);
		}

		for (int i = 0; i < v.size(); i++)
			out << " " << v.at(i);

		if (t < ncases)
			out << endl;
	}

	in.close();
	out.close();
	return 0;
}