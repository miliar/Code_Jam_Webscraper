#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define pf push_front

int t;

int main(void){
	ios_base::sync_with_stdio(false);
	cin >> t;

	for(int k = 1; k <= t; k++){
		string s;
		cin >> s;

		string res;
		res.pb(s[0]);
		for(int i = 1; i < s.size(); i++){
			if(s[i] >= res[0]){
				res = s[i] + res;
			}
			else{
				res.pb(s[i]);
			}
		}
		cout << "Case #" << k << ": " << res << '\n';
	}
}
