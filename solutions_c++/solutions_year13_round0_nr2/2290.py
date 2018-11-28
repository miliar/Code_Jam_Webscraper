#define _CRT_SECURE_NO_WARNINGS
#include <numeric>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <bitset>
#include <vector>
#include <map>
#include <queue>
#include <deque>
#include <set>
#include <math.h>
#include <assert.h>
#include <time.h>
#include <stdio.h>
#include <string.h>
#include <string>
#include <sstream>

#pragma comment(linker, "/STACK:256000000")
using namespace std;
typedef long long ll;
template<typename T> int size(T &a) {return (int)a.size();}
template<typename T> T sqr(T a)  { return a * a; }

#define fi first
#define se second
#define VAR(a,b) __typeof(b) a=(b)
#define FOR(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,a,b) for(int i=(a);i<(b); ++i)
#define REPD(i,a,b)for(int i=(b)-1;i>=a;--i)
#define _(a,b) memset((a), (b), sizeof(a))
#define all(a) a.begin(), a.end()
#define mp make_pair
#define pb push_back
#define ve vector


void solve(){
	int n, m;
	cin>>n>>m;
	ve<ve<int> > a(n,ve<int> (m));
	REP(i,0,n)REP(j,0,m)cin>>a[i][j];
	bool ok=true;
	int mx=-100;
	REP(i,0,n) mx=max(mx, *max_element(&a[i][0],&a[i][0]+m));

	REP(i,0,n) REP(j,0,m) {
		if (mx == a[i][j]) continue;
		bool ok1=true;
		bool ok2=true;
		REP(u,0,n)
			ok1 &= a[i][j] == a[u][j];
		REP(u,0,m) ok2 &= a[i][j] == a[i][u];
		if (!ok1 && !ok2){
			printf("NO");
			return;
		}
	}
	printf("YES");

}
int main() {
#ifdef air
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	//ios_base::sync_with_stdio(false);
	
	int test;
	cin >> test;
	REP(t, 0, test) {
		printf("Case #%d: ", t+1);
		solve();
		printf("\n");
	}
	

#ifdef air
	//printf("\n\n%lf\n", clock() * 1e-3);
#endif

	return 0;
}