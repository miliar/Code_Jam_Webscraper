/*
ID: ahmedfarag111
LANG: C++
TASK: codejama
*/

#include <iostream>
#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define SZ(v) (int)v.size()

#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair

typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long long ll;

const int oo = (int) 1e9;
const double PI = 3.141592653589793;
const double eps = 1e-9;

#define MX 101
int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};
int T, n, e, r, v[MX];

#define SMALL

int calc(int cur, int ind)
{
	if(ind >= n)
		return 0;
	int maxi = 0;
	for (int i = 0; i <= cur; ++i) {
		maxi = max(maxi, i*v[ind] + calc(min(cur - i + r, e), ind + 1));
	}
	return maxi;
}
int main() {
		freopen("B.in", "rt", stdin);
	#ifdef SMALL
		freopen("B-small-attempt0.in","rt",stdin);
		freopen("B-small.out","wt",stdout);
	#endif
	#ifdef LARGE
		freopen("B-large.in","rt",stdin);
		freopen("B-large.out","wt",stdout);
	#endif


	cin >> T;

	for (int t = 0; t < T; ++t) {
		cin >> e >> r >> n;
		for (int i = 0; i < n; ++i) {
			cin >> v[i];
		}

		printf("Case #%d: %d\n", t + 1, calc(e, 0));
	}

	return 0;
}
