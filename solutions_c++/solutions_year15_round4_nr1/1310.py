#include <fstream>
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int T;
int n, m;
const int MAXN = 105;
char a[MAXN][MAXN];
#define cin fin
#define cout fout
ifstream fin("a.in");
ofstream fout("a.out");

bool chk(int x, int y, int aa, int bb, bool ss = false)
{
//	cout<<x<<' '<<y<<' '<<aa<<' '<<bb<<endl;
	if(x <= 0||x>n||y<=0||y>m) return false;
	if(ss && a[x][y] != '.') return true;
	return chk(x+aa, y+bb, aa, bb, 1);
}

int main()
{
	cin>>T;
	for(int t = 1; t <= T; t++)
	{
		cin>>n>>m;
		for(int i = 1; i <= n; i++)
			for(int j = 1; j <= m; j++)
				cin>>a[i][j];//, cout<<a[i][j];
		bool ok = true;
		int ans = 0;
		for(int i = 1; i <= n; i++)
			for(int j = 1; j <= m; j++)
				if(ok)
				if(a[i][j] != '.')
				{
					if(a[i][j] == '^')
					{
						if(chk(i, j, -1, 0)) continue;
						if(chk(i, j, 1, 0) || chk(i, j, 0, 1) || chk(i, j, 0, -1) || chk(i, j, -1, 0)) ans++;
						else {ok = false;break;}
					}
					if(a[i][j] == '<')
					{
						if(chk(i, j, 0, -1)) continue;
						if(chk(i, j, 1, 0) || chk(i, j, 0, 1) || chk(i, j, 0, -1) || chk(i, j, -1, 0)) ans++;
						else {ok = false;break;}
					}
					if(a[i][j] == '>')
					{
						if(chk(i, j, 0, 1)) continue;
						if(chk(i, j, 1, 0) || chk(i, j, 0, 1) || chk(i, j, 0, -1) || chk(i, j, -1, 0)) ans++;
						else {ok = false;break;}
					}
					if(a[i][j] == 'v')
					{
						if(chk(i, j, 1, 0)) continue;
						if(chk(i, j, 1, 0) || chk(i, j, 0, 1) || chk(i, j, 0, -1) || chk(i, j, -1, 0)) ans++;
						else {ok = false;break;}
					}
				}
		cout << "Case #"<<t<<": ";
		if(ok == false) cout << "IMPOSSIBLE" << endl;
		else cout << ans << endl;
	}
	
	return 0;
}
/*
4
2 1
^
^
2 2
>v
^<
3 3
...
.^.
...
1 1
.

*/

