#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
	ifstream in("in.txt");
	//cin.rdbuf(in.rdbuf());

	int t;
	cin >> t;
	for (int tc = 1; tc <= t; tc++)
	{
		int x, r, c;
		bool rich = false;

		cin >> x >> r >> c;

		if (((r*c) % x) != 0)
		{
			rich = true;
		}
		else if (x >= 7)
		{
			rich = true;
		}

		for (int i = 1; i < x; i++)
		{
			if (r < i || c < i)
				rich = true;
		}

		cout << "Case #" << tc << ": " << (rich ? "RICHARD" : "GABRIEL") << endl;
	}

	return 0;
}
