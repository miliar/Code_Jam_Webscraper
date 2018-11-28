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

ll R,t;

ll C(ll count){
	double c_d = count;
	ll start = R * 2 + 1;
	if(start * c_d + 2 * c_d * (c_d + 1) > 10e18 * 2){
		return false;
	} 
	ll cover = start * count + 2 * count * (count - 1);
	return cover <= t;
}

ll solve(){
	cin>>R>>t;

	ll l = 1; 
	ll r = (ll)1e18;
	while(r - l != 1){
		ll md = (l + r) / 2;
		if(C(md)) l = md;
		else r = md;
	}
	return l;
}

int main(){
	int t; cin>>t;
	for(int i = 1; i <= t; i++){
		auto ret = solve();
		printf("Case #%d: %lld\n",i,ret);
	}
	return 0;
}
