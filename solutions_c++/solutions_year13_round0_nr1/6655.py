#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES
#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <ctype.h>
#include <complex>
#include <cassert>
#include <ctime>
using namespace std;
#define fill(x,v) memset(x,v,sizeof x)
#define MP make_pair
#define x first
#define y second
#define sz(s) int((s).size())
#define pb push_back
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef long long ll;
typedef unsigned long long ull;
template<class T> T sqr(T x) {return x * x;}
template<class T> T abs(T x) {return (x < 0) ? -x : x;}
const double EPS = 1e-18;
const int INF = 1010*1000*1000;

int main () {
#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
#endif
	int t;
	cin >> t;
	for (int cs = 1; cs <= t; cs++)
	{
		scanf("\n");
		vector<string> m(4);
		for (int i = 0; i < 4; i++)
		{
			cin >> m[i];
		}
		
		int xw = 0, ow = 0;
		bool draw = true;
		
		for (int i = 0; i < 4; i++)
		{
			int x = 0, o = 0;
			for (int j = 0; j < 4; j++)
			{
				if (m[i][j] == 'X')
				{
					x++;
				}
				else if (m[i][j] == 'O')
				{
					o++;
				}
				else if (m[i][j] == 'T')
				{
					o++, x++;
				}
				else
				{
					draw = false;
				}
			}
			if (x == 4) xw++;
			if (o == 4) ow++;
		}
		
		for (int j = 0; j < 4; j++)
		{
			int x = 0, o = 0;
			for (int i = 0; i < 4; i++)
			{
				if (m[i][j] == 'X')
				{
					x++;
				}
				else if (m[i][j] == 'O')
				{
					o++;
				}
				else if (m[i][j] == 'T')
				{
					o++, x++;
				}
				else
				{
					draw = false;
				}
			}
			if (x == 4) xw++;
			if (o == 4) ow++;
		}
		
		int tx = 0, to = 0;
		for (int i = 0, j = 0; i < 4; i++, j++)
		{
			if (m[i][j] == 'X')
			{
				tx++;
			}
			else if (m[i][j] == 'O')
			{
				to++;
			}
			else if (m[i][j] == 'T')
			{
				to++, tx++;
			}
			else
			{
				draw = false;
			}
		}
		if (tx == 4) xw++;
		if (to == 4) ow++;
		tx = 0;
		to = 0;
		for (int i = 0, j = 3; i < 4; i++, j--)
		{
			if (m[i][j] == 'X')
			{
				tx++;
			}
			else if (m[i][j] == 'O')
			{
				to++;
			}
			else if (m[i][j] == 'T')
			{
				to++, tx++;
			}
			else
			{
				draw = false;
			}
		}
		if (tx == 4) xw++;
		if (to == 4) ow++;
		
		if (xw > 0)
		{
			printf("Case #%d: X won\n", cs);
		}
		else if (ow > 0)
		{
			printf("Case #%d: O won\n", cs);
		}
		else if (draw)
		{
			printf("Case #%d: Draw\n", cs);
		}
		else
		{
			printf("Case #%d: Game has not completed\n", cs);
		}
	}
	
	
	return 0;
}

