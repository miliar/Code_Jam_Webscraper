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

const ld PI = acos(-1);
const ld EPS = 1e-10;
double __t;

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
	int T;
	cin >> T;
	int x, r, c;
	for(int test = 1; test <= T; ++test)
	{
		string ans;
		cin >>x >> r >> c;
		if (x == 1) //ok
			ans = "GABRIEL";
		if (x == 2) //ok
		{
			if ((r*c)%2 == 1) //ok
				ans = "RICHARD";
			else
				ans = "GABRIEL";
		} 
		if (x == 3)
		{
			if(r == 1 || c == 1) //ok
				ans = "RICHARD";
			else
			{
				if (r == 2 && c == 2) //ok
					ans = "RICHARD";
				if (r == 2 && c == 3) //ok
					ans = "GABRIEL";
				if (r == 2 && c == 4)  //ok
					ans = "RICHARD";
				if (r == 3 && c == 2) //ok
					ans = "GABRIEL";
				if (r == 3 && c == 3) //ok
					ans = "GABRIEL";
				if (r == 3 && c == 4) //ok
					ans = "GABRIEL";
				if (r == 4 && c == 2) //ok
					ans = "RICHARD";
				if (r == 4 && c == 3) //ok
					ans = "GABRIEL";
				if (r == 4 && c == 4) //ok
					ans = "RICHARD";
			}	
		}
		if (x == 4)
		{
			if (r < 4 && c < 4) // ok
				ans = "RICHARD";
			else
			{
				if (r == 4 && c == 1) //ok
					ans = "RICHARD";
				if (r == 4 && c == 2) //ok
					ans = "RICHARD";
				if (r == 4 && c == 3) //ok
					ans = "GABRIEL";
				if (r == 4 && c == 4) //ok
					ans = "GABRIEL";
				if (r == 3 && c == 4) //ok
					ans = "GABRIEL";
				if (r == 2 && c == 4) //ok
					ans = "RICHARD";
				if (r == 1 && c == 4) //ok
					ans = "RICHARD";
			}
		}
		if (ans[0] == 'G')
			ans = "GABRIEL";
		if (ans[0] == 'R')
			ans = "RICHARD";
		cout << "Case #" << test << ": " << ans << '\n';
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