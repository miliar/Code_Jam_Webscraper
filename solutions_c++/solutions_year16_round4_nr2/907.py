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

string filename = "b.in";
ifstream in(filename);
ofstream out(filename + "_out.txt");

#define cin in
#define cout out

int cnk[20][20];

int main()
{
	for (int i = 0; i < 20; ++i)
		cnk[i][0] = 1;

	for (int i = 1; i < 20; ++i)
		for (int j = 1; j <= i; ++j)
			cnk[i][j] = cnk[i - 1][j] + cnk[i - 1][j - 1];

	//ios_base::sync_with_stdio(0);
	//cin.tie(0);
	int t;
	cin >> t;

	for (int i = 0; i < t; ++i)
	{
		cout << "Case #" << i + 1 << ": ";
		int n, k;
		cin >> n >> k;
		vector<double> p(n);
		for (int i = 0; i < n; ++i)
			cin >> p[i];
		vector<int> perm(n, 0);
		for (int j = n - k; j < n; ++j)
			perm[j] = 1;
		double ans = 0;
		int k2 = 1;
		for (int _ = 0; _ < k; ++_)
			k2 *= 2;
		do
		{
			vector<double> a;
			for (int j = 0; j < n; ++j)
				if (perm[j])
					a.push_back(p[j]);

			vector<double> sm(k + 1, 0);
			
			for (int mask = 0; mask < k2; ++mask)
			{
				int m2 = mask;
				vector<int> f;
				int howmuch = 0;
				double cv = 1;
				for (int h = 0; h < k; ++h)
				{
					int c = m2 & 1;
					m2 >>= 1;
					howmuch += c;
					if (c)
						cv *= a[h];
				}
				sm[howmuch] += cv;
			}
			double ca = 0;
			for (int x = k / 2; x <= k; ++x)
			{
				if ((x - k / 2) % 2 == 1)
					ca += sm[x] * cnk[x][x - k / 2];
				else
					ca -= sm[x] * cnk[x][x - k / 2];
			}
			if (ca < 0)
				ca *= -1;
			ans = max(ans, ca);
		} while (next_permutation(perm.begin(), perm.end()));
		cout.precision(15);
		cout << fixed << ans << endl;
	}
	return 0;
}
