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
	vector<char> lw;
	string word;

	ifstream in;
	ofstream out;
	in.open("A/A-large.in");
	out.open("A/A-large-results.out");
	in >> ncases;

	for (int t = 1; t <= ncases; t++)
	{
		out << "Case #" << t << ": ";
		word.clear();
		lw.clear();
		in >> word;

		lw.push_back(word.at(0));
		if (word.length() > 1)
		{
			for (int i = 1; i < word.length(); i++)
			{
				if (int(word.at(i)) >= int(lw.at(0)))
				{
					lw.insert(lw.begin(), word.at(i));
				}
				else
				{
					lw.push_back(word.at(i));
				}
			}
		}

		for (int i = 0; i < word.length(); i++)
		{
			out << lw.at(i);
		}
		if (t < ncases)
			out << endl;
	}

	in.close();
	out.close();
	return 0;
}