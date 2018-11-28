#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <sstream>

using namespace std;

int main()
{
	int ncases;
	unsigned long long ni, c, res, ntest;
	int check[10];
	bool cont;
	string ns;
	ifstream in;
	ofstream out;

	in.open("A-large.in");
	out.open("A-large-results.out");
	in >> ncases;

	for (int t = 1; t <= ncases; t++)
	{
		ns.clear();
		memset(check, 0, sizeof(int) * 10);
		out << "Case #" << t << ": ";
		in >> ni;
		ntest = ni;
		ns = to_string(ni);
		cont = true;
		c = 2;

		if (ni != 0)
		{
			while (cont)
			{
				res = ntest;
				for (int i = 0; i < ns.length(); i++)
				{
					check[int(ns.at(i) - 48)]++;
				}

				for (int i = 0; i < 10; i++)
				{
					if (check[i] == 0)
						break;
					else if (check[i] > 0 && i == 9)
						cont = false;
				}

				ntest = ni*c;
				ns = to_string(ntest);
				c++;
			}

			out << res;
		}
		else
		{
			out << "INSOMNIA";
		}

		if (t < ncases)
			out << endl;
	}

	in.close();
	out.close();
	return 0;
}