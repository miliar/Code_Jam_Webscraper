#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

#define ALL(c) (c).begin(), (c).end()

const int
	MAXC = 1 << 7;

int h[MAXC][MAXC];

int main()
{
	int testCount;
	cin >> testCount;

	for (int test = 1; test <= testCount; ++test)
	{
		int R, C;
		cin >> R >> C;

		vector< int > r[R], c[C];

		for (int i = 0; i < R; ++i)
		for (int j = 0; j < C; ++j)
		{
			cin >> h[i][j];
			r[i].push_back(h[i][j]);
			c[j].push_back(h[i][j]);
		}

		for (int i = 0; i < R; ++i)
			sort(ALL(r[i]));

		for (int i = 0; i < C; ++i)
			sort(ALL(c[i]));

		bool ok = true;

		for (int i = 0; i < R; ++i)
		for (int j = 0; j < C; ++j)
		{
			if (r[i].back() > h[i][j] && c[j].back() > h[i][j])
				ok = false;
		}

		cout << "Case #" << test  << ": " << (ok ? "YES" : "NO") << endl;
	}

	return 0;
}
