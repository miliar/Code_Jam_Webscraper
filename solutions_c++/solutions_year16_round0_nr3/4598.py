#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

ll conv(int s, int b){
	ll r = 0;
	ll p = 1;
	for(int i = 0; i < 17; i++){
		if((s & (1 << i)) != 0)
			r += p;
		p *= b;
	}
	
	return r;
}

ll div(ll x){

	for(ll i = 2; i * i <= x; i++){
		if((x % i) == 0) return i;
	}
	return -1;
}

void print(ll x, ll s){
	for(int i = s - 1; i >= 0; i--){
		if( (x & (1 << i)) != 0) cout << 1;
		else					 cout << 0;
	}

}

void solve(int n, int k){

	int b = 1 << (n - 1);
	for(int i = b; i < (1  << n) && k > 0; i++){
		
		if(i & 1){
			
			vector<ll> tsol;
			for(int j = 2; j <= 10; j++){
				ll fd = div(conv(i, j));
					
				if(fd != -1){
					tsol.emplace_back(fd);
				}else{
					break;
				}			
			}

			if(tsol.size() == 9){				
				print(i, n);
				for(int j = 0; j < tsol.size(); j++)
					cout << " " << tsol[j];
				cout << endl;
				
				k--;
			}
			
		}
		
	}
}

int main(){
	int t, nc = 0;
	cin >> t;
	while( t--){
		int n,k; cin >> n >> k;
		cout << "Case #" << ++nc << ":" << endl;
		solve(n, k);
	}
}
