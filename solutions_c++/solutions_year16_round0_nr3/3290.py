#include<bits/stdc++.h>

using namespace std;

#define endl '\n'
#define SZ(c) ll((c).size())
#define REP(i , n) for( ll i = 0; i < (n); i++ )
#define WAIT cout << flush, system("PAUSE")
typedef long long ll;

ll T, N, C;

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	
	cin >> T;
	REP(tc, T){
		cin >> N >> C;
		
    	cout << "Case #1:" << endl;
		ll xtra = (1ll<<(N-1)) + 1;
		N -= 2;
		
		REP(msk, 1<<N) if (C>0){
			ll x = 2*msk + xtra;
			
			//cout << x << endl;
			//for(ll I=N+1; I>=0; I--) cout << ((x&(1ll<<I))?1:0);
				
			vector<ll> div;
			for(ll base=2; base<=10; base++){
				ll curr = 0;
				for(ll I=N+1; I>=0; I--){
					curr = curr*base + ((x&(1ll<<I))?1:0);
				}
				
				//cout << base << " " << curr << endl;
				for(ll d=2; d*d<=curr; d++) if (curr%d==0){
					div.push_back(d);
					break;
				}
			}
			if (div.size()==9){
				for(ll I=N+1; I>=0; I--) cout << ((x&(1ll<<I))?1:0);
				
				for(auto d: div) cout << " " << d;
				cout << "\n";
				C--;
			}
		}
	}
}
/*1
6 3
Case #1:
100001 3 2 5 2 7 2 3 2 11
100011 5 13 3 31 43 3 73 7 3
100111 3 2 5 2 7 2 3 2 11
*/


















