#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstdlib>
#include <iomanip>
#include <ctime>
#include <utility>

#define x first
#define y second
#define mp make_pair
#define pb push_back
#define sqr(x) (x)*(x)
#define _with_file
#define TASK ""
#define forn(i, n) for(int i = 0; i < (int)n; ++i)

void quit(); 

using namespace std;

typedef long long i64;
typedef unsigned long long u64;
#ifdef local
typedef double ld;
#else
typedef long double ld;
#endif
typedef pair <int, int> PII;
typedef pair <i64, i64> PII64;
typedef pair <ld, ld> PLL;
typedef pair <char, bool> Q;


const ld PI = acos(-1);
const ld EPS = 1e-10;
double __t;

char st[128][128];
bool nt[128][128];

Q multiply(const Q & a, const Q & b)
{
	Q res;
	res.x = st[a.x][b.x];
	res.y = nt[a.x][b.x];
	if (a.y != b.y)
		res.y = !res.y;
	return res;
}

Q inv(Q a)
{
	if (a.x == '1')
		return a;
	a.y = !a.y;
	return a;
}

string tos(const Q & a)
{
	string s;
	if (a.y)
		s = "-";
	s += a.x;
	return s; 
}

char q[4] = {'1', 'i', 'j', 'k'};
Q p[10100];

Q prod(int l, int r)
{
	if (l)
		return multiply(inv(p[l-1]), p[r]);
	return p[r];
}

int main()
{
	#ifdef local
		__t = clock();
		#ifndef _with_files
			freopen("z.in", "rt", stdin);
			freopen("z.out", "wt", stdout);
		#endif
	#endif
	#ifdef _with_files
		freopen(TASK".in", "rt", stdin);
		freopen(TASK".out", "wt", stdout);
	#endif
	st['1']['1'] = '1';
	st['1']['i'] = 'i';
	st['1']['j'] = 'j';
	st['1']['k'] = 'k';
	st['i']['1'] = 'i';
	st['i']['i'] = '1'; nt['i']['i'] = 1;
	st['i']['j'] = 'k';
	st['i']['k'] = 'j'; nt['i']['k'] = 1;
	st['j']['1'] = 'j';
	st['j']['i'] = 'k'; nt['j']['i'] = 1;
	st['j']['j'] = '1'; nt['j']['j'] = 1;
	st['j']['k'] = 'i';
	st['k']['1'] = 'k';
	st['k']['i'] = 'j';
	st['k']['j'] = 'i'; nt['k']['j'] = 1;
	st['k']['k'] = '1'; nt['k']['k'] = 1;	 
	
	//check table
	/*
	for(int i = 0; i < 4; ++i)
	{
		for(int j = 0; j < 4; ++j)
			cout << tos(multiply(mp(q[i], (bool)0), mp(q[j], (bool)0))) << ' ';
		cout << '\n';
	}
	*/
	//!!!it's ok
	int T;
	cin >> T;
	int l, x;
	string s;
	string ss;
	for(int test = 1; test <= T; ++test)
	{
		cin >> l >> x >> s;
		ss = "";
		for(int i = 0; i < x; ++i)
			ss += s;
		p[0] = mp(ss[0], (bool)0);
		for(int i = 1; i < l*x; ++i)
			p[i] = multiply(p[i-1], mp(ss[i], (bool)0));
		bool ok = 0;
		for(int p1 = 0; p1 < l*x && !ok; ++p1)
		{
			for(int p2 = p1 + 1; p2 < l*x && !ok; ++p2)
			{
				if (prod(0, p1) == mp('i', (bool)0) && prod(p1 + 1, p2) == mp('j', (bool)0) && prod(p2 + 1, l*x-1) == mp('k', (bool)0))
				{
					ok = 1;
				}
			}
		}
		if (ok)
			cout << "Case #" << test<<": YES\n";
		else
			cout << "Case #" <<test<<": NO\n";
	}
	quit();
}

void quit()
{
	#ifdef local
		cerr << "\nTOTAL TIME: "<< (clock() - __t)/1000.0 << " s\n";
	#endif
	exit(0);		
}