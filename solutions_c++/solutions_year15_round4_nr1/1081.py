		//	   - -- --- ---- -----be name khoda----- ---- --- -- -		\\

#include <bits/stdc++.h>
using namespace std;

inline int in() { int x; scanf("%d", &x); return x; }
const int N = 2002;

char a[N][N];
int mark[N][N], tt[N][N];

int main()
{
	int _ = in();
	for(int i = 1; i <= _; i++)
	{
		printf("Case #%d: ", i);
		int n = in(), m = in();
		for(int i = 0; i < n; i++)
			for(int j = 0; j < m; j++)
				cin >> a[i][j];
		int cmp = 0;
		for(int i = 0; i < n; i++)
			for(int j = 0; j < m; j++)
				if(a[i][j] != '.')
				{
					int x = i;
					int y = j;
					int stx = 0, sty = 0;
					int t = 0;
					if(a[i][j] == 'v')
						stx = 1;
					if(a[i][j] == '^')
						stx = -1;
					if(a[i][j] == '>')
						sty = 1;
					if(a[i][j] == '<')
						sty = -1;
					x += stx;
					y += sty;
					while(min(x, y) >= 0 && x < n && y < m)
					{
						t += bool(a[x][y] != '.');
						x += stx;
						y += sty;
					}
					if(!t)
					{
						cmp++;
						int c = 0;
						int hoy = 0;
						for(int x = i + 1; x < n; x++)
							hoy |= (a[x][j] != '.');
						for(int x = 0; x < i; x++)
							hoy |= (a[x][j] != '.');
						for(int x = j + 1; x < m; x++)
							hoy |= (a[i][x] != '.');
						for(int x = 0; x < j; x++)
							hoy |= (a[i][x] != '.');
						if(!hoy)
							cmp = -1e8;
					}
				}
		if(cmp < 0)
			cout << "IMPOSSIBLE\n";
		else
			cout << cmp << endl;
	}
}
