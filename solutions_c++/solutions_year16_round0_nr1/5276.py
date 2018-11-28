#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;

#define FOR(i,a,b) for(ll i=(a); i < (b); i++) 
#define FORD(i,a,b) for(ll i=(b); i >=(a); i--)
int main() {
	ios_base::sync_with_stdio(false);
	
	ll t;
	cin >> t;

	FOR(q,0,t) {
		bool flag = false;	
		vector<bool>digits;
		FOR(i,0,10) {
			digits.push_back(false);
		}
		
		ll val = 0;
		ll input;
		cin >> input;
		ll old = -1;

		ll counter = 1;
		while(!flag) {
			val=counter*input;
			string curr = to_string(val);
			FOR(i, 0, curr.length()) {
				digits[curr.at(i)-'0'] = true;
			}
			flag = true;
			FOR(i,0, digits.size()) {	
				if(!digits[i]) {
					flag = false;
				}
			}
			if(val <= old) {
				flag = true;
				val = -1;
			}
			old = val;
			counter++;
		}
		if(val >= 0) {
			cout << "CASE #" << q+1 << ": " << val << endl;	
		} else {
			cout << "CASE #" << q+1 << ": INSOMNIA" << endl;
		}
	}
}
