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

const int maxN = 100 * 1000 + 5;
const int N = 1000 * 10000;

int main()
{
	ios_base::sync_with_stdio(false);
	int T; cin >> T;

	for (int tt = 0; tt < T; tt++)
	{
		double c, f, x;
		cin >> c >> f >> x;
		double ans = x/2;
		double t = 0, p = 2;
		for (int i = 1; i <= N; i++)
		{
			t += c/p;	
			p += f;
			if (t+x/p > ans)
				break;
			ans = t+x/p;
		}
		cout << "Case #" << tt+1 << ": ";
		cout << fixed << setprecision(7) << ans << endl;
	}
	return 0;
}

