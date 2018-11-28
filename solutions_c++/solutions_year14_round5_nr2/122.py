#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <functional>
using namespace std;

typedef long long int64;
#define PB push_back
#define MP make_pair
#define debug(x) cout<<(#x)<<": "<<(x)<<endl
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,l,h) for(int i=(l);i<=(h);++i)
#define FORD(i,h,l) for(int i=(h);i>=(l);--i)
#define MOD 1000000007

int dp[2][1020];

int main() {
	int tN;
	cin >> tN;
	FOR(cN, 1, tN) {
		int hero, tower, n;
		cin >> hero >> tower >> n;
		memset(dp, -1, sizeof(dp));
		int o = 0;
		dp[o][1] = 0;
		REP(creep, n) {
			o = 1-o;
			memset(dp[o], -1, sizeof(dp[o]));
			int hp, gold;
			cin >> hp >> gold;
			int towerHit = (hp+tower-1) / tower;
			FOR(i, 0, 1000) {
				if (dp[1-o][i] >= 0) dp[o][i+towerHit] = max(dp[o][i+towerHit], dp[1-o][i]);
			}
			--towerHit;
			int hpLeft = hp - towerHit*tower;
			int heroHit = (hpLeft+hero-1) / hero;
			FOR(i, 0, 1000) if (dp[1-o][i] >= 0 && i+towerHit-heroHit >= 0) {
				dp[o][i+towerHit-heroHit] = max(dp[o][i+towerHit-heroHit], dp[1-o][i] + gold);
			}
			FORD(i, 1000, 0) dp[o][i] = max(dp[o][i], dp[o][i+1]);
		}
		int ans = dp[o][0];
		printf("Case #%d: %d\n", cN, ans);
	}
}
