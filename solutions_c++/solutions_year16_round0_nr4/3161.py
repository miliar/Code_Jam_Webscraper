#include<bits/stdc++.h>

#define REP(i , n) for( int i = 0; i < (n); i++ )
using namespace std;
typedef long long ll;

ll T, K, C, S;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	
	cin >> T;
	REP(tc, T){
		cin >> K >> C >> S;
		
		ll pw = 1;
		REP(I, C-1) pw *= K;
		
		cout << "Case #" << tc+1 << ": ";
		REP(I, K) cout << (I+1)*pw << " \n"[I+1==K];
	}
}
