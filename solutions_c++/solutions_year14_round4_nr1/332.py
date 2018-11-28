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

const int maxN = 10 * 1000 + 5;

int a[maxN];

int main()
{
	ios_base::sync_with_stdio(false);
	int T; cin >> T;
	for (int t = 0; t < T; t++)
	{
		int n, m;
		cin >> n >> m;
		for (int i = 0; i < n; i++)
			cin >> a[i];
		sort(a, a+n);
		int cnt = 0;
		int j = 0;
		for (int i = n-1; i >= j; i--)
		{
			if (a[i]+a[j] <= m)
				cnt++, j++;
			else
				cnt++;
		}
		cout << "Case #" << t+1 << ": ";
		cout << cnt << endl;
	}
	return 0;
}

