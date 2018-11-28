#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

const int MAX_PAN = 1000;

ifstream lire("large.in", ios::in);
ofstream ecrire("out.txt", ios::out);

int main()
{
	int T;
	lire >> T;
	for (int t = 1; t <= T; t++)
	{
		int D;
		lire >> D;
		int s = MAX_PAN;
		vector<int> p(MAX_PAN + 1, 0);
		for (int k = 1; k <= D; k++)
		{
			int a;
			lire >> a;
			p[a]++;
		}
		for (int k = 1; k <= MAX_PAN; k++)
		{
			int r = k;
			for (int i = k + 1; i <= MAX_PAN; i++)
				r += p[i] * (i / k - ((i % k) == 0));
			s = min(s, r);
		}
		ecrire << "Case #" << t << ": " << s << endl;
	}
	return 0;
}
