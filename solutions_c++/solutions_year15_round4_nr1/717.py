#include <bits/stdc++.h>
#define f(i,x,y) for (int i = x; i < y; i++)
#define fd(i,x,y) for(int i = x; i>= y; i--)
#define FOR(it,A) for(typeof A.begin() it = A.begin(); it!=A.end(); it++)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define vint vector<int>
#define ll long long
#define clr(A,x) memset(A, x, sizeof A)
#define pb push_back
#define pii pair<int,int>
#define fst first
#define snd second
#define ones(x) __builtin_popcount(x)
#define cua(x) (x)*(x)
#define eps (1e-9)
#define oo (1<<30)
#define debug(x) cout <<#x << " = " << x << endl
#define adebug(x,n) cout <<#x<<endl; f(i,0,n)cout<<x[i]<<char(i+1==n?10:32)
#define mdebug(x,m,n) cout <<#x<<endl; f(i,0,m)f(j,0,n)cout<<x[i][j]<<char(j+1==n?10:32)
#define N 1
using namespace std;
template<class T> inline void mini(T &a,T b){if(b<a) a=b;}
template<class T> inline void maxi(T &a,T b){if(b>a) a=b;}
int dx[4] = {1,-1,0,0};
int dy[4] = {0,0,1,-1};

int who(char x)
{
	return x=='.'? -1 : x=='v'? 0 : x=='^'? 1 : x=='>'? 2 : 3;
}

int tc,caso;
string M[100];
int a[100][100];
int r,c;

int good(int x, int y)
{
	return 0 <= x && x < r && 0 <= y && y < c;
}

int main()
{
	cin >> tc;
	while(tc--)
	{
		cin >> r >> c;
		f(i,0,r) cin >> M[i];
		f(i,0,r) f(j,0,c) a[i][j] = who(M[i][j]);

		int imp = 0, bad = 0;
//		mdebug(a, r, c);
		f(i,0,r) f(j,0,c) if (~a[i][j])
		{
			int k = a[i][j];
			int x = i, y = j;
			int ok = 0;
			while (1)
			{
				x += dx[k];
				y += dy[k];

				if (!good(x,y)) break;
				if (a[x][y] != -1)
				{
					ok = 1;
					break;
				}
			}
			if (!ok) bad ++;

			int possibles = 0;
			f(kk,0,4) 
			{
				ok = 0;
				x = i; y = j;
				while(1)
				{
					x += dx[kk];
					y += dy[kk];
					if (!good(x,y)) break;

					if (~a[x][y])
					{
						ok = 1;
						break;
					}
				}
				if (ok) possibles ++;
			}
			if (!possibles) imp = 1;
		}

		printf("Case #%d: ", ++caso);

		if (imp) puts("IMPOSSIBLE");
		else
		{
			printf("%d\n", bad);
		}
	}
}

