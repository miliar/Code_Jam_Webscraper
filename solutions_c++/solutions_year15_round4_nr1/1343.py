#include <iostream>
#include <string>
using namespace std;

int h, w;
char a[100][100];

struct point { int x, y; };

int result(point p)
{
	int ok = -1;
	for(int x = p.x - 1; x >= 0; --x) if(a[x][p.y] != '.')
	{
		if(a[p.x][p.y] == '<')
			return 0;
		ok = 1;
	}
	for(int y = p.y - 1; y >= 0; --y) if(a[p.x][y] != '.')
	{
		if(a[p.x][p.y] == '^')
			return 0;
		ok = 1;
	}
	for(int x = p.x + 1; x < w; ++x) if(a[x][p.y] != '.')
	{
		if(a[p.x][p.y] == '>')
			return 0;
		ok = 1;
	}
	for(int y = p.y + 1; y < h; ++y) if(a[p.x][y] != '.')
	{
		if(a[p.x][p.y] == 'v')
			return 0;
		ok = 1;
	}
	return ok;
}

void solve()
{
	cin >> h >> w;
	for(int y = 0; y < h; ++y) for(int x = 0; x < w; ++x)
		cin >> a[x][y];
	int count = 0;
	for(int y = 0; y < h; ++y) for(int x = 0; x < w; ++x) if(a[x][y] != '.')
	{
		int r = result({x,y});
		if(r == -1)
		{
			cout << "IMPOSSIBLE";
			return;
		}
		count += r;
	}
	cout << count;
}

int main()
{
	int t; cin >> t;
	for(int i = 1; i <= t; ++i)
	{
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
	return 0;
}
