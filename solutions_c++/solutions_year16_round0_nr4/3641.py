#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;


#define FOR(i,a,b) for(ll i =(a); i < (b); i++)
int main() {
	ios_base::sync_with_stdio(false);
	
	ll T;
	cin >> T;
	FOR(q,0,T) {
		ll K,C,S;
		cin >> K >> C >> S;
		cout << "Case #" << q+1 << ":";
		FOR(i,1,S+1) {
			cout << " " << i;		
		}
		cout << endl;
	}

}
