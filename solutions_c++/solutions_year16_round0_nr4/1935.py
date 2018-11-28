//s == k
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

typedef unsigned long long ull;

vector<ull> solve(int k, int c, int s)
{
	vector<ull> v(s);
	for(int i = 0; i < s; i++)
	{
		ull x = i + 1;
		for(int j = 2; j <= c; j++)
		{
			x = k * (x - 1) + (i + 1);
		}
		v[i] = x;
	}
	return v;
}

int main()
{
	int t;
	int k, c, s;
	ifstream f("input.txt");
	ofstream g("output.txt");
	f >> t;
	for(int i = 1; i <= t; i++)
	{
		f >> k >> c >> s;
		g << "Case #" << i << ":";
		if(s != k)
		{
			g << " IMPOSSIBLE\n";
		}
		else
		{
			vector<ull> v = solve(k, c, s);		
			for(int tz = 0; tz < v.size(); tz++)
			{
				g << " " << v[tz];
			}
			g << "\n";
		}
	}
	f.close();
	g.close();
	return 0;
}
