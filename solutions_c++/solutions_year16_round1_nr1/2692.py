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
	for (int icase = 0; icase < ncase; icase++)
	{
		string s; cin >> s;
		string ans;
		ans.push_back(s[0]);
		for (int i = 1; i < s.size(); i++)
		{
			if (string(1, s[i]) + ans < ans + string(1, s[i]))
			{
				ans = ans + string(1, s[i]);
			}
			else
			{
				ans = string(1, s[i]) + ans;
			}
		}

		cout << "Case #" << icase + 1 << ": " << ans <<endl;
	}

}