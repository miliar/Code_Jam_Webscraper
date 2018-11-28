#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:128777216")

#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <sstream>

#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <bitset>
#include <queue>
#include <deque>
#include <stack>

#include <math.h>
#include <cmath>
#include <string>
#include <cstring>
#include <string.h>

#include <memory.h>
#include <cassert>
#include <time.h>
#include<unordered_map>

using namespace std;

#define forn(i,n) for (int i = 0; i < (int)(n); i++)
#define fornd(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forab(i,a,b) for (int i = (int)(a); i <= (int)(b); i++)
#define forabd(i, b, a) for (int i = (int)(b); i >= (int)(a); i--)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)

#define _(a, val) memset (a, val, sizeof (a))
#define sz(a) (int)((a).size())
#define pb push_back
#define mp make_pair
#define all(v) (v).begin(), (v).end()

typedef long long lint;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int, int> pii;
typedef vector<int> vii;

const lint LINF = 1000000000000000000LL;
const int INF = 1000000000;
const long double eps = 1e-9;
const long double PI = 3.1415926535897932384626433832795l;

#ifdef MY_DEBUG
#define dbgx( x ) { cerr << #x << " = " << x << endl; }
#define dbg( ... ) { fprintf(stderr, __VA_ARGS__); fflush(stderr); }
#else
#define dbgx( x ) {  } 
#define dbg( ... ) {  } 
#endif

void prepare(string s)
{
#ifdef MY_DEBUG
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);
#else
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);
#endif
}

const int LENMAX = 100100;
const int NMAX = 205;
int Case = 1;

int n;
char sentence[LENMAX];
vector<string> words[NMAX];

int lang[NMAX];

void read()
{
	scanf("%d\n", &n);
	forn(i, n)
	{
		words[i].clear();
		gets( sentence );
		stringstream ss(sentence);
		string tmp;
		while(ss >> tmp)
			words[i].pb( tmp );
	}
}

void solve()
{
	vector<string> all_w;
	unordered_map<string, int> mem;
	forn(i, n)
	{
		forn(j, sz(words[i]))
		{
			mem[words[i][j]] |= 1 << i;
			all_w.pb( words[i][j] );
		}
	}

	vector<int> wds;
	for(auto it = mem.begin(); it != mem.end(); ++it)
	{
		wds.pb(it->second);
	}

	//sort(all(all_w));
	//all_w.erase(unique(all(all_w)), all_w.end());


	cerr << "Case = " << Case << endl;
	int answer = INF;
	lang[0] = 0;
	lang[1] = 1;
	forn(msk, 1 << (n - 2))
	{
		if ((msk & (msk - 1)) == 0)
			cerr << msk << endl;
		int mask = 2 | (msk << 2);
		int res = 0;
		forn(i, sz(wds))
		{
			int t = wds[i];
			int tt = t & mask;
			if (tt != 0 && tt != t)
				res ++;
		}
		answer = min(answer, res);
	}

	printf("Case #%d: %d\n", Case++, answer);
}

int main()
{
	prepare("");

	int t;
	scanf("%d", &t);
	forn(i, t)
	{
		read();
		solve();
	}

	return 0;
}
