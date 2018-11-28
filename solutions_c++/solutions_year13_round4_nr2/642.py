#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cmath>
#include <map>
#include <vector>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <functional>
#include <algorithm>
#include <utility>
#include <ctime>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pdd pair<double,double>
#define vi vector<int>
#define rep(i,n) for( int i = 0; i < (n); i++ )
#define forn(i,a,b) for( int i = (a); i < (b); i++ )
#define fi first
#define se second

const int MXN = 1010;

	int n,p;
int mxB( int a ){
	int res = 0;
	a++;
	while(a>1){
		res++;
		a>>=1;
	}
	return ((1<<res) - 1)*(1<<(n-res));
}
int mnB( int a ){
	int res = 0;
	a = (1<<n)-a;
	while(a>1){
		res++;
		a>>=1;
	}
	return (1<<(n-res)) - 1;
}

pii solve(){
	scanf("%d%d", &n, &p);
		
	int mx = (1<<n);

	pii ans;

	rep(i,mx){
		if( mxB(i)<p ) ans.first = i;
		if( mnB(i)<p ) ans.second = i;
	}

	return ans;
}

int main(){
	freopen("B.in", "r", stdin);	freopen("B.out", "w", stdout);

	int T;

	scanf("%d", &T);

	rep(i,T){
		pii a = solve();
		cout<<"Case #"<<i+1<<": "<<a.first<<" "<<a.se<<endl;
	}
}