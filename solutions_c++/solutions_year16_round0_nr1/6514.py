#include <iostream>
#include <string>
#include <map>
#include <algorithm>
#include <fstream>

using namespace std;

map<int, bool> vis;

int getVisCount(long long x)
{
	int res = 0;
	while (x > 0)
	{
		int d = x % 10;
		x /= 10;
		if (!vis[d])
		{
			vis[d] = true;
			res++;
		}
	}
	return res;
}


int main()
{
	ifstream cin("A-large.in");
	ofstream cout("output.txt");

	int n;
	cin >> n;
	
	for (int ci = 1; ci <= n; ci++)
	{
		vis.clear();
		long long x;
		cin >> x;

		if (x == 0)
		{
			cout << "Case #" << ci << ": INSOMNIA" << endl;
			continue;
		}

		long long cur = x;
		int curVis = getVisCount(cur);
		int i = 1;

		while (curVis < 10)
		{
			cur = x * (++i);
			curVis += getVisCount(cur);
		}

		cout << "Case #" << ci << ": " << cur << endl;
	}


}