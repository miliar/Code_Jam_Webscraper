#include <bits/stdc++.h>
#define rep(i,n) for(int i = 0; i < n; i++)
#define INF 100000000
#define EPS 1e-10
#define MOD 1000000007
using namespace std;
typedef pair<int,int> P;
typedef long long ll;

ll N, J;

void solve(){
	cin >> N >> J;
	ll x = (1<<(N-1))+1, y;
	ll cnt = 0;
	ll ans[10], out;
	rep(i,1<<(N-2)){
		y = i*2+x;
		ll num = 0;
		for(ll u = 2; u <= 10; u++){
			ll z = 0, Y = y, rank = 1;
			while(Y){
				if(Y&1) z += rank;
				Y >>= 1;
				rank *= u;
			}
			if(u == 10) out = z;
			for(ll j = 2; j*j <= z; j++){
				if(z%j == 0){
					ans[u-1] = j;
					num++;
					break;
				}
			}
			if(num != u-1) break;
		}
		if(num == 9){
			cnt++;
			cout << out;
			for(ll j = 1; j <= 9; j++) cout << " " << ans[j];
			cout << endl;
		}
		if(cnt == J) break;
	}
}

int main(){
	int T;
	cin >> T;
	rep(i,T){
		printf("Case #%d:\n",i+1);
		solve();
	}
}