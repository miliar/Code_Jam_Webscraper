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

ll f(ll a){
	return 1 + a + 2 * a * (a+1);
}

double solve(){
	int n,x,y; cin>>n>>x>>y;
	if(x == 0 && y == 0) return 1.0;
	ll dist = abs(x) + abs(y);
	ll a = dist / 2;
	if(a > ten(5)) return 0.0;

	//ŠÖŒW‚È‚­Ÿè‚ÉÏ‚à‚éŒÂ”
	ll b = f(a-1);
	//‚±‚±‚Ü‚ÅÏ‚à‚Á‚½‚ç100%‚ÈŒÂ”
	ll c = f(a);

	if(n <= b) return 0;
	if(n >= c) return 1;

	if(x == 0){
		//“Áê
		return 0.0; //}ë‚è‚³‚ê‚Ä‚È‚¢ = out
	}
	//‚±‚ê‚©‚çl‚¦‚éŒÂ”‚É’¼‚·
	n -= b;
	vector<double> par(2*a + 1);
	par[0] = 1;
	FOR(i,n){
		vector<double> npar(2*a+1);
		FOR(j,2*a+1){
			int right = i - j;
			if(right < 0) continue;
			if(right == 2*a){
				npar[j+1] += par[j];
			} else if(j == 2*a){
				npar[j] += par[j];
			} else {
				npar[j] += par[j] * 0.5;
				npar[j+1] += par[j] * 0.5;
			}
		}
		par.swap(npar);
	}

	double ret = 0;
	for(int h = y+1; h < sz(par); h++) ret += par[h];

	return ret;
}

int main(){

	int t; cin>>t;
	for(int i = 1; i <= t; i++){
		double ans = solve();
		printf("Case #%d: %.15lf\n",i,ans);
	}
	return 0;
}
