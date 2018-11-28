#include<bits/stdc++.h>

using namespace std;


int main() {

	freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
	int t, tt = 0, val = 0;
	cin >> t;
	
	while(t--) {
		tt++;
		cout << "Case #"<<tt<<": ";
		string s;
		cin >> s;
		s += '+';
		val = 0;
		for(int i = 1; i < s.length(); i++)
			if(s[i] != s[i-1]) val++;
		cout << val << "\n";
	}
	return 0;
}
