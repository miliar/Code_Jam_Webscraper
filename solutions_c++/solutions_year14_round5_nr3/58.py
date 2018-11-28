#include<stdio.h>
#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<memory.h>
#include<map>
#include<set>
#include<queue>
#include<list>
#include<sstream>
#define mp make_pair
#define pb push_back      
#define F first
#define S second
#define SS stringstream
#define sqr(x) ((x)*(x))
#define m0(x) memset(x,0,sizeof(x))
#define m1(x) memset(x,63,sizeof(x))
#define CC(x) cout << (x) << endl
#define pw(x) (1ll<<(x))
#define M 1000000007
#define N 111111
using namespace std;
typedef pair<int,int> pt;

int n;
char t[3222];
int a[3222], u[3333];
int dp[20][67000];

int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		cin >> n;
		for (int i = 0; i < n; i++) cin >> t[i] >> a[i];
		for (int i = 0; i <= 3000; i++) u[i] = -1;
		for (int i = 0; i < n; i++) u[a[i]] = 1;
		int e = 0;
		for (int i = 0; i <= 3000; i++) if (u[i] != -1) {
			u[i] = e;
			e++;
		}
		for (int i = 0; i <= 3000; i++) if (e < n && u[i] == -1) {
			u[i] = e;
			e++;
		}	
		for (int i = 0; i <= n; i++)
		for (int o = 0; o < pw(e); o++) dp[i][o] = 0;
		for (int o = 0; o < pw(e); o++) dp[0][o] = 1;
		for (int i = 0; i < n; i++) for (int o = 0; o < pw(e); o++) if (dp[i][o]) {
			for (int j = 0; j < e; j++) {
				if (a[i] != 0 && j != u[a[i]]) continue;
				if (t[i] == 'L') {
					if (o & pw(j)) dp[i + 1][o - pw(j)] = 1;
				} else {
					if ((o & pw(j)) == 0) dp[i + 1][o + pw(j)] = 1;
				}
			}
		}
		int ans= 1e9;
		for (int o = 0; o < pw(e); o++) if (dp[n][o]){
			int s = 0;
			int x = o;
			while (x > 0) {
				s++;
				x &= x - 1;
			}
			ans = min(ans, s);	
		}
		cout << "Case #" << tt << ": ";
		if (ans == 1e9) puts("CRIME TIME"); else cout << ans << endl;

	}
	return 0;
}