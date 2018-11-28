#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#define lol long long
using namespace std;

string filename = "d.in";
ifstream in(filename);
ofstream out(filename + "_out.txt");

#define cin in
#define cout out

int main()
{
	int t;
	cin >> t;

	for (int _i = 0; _i < t; ++_i)
	{
		cout << "Case #" << _i + 1 << ": ";
		int n;
		cin >> n;
		vector<string> a_(n);
		for (int i = 0; i < n; ++i)
			cin >> a_[i];

		int mxMask = 1 << (n * n);
		int best = 16;
		for (int mask = 0; mask < mxMask; ++mask)
		{
			vector<int> a(n * n);
			int y = mask;
			for (int u = 0; u < n * n; ++u)
			{
				a[u] = y & 1;
				y >>= 1;
			}
			int ch = 0;
			bool blya = 0;
			for (int i = 0; i < n; ++i)
			for (int j = 0; j < n; ++j)
			{
				if (a_[i][j] - '0' == 0 && a[i * n + j] == 1)
					++ch;
				if (a_[i][j] - '0' == 1 && a[i * n + j] == 0)
					blya = 1;
			}
			if (blya)
				continue;
			vector<vector<int> > b(n, vector<int>(n));
			for (int i = 0; i < n; ++i)
			for (int j = 0; j < n; ++j)
				b[i][j] = a[i * n + j];

			vector<int> perm(n);
			for (int i = 0; i < n; ++i)
				perm[i] = i;
			bool fail = 0;
			do
			{
				vector<vector<int>> b_;
				for (int i = 0; i < n; ++i)
					b_.push_back(b[perm[i]]);
				vector<vector<int> > possible(1);
				for (int i = 0; i < n; ++i)
				{
					vector<vector<int>> np;
					for (int j = 0; j < possible.size(); ++j)
					{
						bool ok = 0;
						for (int h = 0; h < n; ++h)
							if (b_[i][h])
							{
								bool ww = 0;
								for (int y = 0; y < possible[j].size(); ++y)
									if (possible[j][y] == h)
									{
										ww = 1;
										break;
									}
								if (ww)
									continue;
								ok = 1;
								possible[j].push_back(h);
								np.push_back(possible[j]);
								possible[j].pop_back();
							}
						if (!ok)
							fail = 1;
						if (fail)
							break;
					}
					if (fail)
						break;
					possible = np;
				}
				if (fail)
					break;
			} while (next_permutation(perm.begin(), perm.end()));
			if (!fail)
				best = min(best, ch);
		}
		cout << best << endl;
	}
	return 0;
}
