#include <bits/stdc++.h>
using namespace std;

#define rREP(i,n) for(int i = (n)-1; i >= 0; i--)
#define REP(i,n) for(int i = 0; i < (n); i++)
#define rFOR(i,a,b) for(int i = (b); i > (a); i--)
#define FOR(i,a,b) for(int i = (a); i < (b); i++)

typedef long long lint;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vii> vvii;
typedef vector<vi> vvi;

int v[1100];

int rate(int a, int b){
	if(b > a)
		return 0;
	int r = (a-b);
	return r;
}

int main(){
	int t;
	cin >> t;
	REP(caso, t){
		int ans1 = 0;
		int ans2 = 0;
		int rat = 0;
		int n, m;
		cin >> n;
		cin >> v[0];
		REP(i, n-1){
			cin >> v[i+1];
			ans1 += max(0, v[i]-v[i+1]);
			rat = max(rat, rate(v[i], v[i+1]));
		}
		REP(i, n-1)
			ans2 += min(v[i], rat);

		cout << "Case #" << caso+1 << ": " << ans1 << " " << ans2 << endl;
	}
	return 0;
}