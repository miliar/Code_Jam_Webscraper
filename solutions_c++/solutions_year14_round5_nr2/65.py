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

int n, A, B;
int h[111], g[111];
int dp[111][1111];
int z[111][111];

map<pair<pt, int>, int> W;

int rec(int x, int hp, int sh) {
	if (x == n) return 0;
	pair<pt, int> e  = mp(mp(x, hp), sh);
	if (W.find(e) != W.end()) return W[e];

	int ret = 0;
	if (hp <= B) ret = rec(x + 1, h[x + 1], sh + 1); else ret = rec(x, hp - B, sh + 1);

	int a = (hp + A - 1) / A;
	if (sh >= a) ret = max(ret, rec(x + 1, h[x + 1], sh - a) + g[x]);
	return W[e] = ret;
}

int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		cin >> A >> B >> n;
		for (int i = 0; i < n; i++) cin >> h[i] >> g[i];
		W.clear();		
		int ans = rec(0, h[0], 1);
		cout << "Case #" << tt << ": ";
		cout << ans << endl;

	}
	return 0;
}