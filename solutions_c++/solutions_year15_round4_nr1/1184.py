/*#include <iostream>
#include <fstream>
#include <sstream>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <vector>
#include <iomanip>
#include <cmath>
#include <algorithm>
#include <numeric>
#include <iterator>

using namespace std;

ifstream in("A0.in");
ofstream out("A0.out");

int main()
{
	char temp[10000];
	int test;
	in >> test;
	for (int t = 1; t <= test; ++t)
	{
		int n;
		in >> n;
		vector < vector <string> > s;
		in.getline(temp, 10000);
		for (int i = 0; i < n; ++i)
		{
			string str, st;
			getline(in, str);
			istringstream read(str);
			while (read >> st)
			{
				s[i].push_back(st);
			}
		}

		set <string> english;
		set <string> french;
		for (int i = 0; i < s[0].size(); ++i)
			english.insert(s[0][i]);
		for (int i = 0; i < s[1].size(); ++i)
			french.insert(s[1][i]);

		for (int x = 0; x < (1 << (n - 2)); ++x)
		{
			for (int i = 0; i < n - 2; ++i)
			{
				if (x & (1 << i))
				{

				}
			}
		}
	}
	return 0;
}*/
//#include <iostream>
#include <fstream>
#include <sstream>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <vector>
#include <iomanip>
#include <cmath>
#include <algorithm>
#include <numeric>
#include <iterator>

using namespace std;

ifstream cin("A2.in");
ofstream cout("A2.out");

int main()
{
	
	int test;
	cin >> test;
	for (int t = 1; t <= test; ++t)
	{
		int n, m, ans = 0;
		cin >> n >> m;
		vector < string > v(n);
		for (int i = 0; i < n; ++i)
			cin >> v[i];
		bool impossible = false;
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < m; ++j)
			{
				if (v[i][j] != '.')
				{
					int di[] = { 0, 0, -1, 1 };
					int dj[] = { -1, 1, 0, 0 };
					int k;
					if (v[i][j] == '<')
						k = 0;
					if (v[i][j] == '>')
						k = 1;
					if (v[i][j] == '^')
						k = 2;
					if (v[i][j] == 'v')
						k = 3;

					bool bad = true;
					for (int ii = i + di[k], jj = j + dj[k];
						ii < n && ii >= 0 && jj < m && jj >= 0;
						ii += di[k], jj += dj[k]) {
						if (v[ii][jj] != '.') {
							bad = false;
						}
					}

					if (!bad)
						continue;

					ans++;

					bool alone = true;
					for (k = 0; k < 4; k++) {
						for (int ii = i + di[k], jj = j + dj[k];
							ii < n && ii >= 0 && jj < m && jj >= 0;
							ii += di[k], jj += dj[k]) {
							if (v[ii][jj] != '.') {
								alone = false;
							}
						}
					}

					if (alone)
						impossible = true;
				}
			}
		}
		printf("Case #%d: ", t);
		if (impossible)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", ans);
	}
	return 0;
}