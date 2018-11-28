#include <iostream>
#include <fstream>

using namespace std;

bool f(char c)
{
	return c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u';
}

main()
{
	ifstream fin("A-small-attempt0.in");
	ofstream fout("A-small-attempt0.txt");
	int t, n;
	string s;
	fin >> t;
	for (int cnt= 1; cnt <= t; ++cnt)
	{
		fin >> s >> n;
		int tot = 0;
		for (int i = 0; i != s.size(); ++i)
		{
			int c = 0, j = i;
			bool p = true;
			for ( ; j != s.size() + 1 && c < n; ++j)
			{
				if (f(s[j]))
				{
					p = true;
					++c;
				}
				else
				{
					c = 0;
					p = false;
				}
			}
			--j;
			if (j == s.size())
				continue;
			tot += s.size() - j;
			//cout << i << ' ' << j << ' ' << s.size() - j << endl;
		}
		fout << "Case #" << cnt << ": " << tot << endl;
	}
}
