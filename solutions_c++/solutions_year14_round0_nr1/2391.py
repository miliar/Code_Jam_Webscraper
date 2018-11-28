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

int a[5][5];
int b[5][5];

int main()
{
	ios_base::sync_with_stdio(false);
	int T; cin >> T;
	for (int t = 0; t < T; t++)
	{
		int n = 4;
		int x, y;
		map <int, int> g;
		cin >> x; x--;
		rep(i, n) rep(j, n)
			cin >> a[i][j];
		rep(i, n) g[a[x][i]]++;
		cin >> y; y--;
		rep(i, n) rep(j, n)
			cin >> b[i][j];
		rep(i, n) g[b[y][i]]++;
		int ans = 0, cnt = 0;
		Foreach(it, g)
			if (it->f2 == 2)
				cnt++, ans = it->f1;
		cout << "Case #" << t+1 << ": ";
		if (cnt == 1)
			cout << ans << endl;
		else if (cnt >= 2)
			cout << "Bad magician!" << endl;
		else
			cout << "Volunteer cheated!" << endl; 
//		cerr << cnt << endl;
	}
	return 0;
}

