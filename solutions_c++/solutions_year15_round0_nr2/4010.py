#include <fstream>
#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

int rec(vector<int>& cakes, int i, int maxi)
{
	if (i > cakes.size() - 1) return maxi;
	int best = -1;
	for (int d = 1; d <= cakes[i]; d++)
	{
		int val = cakes[i] + d - 1;
		val /= d;
		int c = d - 1 + rec(cakes, i + 1, max(maxi, val));
		if (best == -1 || c < best)
			best = c;
	}
	return best;
}

void run(istream& inf, ostream &outf)
{
	int d;
	inf >> d;
	vector<int> cakes(d);
	for (int i = 0; i < d; i++)
		inf >> cakes[i];
	sort(cakes.begin(), cakes.end());
	reverse(cakes.begin(), cakes.end());
	outf << rec(cakes, 0, 0) << endl;
}

int main()
{
	ifstream inf("D:/Downloads/a-small.in");
	ofstream outf("D:/Downloads/a-small.out");

	int t;
	inf >> t;
	for (int i = 0; i < t; i++)
	{
		outf << "Case #" << (i + 1) << ": ";
		run(inf, outf);
	}

	return 0;
}