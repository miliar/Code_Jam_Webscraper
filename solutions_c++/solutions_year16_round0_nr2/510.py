#include<bits/stdc++.h>
using namespace std;

int main() {
	int T;
	cin >> T;
	for(int i=0; i<T; i++) {
		string s;
		cin >> s;
		s += "+";
		int ans = 0;
		for(int j=0; j<s.size()-1; j++) {
			if(s[j] != s[j+1]) ans++;
		}
		
		cout << "Case #" << i+1 << ": " << ans << endl;
		
		
	}
	return 0;
}

