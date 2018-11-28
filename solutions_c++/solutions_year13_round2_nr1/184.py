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
#define ten(n) ((int)1e##n)

int get_count(ll a,vector<ll>& v){
	int cnt = 0;

	FOR(i,sz(v)){
		if(a > v[i]) a += v[i];
		else {
			while(a <= v[i]) a += a-1,cnt++;
			a += v[i];
		}
	}

	return cnt;
}

ll solve(){
	ll a; int n; cin>>a>>n;
	vector<ll> v(n);
	FOR(i,n){
		cin>>v[i];
	}
	sort(v.begin(),v.end());

	if(a == 1){ //‰ò‚ð‘å‚«‚­o—ˆ‚È‚¢
		return n;
	}

	int ans = 1000;

	int e_size = 0;
	while(!v.empty()){
		int cnt = get_count(a,v);
		ans = min(cnt + e_size,ans);
		v.erase(v.end() - 1);
		e_size++;
	}

	ans = min(ans,n);

	return ans;
}

int main(){
	int t; cin>>t;
	for(int i = 1; i <= t; i++){
		auto ans = solve();
		printf("Case #%d: %lld\n",i,ans);
	}
	return 0;
}
