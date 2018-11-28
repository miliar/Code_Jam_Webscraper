#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;

#define FOR(i,a,b) for(ll i=(a); i < b; i++)
#define FORD(i,a,b) for(ll i=(b)-1; i >=(a); i--)

int main() {
	ios_base::sync_with_stdio(false);
	

	ll T;
	cin >> T;
	FOR(q,0,T) {
	string input;
	cin >> input;
	
	vector<char> output;
	output.push_back(input.at(0));
	
	FOR(i,1,input.length()) {
		if(input.at(i) >= output[0]) {
		//	output.push_front(input.at(i);
			output.insert(output.begin(), input.at(i));
		} else {
			output.push_back(input.at(i));
		}	
	}
	
	cout << "Case #" << q+1 << ": "; 
		FOR(i,0,output.size()) {
			cout << output[i];
		}
	}
	cout << endl;
}

