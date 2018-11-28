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

const int maxN = 1000 + 5;
const int INF = 1000 * 1000 + 5;

PII a[maxN];
int b[maxN];

int d[maxN][maxN];

int pnt[maxN];

int main()
{
	ios_base::sync_with_stdio(false);
	int T; cin >> T;
	for (int t = 0; t < T; t++)
	{
		int n; cin >> n;
		for (int i = 1; i <= n; i++)
			cin >> a[i].f1, a[i].f2 = i;
		sort(a+1, a+n+1);
		for (int i = 1; i <= n; i++)
			b[a[i].f2] = i;
		for (int i = 1; i <= n; i++) pnt[b[i]] = i;
		for (int i = 1; i <= n; i++)
		{
			for (int j = 1; j < i; j++)
				if (b[j] < b[i])
					pnt[b[i]]--;
		}
					
		rep(i, n+1) rep(j, n+1) d[i][j] = INF;
		d[0][0] = 0;
//		for (int i = 1; i <= n; i++)
//			cerr << pnt[i] << endl;
		for (int i = 1; i <= n; i++)
		{
			int k = n-i+1;		
			int x = pnt[i];
//			cerr << i << " " << x-1 << " " << k << " " <<  k-x << endl;
			for (int j = 0; j < i; j++)
			{
				d[i][j+1] = min(d[i][j+1], d[i-1][j] + x-1);
				d[i][j] = min(d[i][j], d[i-1][j] + k-x);
			}
		}
		int ans = INF;
		for (int j = 0; j <= n; j++)
			ans = min(ans, d[n][j]);
		cout << "Case #" << t+1 << ": ";
		cout << ans << endl;
	}
	return 0;
}

