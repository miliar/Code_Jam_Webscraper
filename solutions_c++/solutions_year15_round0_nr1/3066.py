#include <iostream>
#include <fstream>
using namespace std;
int T, n, sol;
char s[1010];

int main()
{
	int i, t, now;
	ifstream fin("A.in");
	ofstream fout("A.out");
	fin >> T;
	for(t = 1; t <= T; ++t)
	{
		fin >> n;
		fin >> s;
		now = sol = 0;
		for(i = 0; i <= n; ++i)
		{
			if(s[i] - '0' == 0)
				continue;
			if(now >= i)
				now += s[i] - '0';
			else
			{
				sol += (i - now);
				now = i + s[i] - '0';
			}
		}
		fout << "Case #" << t << ": " << sol << "\n";
	}
	fin.close();
	fout.close();
	return 0;
}
