#include <bits/stdc++.h>
using namespace std;

#define EACH(i,c) for(__typeof((c).begin()) i = (c).begin();i!=(c).end();i++)
#define FOR(i,a,b)  for(int i=(a);i<(b);i++)
#define dbg(e)  cout<<(#e)<<" : "<<e<<endl
#define set(v,i) memset(v,i,sizeof(v))
#define all(x) x.begin(),x.end()
#define sz(x) int((x).size())
#define REP(i,n) FOR(i,0,n)
#define pb  push_back
#define mp make_pair
#define INF (1 << 29)

int cache[105][105][2][2];
char a[105];

// f1 - flip each pancake - to + and + to -
// f2 - Swap the order of elements
int solve(int left, int right, int f1, int f2) {
	if(left > right) return 0;
	
	int &r = cache[left][right][f1][f2];
	if(r != -1) return r;
	
	r = INF;
	// 1. if last is + skip it
	if(f2 == 0) {
		// right is last
		if(f1 == 0 && a[right] == '+') r = min(r, solve(left, right - 1, f1, f2));
		if(f1 == 1 && a[right] == '-') r = min(r, solve(left, right - 1, f1, f2));
		if(f1 == 0 && a[left] == '+')  {
			int x = left; while(x <= right && a[x] == '+') x++;
			r = min(r, solve(x, right, !f1, !f2) + 2);
		}
		if(f1 == 1 && a[left] == '-') {
			int x = left; while(x <= right && a[x] == '-') x++;
			r = min(r, solve(x, right, !f1, !f2) + 2);
		}
	} else {
		// left is last
		if(f1 == 0 && a[left] == '+') r = min(r, solve(left + 1, right, f1, f2));
		if(f1 == 1 && a[left] == '-') r = min(r, solve(left + 1, right, f1, f2));
		//if(f1 == 0 && a[right] == '+') r = min(r, solve(left, right - 1, !f1, !f2) + 2);
		//if(f1 == 1 && a[right] == '-') r = min(r, solve(left, right - 1, !f1, !f2) + 2);
		if(f1 == 0 && a[right] == '+') {
			int x = right; while(left <= x && a[x] =='+') x--;
			r = min(r, solve(left, x, !f1, !f2) + 2);
		}
		if(f1 == 1 && a[right] == '-') {
			int x = right; while(left <= x && a[x] =='-') x--;
			r = min(r, solve(left, x, !f1, !f2) + 2);
		}
	}
	// 2. else flip and switch
	r = min(r, solve(left, right, !f1, !f2) + 1);
	
	return r;
}

int main() {
	int t;
	cin >> t;
	REP(tt, t) {
		cin >> a;
		set(cache, -1);
		cout << "Case #" << tt + 1 << ": " << solve(0, strlen(a)-1, 0, 0) << endl;
	}
}
