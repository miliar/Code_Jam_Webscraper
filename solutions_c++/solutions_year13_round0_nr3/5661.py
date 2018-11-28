#include <iostream>
#include <sstream>
#include <fstream>
#include <cmath>

using namespace std;

string f(int a)
{
	stringstream sout;
	sout << a;
	return sout.str();
}

main()
{
	ifstream fin("C-small-attempt0.in");
	ofstream fout("C-small-attempt0.txt");
	int t;
	fin >> t;
	for (int cnt = 1; cnt <= t; ++cnt)
	{
		int a, b, c = 0;
		fin >> a >> b;
		for (int i = a; i <= b; ++i)
		{
			int j = sqrt(i);
			if (j * j == i)
			{
				string s = f(i), t = f(j), ss = "", tt = "";
				for (int k = 0; k != s.size(); ++k)
					ss = s[k] + ss;
				for (int k = 0; k != t.size(); ++k)
					tt = t[k] + tt;
				if (s == ss && t == tt)
					++c;
			}
		}
		fout << "Case #" << cnt << ": " << c << endl;
	}
}
