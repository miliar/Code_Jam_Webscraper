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
#define MAX 2001
#define sz(v) (int)v.size()
#define all(c) (c).begin(),(c).end()
#define rall(c) (c).rbegin(),(c).rend()
#define iter(it,s) for(it=s.begin();it!=s.end();it++)
#define show(x) cerr<<#x<<" = "<<x<<endl;
#define mem(s,v) memset(s,v,sizeof(s))

typedef long long ll;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<string> vs;
typedef pair<int, int> pi;
typedef vector<pi> vpi;

int dx[] = { 0, 0, 1, -1 };
int dy[] = { 1, -1, 0, 0 };

int main() {
#ifndef ONLINE_JUDGE
	freopen("A-small-attempt0.in", "rt", stdin);
		freopen("o.txt", "wt", stdout);
#endif
	int t, cs = 1, n, cnt = 0;
	cin >> t;
	string s, vow = "aeiou", tmp = "";
	while (t--) {
		cnt = 0;
		cin >> s >> n;
		int si = sz(s);
		FOR(i , 0 , si) {
			tmp = "";
			FOR(j ,i , si) {
				tmp += s[j];
				if (sz(tmp) >= n) {
					int con = 0;
					FOR(k , 0 , sz(tmp)) {
						bool gd = true;
						FOR(l , 0 , 5)
							if (tmp[k] == vow[l])
								con = 0 , gd = false;
						if (gd)
							con++;
						if (con >= n) {
							cnt++;
							break;
						}
					}
				}
			}
		}
		printf("Case #%d: %d\n", cs++, cnt);
	}
	return 0;
}
