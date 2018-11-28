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

const int maxN = 10 + 5;
const int maxS = 30 + 5;
const int mod = 1000 * 1000 * 1000 + 7;

int g[maxN][maxS];
int n, m;

int b[maxN];

string s[maxN];
int solve()
{
	int res = 0;
	for (int i = 0; i < m; i++)
	{
		set <string> uq;
		for (int j = 0; j < n; j++)
			if (b[j] == i)
				for (int k = 0; k <= Size(s[j]); k++)
					uq.insert(s[j].substr(0, k));
		res += Size(uq);
	}
	return res;
}


int ans = 0, cnt = 0;

void bt(int ind)
{
	if (ind == n)
	{
		int mark[10] = {0};
		for (int i = 0; i < n; i++)
			mark[b[i]] = 1;
		for (int i = 0; i < m; i++)
			if (!mark[i])
				return;
		int res = solve();
		if (ans < res)
			ans = res, cnt = 0;
		if (ans == res)
			cnt++, cnt %= mod;
		return;
	}
	for (int i = 0; i < m; i++)
	{
		b[ind] = i;
		bt(ind+1);
	}
}


int main()
{
	ios_base::sync_with_stdio(false);
	// ans = 0
	int T; cin >> T;
	for (int t = 0; t < T; t++)
	{
		cerr << t << endl;
		cin >> n >> m;
		for (int i = 0; i < n; i++)
			cin >> s[i];
		ans = cnt = 0;
		bt(0);
		cout << "Case #" << t+1 << ": ";
		cout << ans << " " << cnt << endl;
	}
	return 0;
}

