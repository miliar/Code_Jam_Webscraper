#include<iostream>
#include<cstdio>
#include<string>
#include<set>
#include<algorithm>
#include<vector>
#include<map>
#include<cmath>
#include<queue>
#include<time.h>
using namespace std;

const int N = 200;
int row[N][N];
int ans[N][N];
bool used[N];

void solve()
{
	int n;
	cin >> n;

	map<int, int> cnt;
	int m = 2 * n;
	for (int i = 0; i < m - 1; i++)
		for (int j = 0; j < n; j++)
		{
			cin >> row[i][j];
			cnt[row[i][j]]++;
		}

	int pos = 0;
	for (auto p : cnt)
	{
		if (p.second % 2)
			row[m - 1][pos++] = p.first;
	}
	sort(row[m - 1], row[m - 1] + n);

	for (int i = 0; i < n; i++)
		cout << row[m - 1][i] << " ";

	/*for (int i = 0; i < m; i++)
		used[i] = false;

	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			ans[i][j] = 0;

	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
		{
			set<int> can1, can2;

			for (int k = 0; k < m; k++)
			{
				bool ok = true;
				for (int c = 0; c < n; c++)
					if (ans[i][c] != 0 && ans[i][c] != row[k][c])
						ok = false;
				if (ok)
					can1.insert(row[k][j]);

				ok = true;
				for (int r = 0; r < n; r++)
					if (ans[r][j] != 0 && ans[r][j] != row[k][r])
						ok = false;
				if (ok)
					can2.insert(row[k][i]);
			}

			set<int> can;
			for (auto x : can1)
				if (can2.count(x))
					can.insert(x);

			if (can.size() == 0)
			{
				cout << "ERROR";
				exit(0);
			}

			ans[i][j] = *can.begin();
		}

	for (int i = 0)*/
}

int main()
{
#ifdef LOCAL
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	long long T;
	cin >> T;
	for (long long t = 1; t <= T; t++)
	{
		cout << "Case #" << t << ": ";
		solve();
		cout << endl;
		cerr << t << " " << 1.0 * clock() / CLOCKS_PER_SEC << endl;
	}
}