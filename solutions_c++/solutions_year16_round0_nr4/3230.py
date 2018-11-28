#include<bits/stdc++.h>

using namespace std;

#define endl '\n'
#define rep(i , n) for( int i = 0; i < (n); i++ )

typedef long long ll;
typedef pair<int, int> pii;

ll K , C , S;

ll mpow(ll x , ll n){
	ll res = 1;
	for( int i = 1; i <= n; i++ ){
		res = res * x;
	}
	return res;
}

int main(){

	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int tc;
	cin >> tc;
	for(int cc = 1; cc <= tc; cc++ ){
		cout << "Case #" << cc << ": ";
		cin >> K >> C >> S;		
		if(K != S){
			cout << endl;
		}
		else{
		
			for( ll i = 1; i <= K; i++ )
				cout << (i - 1) * mpow(K, C - 1) + 1 << " \n"[i == K];
		}
	}
}
