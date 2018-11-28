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

unsigned long long r, t;

bool chk(unsigned long long x) {
	unsigned long long rr;
	rr = (2 * x + 2* r + 1);
	return rr <= t/(x + 1) ;
}

ll bs() {
	ll lo = 1, hi = t , res = 0;
	while (lo <= hi) {
		ll mid = lo + (hi - lo) / 2;
		if(chk(mid)) {
			res = mid;
			lo = mid+1;
		}else
			hi = mid - 1;
	}
	return res+1;
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("A-large.in", "rt", stdin);
	freopen("o.txt", "wt", stdout);
#endif
	int tt;
	cin >> tt;
	int cs = 1;
	while (tt--) {
		cin >> r >> t;
		cout<<"Case #"<<cs++<<": "<<bs()<<endl;
	}
	return 0;
}
