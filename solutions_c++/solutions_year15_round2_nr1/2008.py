// Author : Bony Roopchandani
// 

// INCLUDES
#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <tuple>
#include <vector>
using namespace std;

// MACROS
#define all(a) a.begin(), a.end()
#define eb emplace_back
#define in(a) freopen(a, "r", stdin)
#define ll long long
#define mt make_tuple
#define out(a) freopen(a, "w", stdout)
#define rep(i, n) for(int i=0; i<n; i++)
#define repd(i, a, b) for(int i=a; i>=b; i--)
#define rept(i, a, b) for(int i=a; i<=b; i++)
#define sz size()

// CONSTS
const bool TESTING=true;
const double EPS = (1e-11);
const double PI = acos(-1.0);
const int INF = 9999999;
const int MOD = (1e9 + 7);

ll n, rev[1000005];

ll reverse(ll n) {
	ll ret=0;
	while(n) {
		ret=ret*10+n%10;
		n/=10;
	}
	return ret;
}

void pre() {
	rept(i, 1, 1000000) {
		rev[i]=reverse(i);
	}
}

ll bfs(ll n) {
	queue<tuple<ll, ll>> Q;
	bool vis[1000005]={0};
	Q.push(mt(1,1));
	vis[1]=true;
	while(!Q.empty()) {
		ll N=get<0>(Q.front());
		ll s=get<1>(Q.front());
		Q.pop();
		if(N==n)
			return s;
		ll a=N+1, b=rev[N];
			if(!vis[a]) {
				Q.push(mt(a, s+1));
				vis[a]=true;
			}
			if(!vis[b] and b<=n) {
				Q.push(mt(b, s+1));
				vis[b]=true;
			}
	}
}

int main(void) {
	ios_base::sync_with_stdio(TESTING);
	in("A.in");
	out("A.out");
	int T, cs=1; cin>>T;
	pre();
	while(T--) {
		ll curr=1, steps=1; cin>>n;
		steps=bfs(n);
		cout<<"Case #"<<(cs++)<<": "<<steps<<endl;
	}
	return (0);
}