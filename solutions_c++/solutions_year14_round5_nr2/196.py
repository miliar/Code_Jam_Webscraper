// written by Amirmohsen Ahanchi //
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <string>
#include <sstream>
#include <cmath>
#include <stdio.h>
#include <iomanip>
#include <queue>
#include <map>
#include <fstream>
#include <cstring>
#include <list>
#include <iterator>
#include <complex>
#include <cassert>

#define pb push_back
#define mp make_pair
#define f1 first
#define f2 second
#define X first
#define Y second
#define Size(n) ((int)(n).size())
#define Foreach(i, x) for (__typeof(x.begin()) i = x.begin(); i != x.end(); i++)
#define all(x) x.begin(),x.end()
#define rep(i, n) for (int i = 0; i < n; i++)
#define dbg(x) "#" << #x << ": " << x 
#define spc << " " <<

using namespace std;

//#define cin fin
//#define cout fout

typedef long long LL;
typedef pair <int, int> PII; 

const int maxN = 300 + 5;

//vector <int> h, g;
int n, p1, p2; // diana tower

/*
map <pair <int, vector <int> >, int> d; 

int bt(int t)
{
	bool alive = false;
	pair <int, vector <int> > st = mp(t, h);
	if (d.find(st) != d.end()) return d[st];
	rep(i, n) alive |= h[i] > 0;
	int& res = d[st];
	if (!alive)
		return res = 0;
	if (t == 0)
	{
		rep(i, n) if (h[i] > 0)
		{
			h[i] -= p1;
			int w = 0;
			if (h[i] <= 0) w += g[i];
			res = max(w+bt(t^1), res);
			h[i] += p1;
		}
		res = max(res, bt(t^1));
	}
	else
		rep(i, n) if (h[i] > 0)
		{
			h[i] -= p2;
			res = max(res, bt(t^1));
			h[i] += p2;
			break;
		}
	return res;
}
		
*/

const int maxS = 1000 + 5;
int d[maxN][maxN][maxS];
int h[maxN], g[maxN];


int main()
{
	ios_base::sync_with_stdio(false);
	int T; cin >> T;
	for (int t = 0; t < T; t++)
	{
		cin >> p1 >> p2 >> n;
		memset(h, 0, sizeof h);
		memset(g, 0, sizeof g);
		rep(i, n) cin >> h[i] >> g[i];
		memset(d, 0, sizeof d);
//		cerr << n << endl;
		cerr << t << endl;
		for (int i = n-1; i >= 0; i--) 
			for (int c = 1; c <= h[i]; c++)
				for (int j = 0; j < maxS-2; j++)
				{
					int k = (c/p1) + (bool)(c%p1);
					int& res = d[i][c][j];
					if (j >= k)
					{
						res = max(res, g[i] + d[i+1][h[i+1]][j-k]);
//						if (c2 > 0)	
//							res = max(res, g[i] + d[i+1][h[i+1]][j-k]);
//						else
//							res = max(res, g[i] + d[i+2][h[i+2]][j-k+1]);
					}
					int x = c-p2;
					if (x <= 0)
						res = max(res, d[i+1][h[i+1]][j+1]);
					else
						res = max(res, d[i][x][j+1]);
				}
//		cerr << d[0][][3] << endl;
//		cerr << d[0][h[0]][1] << endl;
//		d.clear();
//		int ans = bt(0);
		cout << "Case #" << t+1 << ": ";
		cout << d[0][h[0]][1] << endl;
		//cerr << "Case #" << t+1 << ": ";
//		cerr << ans << endl;
	}
	return 0;
}

