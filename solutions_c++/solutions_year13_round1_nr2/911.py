#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cfloat>
#include <ctime>
#include <cassert>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <numeric>
#include <list>
#include <iomanip>


using namespace std;
const int MODULO = 1000000007; // check!!!
const int INF = 100000000; //1e8

typedef long long ll;
typedef pair<int,int> Pii;
typedef pair<ll,ll> Pll;

#define FOR(i,n) for(int i = 0; i < (n); i++)
#define sz(c) ((int)(c).size())

int r,e,n;
int v[10000];

int dp[14][10];

ll solve(){
	cin>>e>>r>>n;
	FOR(i,n) cin>>v[i];
	memset(dp,0,sizeof(dp));

	for(int i = 0; i < n; i++){
		for(int le = 0; le <= e; le++){
			for(int use = 0; use <= le; use++){
				int ne = min(le - use + r,e);
				dp[i+1][ne] = max(dp[i+1][ne],dp[i][le] + use * v[i]);
			}
		}
	}

	int ans = *max_element(dp[n],dp[n] + 10);

	return ans;
}

int main(){
	int t; cin>>t;
	for(int i = 1; i <= t; i++){
		auto ret = solve();
		printf("Case #%d: %lld\n",i,ret);
	}
	return 0;
}
