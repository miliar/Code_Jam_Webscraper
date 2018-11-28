#include<bits/stdc++.h>
using namespace std;
#define fileio freopen("in.txt","r",stdin); freopen("out.txt","w",stdout);
#define boost  ios_base::sync_with_stdio(false);


int main() {
	fileio;
	boost;
	int t, tt = 0, ans = 0;
	cin >> t;
	while(t--) {
		tt++;
		cout << "Case #"<<tt<<": ";
		string s;
		cin >> s;
		s += '+';
		ans = 0;
		for(int i = 1; i < s.length(); i++)
			if(s[i] != s[i-1]) ans++;
		cout << ans << "\n";		
	}
	return 0;
}
