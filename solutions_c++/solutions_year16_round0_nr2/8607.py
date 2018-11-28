#include <bits/stdc++.h>

typedef long long int ll;
typedef unsigned long long int ull;
#define rep(i,n) for(ll i=0;i<(n);i++)
 
using namespace std;

int main(){
	ll times;
	cin >> times;
	rep(t, times){
		string s;
		cin >> s;

		char c = s[0];
		ll count;
		if(c == '-'){
			count = 1;
			for(ll i = 1; i < s.length(); i++){
				if(c != s[i]){
					if(s[i] == '-')	count += 2;
					c = ((c == '+')? '-':'+');
				}
			}
		}
		else if(c == '+'){
			count = 0;
			for(ll i = 1; i < s.length(); i++){
				if(c != s[i]){
					if(s[i] == '-')	count += 2;
					c = ((c == '+')? '-':'+');
				}
			}
		}
		cout << "Case #" << t+1 << ": " << count << endl;
	}

	return 0;
}