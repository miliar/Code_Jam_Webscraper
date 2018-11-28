#pragma warning( disable : 4996)
#define _USE_MATH_DEFINES
#pragma comment(linker, "/STACK:666000000")

#define bublic public

#include <algorithm>
#include <assert.h>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits.h>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <time.h>
#include <vector>
#include <stack>

#define nextLine() {for(int c=getchar(); c!='\n' && c!=EOF; c=getchar());}
#define sqr(a) ((a)*(a))
#define has(mask,i) (((mask) & (1<<(i))) == 0 ? false : true)
#define set_true(mask, i) (mask|(1<<(i)))
#define set_false(mask, i) (~((~mask)|(1<<(i))))

#define Equal(a, b) (fabsl(a-b) < 1e-9)
#define Less(a, b) (a < b && !Equal(a, b))
#define Greater(a, b) (a > b && !Equal(a, b))

using namespace std;

#ifdef SCHULLZ
#define TASK "file"
#define eprintf(...) fprintf(stdout, __VA_ARGS__)
#define parr(a,n,m) for(int i=0;i<n;i++){for(int j=0;j<m;j++)cout<<a[i][j]<<" ";puts("");}puts("");
#define log(x) cout << #x << " = " << x << endl
#else
#define TASK "file"
#define eprintf(...) 
#define parr(a,n,m)
#define log(x)
#endif

#define pb(_o_) push_back(_o_)

typedef long long LL;
typedef unsigned long long ULL;
typedef long double ldb;

typedef pair<int,int> pii;
typedef pair<pii,int> tiii;
typedef pair<pii,pii> fiiii;
#define aaa first.first
#define bbb first.second
#define ccc second.first
#define ddd second.second
#define mp(x, y) make_pair(x, y)
#define mpp(x, y, z) make_pair(mp(x, y), z)
#define mppp(x, y, z, a) make_pair(mp(x, y), mp(z, a))

#define sci(a) (1 == scanf("%d", &a))
#define scii(a,b) (2 == scanf("%d%d", &a, &b))
#define sciii(a,b,c) (3 == scanf("%d%d%d", &a, &b, &c))
#define sciiii(a,b,c,d) (4 == scanf("%d%d%d%d", &a, &b, &c, &d))
#define sciiiii(a,b,c,d,e) (5 == scanf("%d%d%d%d%d", &a, &b, &c, &d, &e))

#define scin(a) (1 == scanf("%d\n", &a))
#define sciin(a,b) (2 == scanf("%d%d\n", &a, &b))
#define sciiin(a,b,c) (3 == scanf("%d%d%d\n", &a, &b, &c))
#define sciiiin(a,b,c,d) (4 == scanf("%d%d%d%d\n", &a, &b, &c, &d))
#define sciiiiin(a,b,c,d,e) (5 == scanf("%d%d%d%d%d\n", &a, &b, &c, &d, &e))

#define FORN(i,n) for(int i = 0; i < (int)(n); i++)
#define FORR(i,n) for(int i = n - 1; i >= 0; i--)
#define FORS(it,a) for(auto it = a.begin(); it != a.end(); it++)
#define fill(a,v) memset(a,v,sizeof(a))
#define all(A) A.begin(),A.end()

typedef vector<int> vi;
typedef vector<vi> vvi;

#ifdef SCHULLZ
typedef vector<int> vc;
typedef vector<vc> vvc;
#else
typedef vector<char> vc;
typedef vector<char> vvc;
#endif

const int INF = (1 << 30) - 1;
const ldb EPS = 1e-9;

void ML(const bool v)
{
	if (v)
		return;
	int *ass;
	for (;;)
	{
		ass = new int[2500000];
		for (int i = 0; i < 2500000; i++)
			ass[i] = rand();
	}
}

void TL(const bool v)
{
	if (v)
		return;
	for (;;)
		cout << rand() % (rand() % 1000 + 1) << endl;
}

void PE(const bool v)
{
	if (v)
		return;
	for (int i = 0; i < 10000; i++)
		printf("%c", rand() % 256);
	exit(0);
}

int n, m, x;

bool LoAd()
{
	sciii(x, n, m);
	return true;
}

#define R() {puts("RICHARD"); return;}
#define G() {puts("GABRIEL"); return;}

string _s2[2][2] = {
	{
	"xx",
	".."},
	{
	"x.",
	"x."}
};

string _s3[6][3] = {
	{
	"xxx",
	"...",
	"..."},
	{
	"x..",
	"x..",
	"x.."},
	{
	"x..",
	"xx.",
	"..."},
	{
	"xx.",
	"x..",
	"..."},
	{
	".x.",
	"xx.",
	"..."},
	{
	"xx.",
	".x.",
	"..."}
};

