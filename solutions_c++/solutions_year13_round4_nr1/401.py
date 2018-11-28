#include<iostream>
#include<sstream>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<complex>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cassert>

#define rep(i,n) for(int i=0;i<(int)n;i++)
#define all(c) (c).begin(),(c).end()
#define mp make_pair
#define pb push_back
#define each(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
#define dbg(x) cerr<<__LINE__<<": "<<#x<<" = "<<(x)<<endl

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;
const int inf = (int)1e9;
const double INF = 1e12, EPS = 1e-9;

const int mod = 1000002013;
int n, m, p;
ll calc(int s, int t){
	t -= s;
	/*
	dbg(t);
	dbg(((ll)n * t - t * (t - 1ll) / 2) % mod);
	*/
	return ((ll)n * t - t * (t - 1ll) / 2) % mod;
}

void run(){
	cin >> n >> m;
	map<ll, ll> M;
	deque<ll> num, pos;
	ll ans = 0;
	
	rep(i, m){
		int a, b, c;
		cin >> a >> b >> c;
		M[a] += c;
		M[b] -= c;
		(ans += calc(a, b) * c % mod) %= mod;
	}
	
	each(i, M){
		while(i->second < 0){
			assert(num.size());
			ll t = min(-i->second, num.back());
			num.back() -= t;
			i->second += t;
			(ans += mod - t * calc(pos.back(), i->first) % mod) %= mod;
			
			if(num.back() == 0) num.pop_back(), pos.pop_back();
		}
		if(i->second > 0){
			num.pb(i->second);
			pos.pb(i->first);
		}
	}
	cout << ans << endl;
}

int main(){
	int CS;
	cin >> CS;
	rep(cs, CS){
		cout << "Case #" << cs + 1 << ": ";
		run();
	}
	return 0;
}
