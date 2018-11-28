#include <bits/stdc++.h>
using namespace std;

int n, m;
string grid[101];

int dx[] = {1, -1, 0, 0, 0};
int dy[] = {0, 0, 1, -1, 0};

int toDir(char c)
{
	if(c == 'v') return 0;
	if(c == '^') return 1;
	if(c == '>') return 2;
	if(c == '<') return 3;
	if(c == '.') return 4;
	return -1;
}

bool inBoard(int i, int j)
{
	if(i < 0) return false;
	if(i >= n) return false;
	if(j < 0) return false;
	if(j >= m) return false;
	return true;
}

bool goingOut(int i, int j, int dir)
{
	//cout << i << " " << j << " " << dir << endl;
	i += dx[dir];
	j += dy[dir];
	while(inBoard(i, j))
	{
		if(grid[i][j] != '.')
			return false;
		i += dx[dir];
		j += dy[dir];
	}
	//cout << "out: " << i << " " << j << endl;
	return true;
}


void solve()
{
	cin >> n >> m;
	for(int i = 0; i < n; i++)
		cin >> grid[i];
	int needs = 0;
	bool bad = false;
	for(int i = 0; i < n; i++)
		for(int j = 0; j < m; j++)
			if(grid[i][j] != '.')
				if(goingOut(i, j, toDir(grid[i][j])))
				{
					needs ++;
					bool ok = false;
					for(int k = 0; k < 4; k++)
						if(!goingOut(i, j, k))
							ok = true;
					if(!ok)
						bad = true;
				}
	if(bad)
		cout << "IMPOSSIBLE" << endl;
	else
		cout << needs << endl;
}

int MAIN()
{
	int TestCase;
	cin >> TestCase;
	for(int caseID = 1; caseID <= TestCase; caseID ++)
	{
		cout << "Case #" << caseID << ": ";
		solve();
	}
	return 0;
}

int main()
{
	int start = clock();
	#ifdef LOCAL_TEST
		freopen("in.txt", "r", stdin);
		freopen("out.txt", "w", stdout);
	#endif
	ios :: sync_with_stdio(false);
	cout << fixed << setprecision(16);
	int ret = MAIN();
	#ifdef LOCAL_TEST
		cout << "[Finished in " << clock() - start << " ms]" << endl;
	#endif
	return ret;
}
