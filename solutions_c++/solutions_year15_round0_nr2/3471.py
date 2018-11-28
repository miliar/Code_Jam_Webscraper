#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <list>
#include <ctime>
#include <sstream>
#include <queue>
#include <stack>
#include <bitset>
using namespace std;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef long long LL;
#define FOR(x, b, e) for(int x=(b); x<=(e); ++x)
#define FORD(x, b, e) for(int x=((int)(b))-1; x>=(e); --x)
#define REP(x, n) for(int x=0; x<(n); ++x)
#define VAR(v,n) typeof(n) v=(n)
#define ALL(c) c.begin(),c.end()
#define SIZE(x) ((int)((x).size()))
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second
#define mp(x,y) make_pair(x,y)
#define DEBUG 1
#define debug(x) {if (DEBUG)cerr <<#x <<" = " <<x <<endl; }
#define debugv(x) {if (DEBUG) {cerr <<#x <<" = "; FOREACH(it, (x)) cerr <<*it <<", "; cout <<endl; }}
typedef short int sint;

void solve() {
	int n;
	cin >> n;
	VI t(n, 0);
	int res = 0;
	REP(i, n) {
		cin >> t[i];
		if (t[i] > res) {
			res = t[i];
		}
	}
	FORD(i, res, 1) {
		int tres = i;
		REP(j, n) {
			tres += max(t[j] - 1, 0)/i;
		}
		if (tres < res) {
			res = tres;
		}
	}
	cout << res << endl;
}

int main(){
	int t;
	cin >> t;
	REP(i, t) {
		cout << "Case #" << i+1 << ": ";
		solve();
	}
}