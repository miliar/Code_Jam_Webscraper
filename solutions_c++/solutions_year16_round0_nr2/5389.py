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
int res;

string flip(string p, int start, int end)
{
	string t = p;
	for (int i = end; i >= 0; i--)
	{
		if (p.at(i) == '-')
			t.at(end - i) = '+';
		else
			t.at(end - i) = '-';
	}

	res++;
	return t;
}

int main()
{
	int ncases, cp, cm, cs, plen;
	string p;
	ifstream in;
	ofstream out;

	in.open("B/B-small-attempt0.in");
	out.open("B/B-small-results.out");
	in >> ncases;

	for (int t = 1; t <= ncases; t++)
	{
		res = 0;
		p.clear();
		cp = cm = 0;
		out << "Case #" << t << ": ";
		in >> p;
		plen = p.length();

		for (int i = 0; i < plen; i++)
		{
			if (p.at(i) == '+')
				cp++;
			else
				cm++;
		}

		if (cp == plen)
		{
			res = 0;
		}
		else if (cm == plen)
		{
			res = 1;
		}
		else
		{
			if (cp < cm)
			{
				int pos, neg;
				pos = neg = 0;
				if (p.at(0) != p.at(plen - 1))
				{
					if (p.at(plen - 1) == '-')
					{
						for (int i = 1; i < plen - 1; i++)
						{
							if (p.at(i) == '+')
								pos++;
							else
								break;
						}
						for (int i = plen - 1; i >= 1; i--)
						{
							if (p.at(i) == '-')
								neg++;
							else
								break;
						}
						if (neg <= pos)
							flip(p, 0, plen - 1);
					}
				}
			}

			int i;
			char cc = p.at(0);
			cs = 1;

			while (true)
			{
				for (i = cs; i < plen; i++)
				{
					if (cc == p.at(i))
					{
						cs++;
					}
					else
					{
						cc = p.at(i);
						break;
					}
				}
				if (cs == plen)
					break;
				else
					flip(p, 0, cs - 1);
			}
			if (p.at(plen - 1) == '-')
				res++;
		}

		out << res;
		if (t < ncases)
			out << endl;
	}

	in.close();
	out.close();
	return 0;
}