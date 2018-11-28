#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <set>
#include <vector>
#include <queue>
#include <map>
using namespace std;

#define forn(i, n) for(int i = 0; i < ((int) n); i++)

string tab[128];

int dx[4]={1,0,0,-1}, dy[4]={0,1,-1,0};

int R, C;

bool enRango(int i, int j)
{
	return (i>=0 && i<R && j>=0 && j<C);
}

bool move(int i, int j, int d)
{
	int ni=i+dx[d], nj=j+dy[d];
	while(enRango(ni, nj) && tab[ni][nj]=='.')
	{
		ni=ni+dx[d], nj=nj+dy[d];
	}
	return enRango(ni, nj);
}

int getd(char c)
{
	if(c=='.') return 4;
	if(c=='v') return 0;
	if(c=='>') return 1;
	if(c=='<') return 2;
	return 3;
}

int main()
{	
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	int T;
	cin >> T;
	
	forn(tc, T)
	{
		cin >> R >> C;
		
		forn(i, R) cin >> tab[i];
		
		int ans=0;
		forn(i, R) forn(j, C)
		{	
			int k = getd(tab[i][j]);
			if(k!=4 && !move(i, j, k))
			{
				int anda=0;
				forn(d, 4)
				{
					if(move(i, j, d)) anda=1;
				}
			
				if(!anda){ ans = -1; break; }
				ans++;
			}
		}
		
		cout << "Case #" << tc+1 << ": ";
		if(ans == -1) cout << "IMPOSSIBLE" << endl; else cout << ans << endl;
	}
	
}