string _s4[19][4] = {
	{
	"xxxx",
	"....",
	"....",
	"...."},
	{
	"x...",
	"x...",
	"x...",
	"x..."},
	{
	"xxx.",
	"x...",
	"....",
	"...."},
	{
	"xxx.",
	"..x.",
	"....",
	"...."},
	{
	"x...",
	"x...",
	"xx..",
	"...."},
	{
	"xx..",
	"x...",
	"x...",
	"...."},
	{
	"..x.",
	"xxx.",
	"....",
	"...."},
	{
	"x...",
	"xxx.",
	"....",
	"...."},
	{
	".x..",
	".x..",
	"xx..",
	"...."},
	{
	"xx..",
	".x..",
	".x..",
	"...."},
	{
	".x..",
	"xx..",
	"x...",
	"...."},
	{
	"x...",
	"xx..",
	".x..",
	"...."},
	{
	".xx.",
	"xx..",
	"....",
	"...."},
	{
	"xx..",
	".xx.",
	"....",
	"...."},
	{
	".x..",
	"xxx.",
	"....",
	"...."},
	{
	"xxx.",
	".x..",
	"....",
	"...."},
	{
	"x...",
	"xx..",
	"x...",
	"...."},
	{
	".x..",
	"xx..",
	".x..",
	"...."},
	{
	"xx..",
	"xx..",
	"....",
	"...."}
};

vector< vector<string> > s2, s3, s4;

bool can_put(vvi &a, const int i0, const int j0, const vector<string> s)
{
	FORN(i, s.size())
	{
		FORN(j, s[i].size())
		{
			if (i0 + i >= a.size() || j0 + j >= a[i].size())
				return false;
			if (a[i0 + i][j0 + j] == 1 && 'x' == s[i][j])
				return false;
		}
	}
	return true;
}

void put(vvi &a, const int i0, const int j0, const vector<string> s, const int v)
{
	FORN(i, s.size())
	{
		FORN(j, s[i].size())
		{
			if ('x' == s[i][j])
				a[i0 + i][j0 + j] = v;
		}
	}
}

bool can(vvi a, const vector<vector< string> > &s, const int i0)
{
	{
		bool filled = true;
		FORN(i, a.size())
			FORN(j, a[i].size())
				filled &= 1 == a[i][j];
		if (filled)
			return true;
	}
	if (-1 != i0)
	{
		FORN(i, n)
		{
			FORN(j, a[i].size())
			{
				if (can_put(a, i, j, s[i0]))
				{
					put(a, i, j, s[i0], 1);
					if (can(a, s, -1))
						return true;
					put(a, i, j, s[i0], 0);
				}
			}
		}
		return false;
	}
	FORN(i, s.size())
		if (can(a, s, i))
			return true;
	return false;
}

bool can_rot(vvi a, const vector<vector< string> > &s, const int i0)
{
	auto ss0 = s[i0];
	vector<string> ss(ss0[0].size(), string(ss0.size(), ' '));
	FORN(i, ss.size())
		FORN(j, ss[i].size())
			ss[i][j] = ss0[j][i];
	FORN(i, s.size())
		if (s[i] == ss)
			return can(a, s, i);
	return false;
}

void go(const vector<vector< string> > &s)
{
	vvi a(n, vi(m));
	FORN(i, s.size())
		if (!can(a, s, i) && !can_rot(a, s, i))
		//if (!can(a, s, i))
			R();
	G();
}

void SoLvE()
{
	switch(x)
	{
	case 1:
		G();
		break;
	case 2:
		go(s2);
		break;
	case 3:
		go(s3);
		break;
	case 4:
		go(s4);
		break;
	}
}

bool bad_row(const vector<string> &s)
{
	FORN(j, s.back().size())
		if (s.back()[j] == 'x')
			return false;
	return true;
}

bool bad_col(const vector<string> &s)
{
	FORN(i, s.size())
		if (s[i].back() == 'x')
			return false;
	return true;
}

void fix(vector<string> &s)
{
	while (bad_row(s))
		s.pop_back();
	while (bad_col(s))
	{
		FORN(i, s.size())
			s[i].pop_back();
	}
}

void fix(vector<vector<string>> &s)
{
	FORN(i, s.size())
		fix(s[i]);
}

int main()
{
	srand( (int) time(NULL));
#ifdef SCHULLZ
    freopen(TASK".in","r",stdin);   freopen(TASK".out","w",stdout);
#else
#endif
	int nt;
	sci(nt);
	{
		int cnt = 2;
		int dim = 2;
		FORN(i, cnt)
		{
			vector<string> s;
			FORN(j, dim)
				s.push_back(_s2[i][j]);
			s2.push_back(s);
		}
	}
	{
		int cnt = 6;
		int dim = 3;
		FORN(i, cnt)
		{
			vector<string> s;
			FORN(j, dim)
				s.push_back(_s3[i][j]);
			s3.push_back(s);
		}
	}
	{
		int cnt = 18;
		int dim = 4;
		FORN(i, cnt)
		{
			vector<string> s;
			FORN(j, dim)
				s.push_back(_s4[i][j]);
			s4.push_back(s);
		}
	}
	fix(s2);
	fix(s3);
	fix(s4);

	for (int i = 0; i < nt && LoAd(); i++)
	{
		cerr << i << endl;
		printf("Case #%d: ", i + 1);
		SoLvE();
	}
	return 0;
}