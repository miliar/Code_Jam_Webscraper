#include <bits/stdc++.h>
using namespace std;

#define jjs(i, s, x) for (int i = (s); i < int(x); i++)
#define jjl(i, x) jjs(i, 0, x)
#define ji(x) jjl(i, x)
#define jj(x) jjl(j, x)
#define jk(x) jjl(k, x)
#define jij(a, b) ji(a) jj(b)
#define ever ;;
#define foreach(x, C) for (auto& x : (C))
#define INF ((int) 1e9+10)
#define LINF ((ll) 1e16)
#define pb push_back
#define mp make_pair
#define nrint(x) int x; rint(x);
#define nrlong(x) long long x; rint(x);
#define rfloat(x) scanf("%lf", &(x))

#ifndef ONLINE_JUDGE
const bool DEBUG = true;
#define Db(x...)   ({ if (DEBUG) { cout << "Debug["; DB, #x, ":", x, "]\n"; } })
template<class T> void Dbrng(T lo, T hi, string note = "", int w = 0) {
  if (DEBUG) {  
    cout << "Debug[ ";
    if (!note.empty()) cout << setw(3) << note << " : ";
    for (; lo != hi; ++lo) cout << setw(w) << *lo << " ";
    cout << "]" << endl;
  }
}
struct Debugger { template<class T> Debugger& operator ,
  (const T & v) { cout << " " << v << flush; return *this; } } DB;
#else
const bool DEBUG = false;
#define Db(x...)
#endif

#define rint readInteger
template<typename T>
bool readInteger(T& x)
{
	char c,r=0,n=0;
	x=0;
	for (ever)
	{
		c=getchar();
		if ((c<0) && (!r))
			return(0);
		else if ((c=='-') && (!r))
			n=1;
		else if ((c>='0') && (c<='9'))
			x=x*10+c-'0',r=1;
		else if (r)
			break;
	}
	if (n)
		x=-x;
	return(1);
}

const int MOD = 1000000007;
typedef long long ll;
typedef pair<int, int> pi;

const int MX = 110;
char grid[MX][MX];
bool poss[MX][MX][4];
int R, C;
bool died;

const char* vstr = "^>v<.";
int iof(char c)
{
	ji(5) if (vstr[i] == c)
		return i;
	assert(false);
}

pi follow(int x, int y, int dx, int dy)
{
	while (x >= 0 && y >= 0 && x < R && y < C)
	{
		if (grid[x][y] != '.')
			return {x, y};
		x += dx;
		y += dy;
	}
	return {-1, -1};
}

void unAllow(int x, int y, int dx, int dy, int idx)
{
	pi v = follow(x, y, dx, dy);
	// Db(x, y, dx, dy, idx, v.first, v.second);
	if (v.first < 0)
		;
	else
	{
		// if (idx == iof(grid[v.first][v.second]))
			// printf("%d %d %d %d -> mark %d %d %d\n", x, y, dx, dy, v.first, v.second, idx);
		poss[v.first][v.second][idx] = false;
	}
}

int main()
{
	nrint(T);
	jjl(test, T)
	{
		rint(R); rint(C);
		ji(R) scanf("%s", grid[i]);
		jij(R, C) jk(4) poss[i][j][k] = true;
		died = false;
		jij(R, C)
		{
			if (i == 0)
				unAllow(i, j, 1, 0, 0);
			if (j == 0)
				unAllow(i, j, 0, 1, 3);
			if (i == R-1)
				unAllow(i, j, -1, 0, 2);
			if (j == C-1)
				unAllow(i, j, 0, -1, 1);
		}
		int changed = 0;
		bool anyArrows = false;
		jij(R, C)
		{
			bool any = false;
			jk(4) any |= poss[i][j][k];
			if (!any) died = true;
			changed += !poss[i][j][iof(grid[i][j])] && grid[i][j] != '.';
			anyArrows |= grid[i][j] != '.';
		}
		if (!anyArrows) died = false;
		// ji(R) printf("%s\n", grid[i]);
		printf("Case #%d: ", test + 1);
		if (died) printf("IMPOSSIBLE\n");
		else printf("%d\n", changed);
	}
}
