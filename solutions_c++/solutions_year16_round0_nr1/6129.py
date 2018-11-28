#include <iostream>
#include <cstdio>
#include <vector>
#include <fstream>
#include <sstream>
#include <cassert>
#include <queue>
#include <cassert>
#include <map>
#include <cstdlib>
#include <algorithm>
#include <set>

using namespace std;

int main()
{
#if _JOE_PC
	freopen("in.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int ncase; cin >> ncase;
	set<char> seen;
	for (int icase = 0; icase < ncase; icase++)
	{
		set<char> seen;
		long long int n; cin >> n;
		for (int i = 1; i < 10e3; i++)
		{
			stringstream ss;
			ss << n *i;
			string s = ss.str();
			for (int i = 0; i < s.size(); i++)
			{
				seen.insert(s[i]);
			}
			if (seen.size() == 10)
			{
				cout << "Case #" << icase + 1 << ": " << (i) *n << endl;
				break;
			}
		}
		if (seen.size() != 10)
		{
			cout << "Case #" << icase + 1 << ": INSOMNIA" << endl;
		}
	}
}