#include <iostream>
#include <iomanip>
#include <cstdio>
#include <stack>
#include <queue>
#include <vector>
#include <cmath>
#include <string>
#include <cstring>
#include <algorithm>
#include <climits>
#include <set>
#include <map>
using namespace std;

#define FORD(i,a,b) for(int i = (a); i >= (b); --i)
#define FOD(i,a,b) for(int i = (a);i > (b); --i)
#define FOR(i,a,b) for(int i = (a); i <= (b); ++i)
#define FO(i,a,b)  for(int i = (a);i < (b); ++i)
#define PI M_PI
#define pb push_back
#define mp make_pair
#define st first
#define nd second
#define FILEIN freopen("A-large.in", "r", stdin)
#define FILEOUT freopen("test.out", "w", stdout)
#define OUT(v) {FO(i,0,v.size()) cout << v[i] << " "; cout << endl;}
int debug = 0;
#define DEBUG() {cout << "YES " << debug++ << endl;}
typedef pair<int, int> II;
typedef long long LL;
typedef unsigned long long ULL;

int cnt[1010];
int sum[1010];
int n; string s;


int main() {
//	ios_base::sync_with_stdio(false);
	FILEIN;
	FILEOUT;
	int test; cin >> test;
	FOR(t,1,test) {
	
		cin >> n >> s;
		FOR(i,0,n) {
			cnt[i] = s[i] - '0';
			if(i > 0) sum[i] = sum[i-1] + cnt[i];
		}
	//	FOR(i,1,n) cout << i << " "; cout << endl;
	//	FOR(i,1,n) cout << sum[i] << " "; cout << endl;
		int ans = 0;
		FOR(i,1,n) {
			if(i > sum[i-1] + cnt[0]) {
				ans += i - (sum[i-1] + cnt[0]) ;
				cnt[0] += i - (sum[i-1] + cnt[0]);
			}
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}


