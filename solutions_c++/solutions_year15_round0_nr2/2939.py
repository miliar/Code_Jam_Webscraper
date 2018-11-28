#include <iostream>
#include <fstream>
#include <cmath>
#include <set>
using namespace std;
int T, n, sol, v[1010];

int main()
{
	int t, i, j, x, now;
	multiset <int>::iterator it;
	ifstream fin("B.in");
	ofstream fout("B.out");
	fin >> T;
	for(t = 1; t <= T; ++t)
	{
		fin >> n;
		sol = 0;
		for(i = 1; i <= n; ++i)
		{
			fin >> x;
			v[i] = x;
			sol = max(sol, x);
		}
		for(i = sol; i > 0; --i)
		{
			now = i;
			for(j = 1; j <= n; ++j)
			{
				if(v[j] <= i)
					continue;
				if(v[j] % i == 0)
					now += (v[j] / i) - 1;
				else
					now += (v[j] / i);
			}
			sol = min(sol, now);
		}
		fout << "Case #" << t << ": " << sol << "\n";
	}
	fin.close();
	fout.close();
	return 0;
}
