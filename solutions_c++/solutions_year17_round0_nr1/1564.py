#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(){
	int t, k;
	string s;
	cin >> t;
	for(int _t = 1; _t <= t; _t++) {
		cin >> s >> k;
		int c = 0;
		int l = s.length();
		for(int i=0; i<=l-k; i++) {
			if(s[i] == '-') {
				c++;
				for(int j=i; j<i+k; j++) {
					if(s[j] == '+') s[j] = '-';
					else s[j] = '+';
				}
			}
		}
		
		printf("Case #%d: ", _t);
		
		bool flag = true;
		for(int i=l-k+1; i<l; i++) {
			if(s[i] == '-') { flag = false; break; }
		}
		
		if(flag) cout << c;
		else cout << "IMPOSSIBLE";
		cout << endl;
	}
	
	return 0;
}
