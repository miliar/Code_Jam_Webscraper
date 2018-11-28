#include <iostream>
#include <fstream>
#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;

ifstream fin("t.txt");
ofstream fout("out.txt");

int r, c, w;
int main()
{
	int t;
	fin >> t;
	for (int k = 1; k <= t; k++)
	{
		fout << "Case #" << k << ": ";
		fin >> r >> c >> w;
		if (w == c) {fout << w << "\n"; continue;	}
		if (w == 1) { fout << r*c << "\n"; continue; }
		int ans = c / w;
		if (c%w == 0) ans += w - 1;
		else ans += w;
		fout << ans << "\n";
	}
}