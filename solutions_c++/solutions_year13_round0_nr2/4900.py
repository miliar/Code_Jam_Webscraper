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

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REV(i,b,a) for(int i=(a);i>=(b);i--)
#define mp make_pair
#define pb push_back
#define oo 1e9
#define MAX 101
#define sz(v) (int)v.size()
#define all(c) (c).begin(),(c).end()
#define rall(c) (c).rbegin(),(c).rend()
#define iter(it,s) for(it=s.begin();it!=s.end();it++)
#define show(x) cerr<<#x<<" = "<<x<<endl;
#define mem(s,v) memset(s,v,sizeof(s))

int a[MAX][MAX];

int main() {
#ifndef ONLINE_JUDGE
	freopen("B-large.in", "rt", stdin);
		freopen("o.txt", "wt", stdout);
#endif
	int t, cs = 1, n, m;
	cin >> t;
	while (t--) {
		cin >> n >> m;
		FOR(i , 0 , n)
			FOR(j , 0 , m)
				cin >> a[i][j];
		bool ok = true;
		FOR(i , 0 , n) {
			FOR(j , 0 , m) {
				bool b1 = true, b2 = true;
				FOR(k , 0 , m)
					if (a[i][k] > a[i][j])
						b1 = false;

				FOR(k , 0 , n)
					if (a[k][j] > a[i][j])
						b2 = false;
				if (!(b1 || b2))
					ok = false;
			}
		}
		if (ok)
			printf("Case #%d: YES\n", cs++);
		else
			printf("Case #%d: NO\n", cs++);
	}
	return 0;
}
