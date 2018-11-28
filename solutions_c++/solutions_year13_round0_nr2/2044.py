#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <fstream>
#include <list>
#include <set>
#include <climits>
#include <map>
#include <stack>
#include <queue>
#include <complex>
#include <cmath>
#include <sstream>
#include <deque>
#include <utility>
#include <bitset>
#include <ext/hash_set>
#include <ext/hash_map>

using namespace std;
using namespace __gnu_cxx;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REV(i,b,a) for(int i=(a);i>=(b);i--)
#define mp make_pair
#define pb push_back
#define oo (1<<30)
#define M 1001
#define sz(v) (int)v.size()
#define all(c) (c).begin(),(c).end()
#define rall(c) (c).rbegin(),(c).rend()
#define iter(it,s) for(it=s.begin();it!=s.end();it++)
#define show(x) cerr<<#x<<" = "<<x<<endl;
#define mem(s,v) memset(s,v,sizeof(s))
#define ppc(x) __builtin_popcount((x))

typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<double> vd;
typedef vector<string> vs;
typedef pair<int, int> pi;
typedef vector<pi> vpi;

int dx[] = { 0, 0, 1, -1 };
int dy[] = { 1, -1, 0, 0 };

int v[101][101];

int main() {
#ifndef ONLINE_JUDGE
	freopen("test.in", "rt", stdin);
		freopen("o.txt", "wt", stdout);
#endif
	int n, m, t;
	scanf("%d", &t);
	FOR (cs, 1, t + 1) {
		scanf("%d%d", &n, &m);
		FOR (i ,0 , n)
			FOR (j ,0 , m)
				scanf ("%d", &v[i][j]);
		FOR (i , 0 , n) {
			FOR (j , 0 , m) {
				int x = v[i][j];
				bool o1 = true, o2 = true;
				FOR (k , 0 , m)
					if (v[i][k] > x)
						o1 = false;
				FOR (k , 0 , n)
					if (v[k][j] > x)
						o2 = false;
				if (!o1 && !o2)
					goto no;
			}
		}
		printf ("Case #%d: YES\n", cs);
		goto yes;
		no:
		printf ("Case #%d: NO\n", cs);
		yes:;
	}
	return 0;
}
