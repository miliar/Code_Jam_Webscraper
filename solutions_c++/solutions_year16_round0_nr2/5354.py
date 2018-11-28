#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;

#define FOR(i,a,b) for(ll i=(a); i < (b); i++)
#define FORD(i,a,b) for(ll i=(b)-1; i >=(a); i--) 

int main() {
	ios_base::sync_with_stdio(false);
	
	ll T;
	cin >> T;
	FOR(q,0,T) {
		string S;
		cin >> S;
		ll counter=0;	
		char curr = S.at(0);
		FOR(i,1,S.length()) {
			if(curr !=S.at(i)) {
				counter++;
				curr=S.at(i);
			}		
		}
		if(curr == '-')
			counter++;

		cout << "CASE #" << q+1 << ": " << counter << endl; 
	}
}
