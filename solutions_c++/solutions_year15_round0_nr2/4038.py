#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;
ifstream fin("t.txt");
ofstream fout("out.txt");
int d, c[1005];
int x,maxim;
int main()
{
	int T;
	fin >> T;
	for (int k = 1; k <= T; k++)
	{
		 maxim = 0;
		fout << "Case #" << k << ": ";
		fin >> d;
		for (int i = 1; i <= d; i++)
		{
			fin >> x;
			c[x]++;
			maxim = max(maxim, x);
		}
		int ans = maxim;
		int till = 0;
		for (int i = maxim; i > 1; i--)
		{
			if (c[i] != 0)
			{
				if (till + i < ans) ans = till + i;
				till += c[i];
				if (i == 9) {
					if (c[i] == 1)
					{
						if (c[4] == 0 && c[5] == 0 ) { c[6]++; c[3]++; }
						else { c[4]++; c[5]++; }
					}
					else { c[4] += c[i]; c[5] += c[i]; }
				}
				else{
					if (i % 2 == 0) c[i / 2] += 2 * c[i];
					else { c[i / 2] += c[i]; c[i / 2 + 1] += c[i]; }
				}
				c[i] = 0;
			}
		}
		fout << ans << "\n";
		for (int i = 1; i <= maxim; i++) c[i] = 0;
	}
}