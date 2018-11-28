#if 1
#include <iostream>
#include <cstdio>
#include <sstream>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <string>
#include <numeric>
#include <cstring>
#include <ctime>


using namespace std;
#define mp make_pair
#define X first
#define Y second
#define pb push_back

typedef pair<int, int> pii ;
typedef long long LL;
typedef long double LD;
typedef vector<int> vi;

const LL inf = 1e9;
const LD eps = 1e-9;

int sm[4][2] = {{0, -1}, {-1, 0}, {0, 1}, {1, 0}};
vector <vector <int> > used;
vector <vector<char> > a;
int W, H, B;
int st = 0;
bool dfs(int x, int y)
{
	used[x][y] = 1;
	if (y == H - 1)
		return true;
	for (int i = 0; i < 4; i++)
	{
		int nx = x + sm[(st + 3 + i) % 4][0];
		int ny = y + sm[(st + 3 + i) % 4][1];
		if (nx >= 0 && nx < W && ny >= 0 && ny < H && a[nx][ny] == ' ' && !used[nx][ny])
		{
			st = (st + 3 + i) % 4;
			if (dfs(nx, ny))
				return true;
		}
	}
	return false;
}
int main()        
{
    freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int q = 0; q < T; q++)
	{
		cerr << q << endl;
		scanf("%d %d %d", &W, &H, &B);
		a.assign(W, vector <char> (H, ' '));
		used.assign(W, vector <int> (H, 0));
		for (int i = 0; i < B; i++)
		{
			int x0, y0, x1, y1;
			scanf("%d %d %d %d", &x0, &y0, &x1, &y1);
			if (x1 < x0)
				swap(x1, x0);
			if (y1 < y0)
				swap(y0, y1);

			for (int j = x0; j <= x1; j++)
			{
				for (int k = y0; k <= y1; k++)
				{
					a[j][k] = 1;
				}
			}
		}

		int cnt = 0;
		for (int i = 0; i < W; i++)
		{
			if (a[i][0] == ' ' && !used[i][0])
			{
				st = 1;
				if(dfs(i, 0))
					cnt++;
			}
		}
		printf("Case #%d: %d\n", q + 1, cnt);
	}
    return 0;
}
#endif