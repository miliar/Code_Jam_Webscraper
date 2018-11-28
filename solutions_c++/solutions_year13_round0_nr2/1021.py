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

int n,m;
int a[100][100];
int row[100],col[100];

string solve(){
	cin>>n>>m;
	FOR(i,n) FOR(j,m) cin>>a[i][j];
	FOR(i,n){
		int mx = 0;
		FOR(j,m) mx = max(mx,a[i][j]);
		row[i] = mx;
	}
	FOR(i,m){
		int mx = 0;
		FOR(j,n) mx = max(mx,a[j][i]);
		col[i] = mx;
	}

	FOR(i,n) FOR(j,m){
		int cut = min(row[i],col[j]);
		if(cut != a[i][j]) return "NO";
	}
	return "YES";
}

int main(){
	int t; cin>>t;
	for(int i = 1; i <= t; i++){
		string ret = solve();
		printf("Case #%d: %s\n",i,ret.c_str());
	}
	return 0;
}
