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

const int maxN = 1000 * 1000 + 5;

LL a[maxN];
LL sum[maxN];
int n, P, Q, R, S;
LL calc(int i, int j)
{
	if (i <= 0 || j < i || j > n) return 0;
	return sum[n] - max(max(sum[n]-sum[j], sum[j]-sum[i-1]), sum[i-1]);
}


int main()
{
	ios_base::sync_with_stdio(false);
	int T; cin >> T;
	for (int t = 0; t < T; t++)
	{
		cin >> n >> P >> Q >> R >> S;
		for (int i = 1; i <= n; i++)
		{
			a[i] = ((LL)(i-1)*P+Q)%R + S;
			sum[i] = sum[i-1] + a[i];
		}
//		for (int i = 1; i<= n; i++) cerr << a[i] << " ";

//		cerr << endl;
		int j = 1;
		LL ans = 0;
		for (int i = 1; i <= n; i++)
		{
			ans = max(ans, calc(i, j));
			ans = max(ans, calc(i, j-1));
			ans = max(ans, calc(i, j+1));
			while (j <= n && sum[j]-sum[i-1] <= sum[n]-sum[j])
			{
				j++;
				ans = max(ans, calc(i, j));
				ans = max(ans, calc(i, j-1));
				ans = max(ans, calc(i, j+1));
			}
			ans = max(ans, calc(i, j));
			ans = max(ans, calc(i, j-1));
			ans = max(ans, calc(i, j+1));
//			cerr << i << " " << j << endl;
		}
//		cerr << ans << " " << sum[n] << endl;
		cout << "Case #" << t+1 << ": ";
		cout << fixed << setprecision(10) << (long double)ans / sum[n] << endl;
//		if (t == 1) break;
	}

	return 0;
}

