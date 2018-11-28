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

double a[maxN], b[maxN];

int main()
{
	ios_base::sync_with_stdio(false);
	int T; cin >> T;
	for (int tt = 0; tt < T; tt++)
	{
		int n; cin >> n;
		rep(i, n) cin >> a[i];
		rep(i, n) cin >> b[i];
		sort(a, a+n); sort(b, b+n);
		/*
		if (tt != 3) continue;
		cerr << endl;
		rep(i, n) cout << a[i] << " ";
		cout << endl;
		rep(i, n) cout << b[i] << " ";
		cout << endl;
		*/
		int ans1 = 0, ans2 = 0;
		int l = 0, r = n-1;
		for (int i = n-1; i >= 0; i--)
		{
			if (a[i] > b[r])
			{
				l++;
				ans1++;
			}
			else
				r--;
		}
		l = 0, r = n-1;
		for (int i = 0; i < n; i++)
		{
			if (a[i] > b[l])
			{
				l++;
				ans2++;
			}
			else
				r--;
		}
		cout << "Case #" << tt+1 << ": ";
		cout << ans2 << " " << ans1 << endl;
	}

	return 0;
}

