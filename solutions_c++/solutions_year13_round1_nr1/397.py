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
int T;
ll r, n;
bool valid(ll a)
{
//	cout << a << " - " << ((a*(2*r + 2 * (a - 1) + 1))) << endl;
	return(((2*r + 2 * (a - 1) + 1)) <= n / (long double)a);
}
#define LARGE
int main() {
		freopen("A.in", "rt", stdin);
	#ifdef SMALL
		freopen("A-small-attempt0.in","rt",stdin);
		freopen("A-small.out","wt",stdout);
	#endif
	#ifdef LARGE
		freopen("A-large.in","rt",stdin);
		freopen("A-large.out","wt",stdout);
	#endif


	cin >> T;

	for (int t = 0; t < T; ++t) {
		cin >> r >> n;
		ll st = 0, en = 2 * 1e18, mid;
		while(st < en)
		{
			mid = st + (en-st+1)/2;
			if(valid(mid))
				st = mid;
			else
				en = mid - 1;
		}
		printf("Case #%d: %lld\n", t + 1, st);
	}

	return 0;
}
