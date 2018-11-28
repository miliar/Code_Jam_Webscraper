// in the name of God
#include <algorithm>
#include <iostream>
#include <string>

#define endl "\n"

using namespace std;

int main() { ios::sync_with_stdio(0); cin.tie(0);
	int T, X = 1;
	cin >> T;
	while(T--) {
		string s;
		cin >> s;
		int n = s.size();
		int ans = 0;
		for(int i=0; i<n-1; i++) {
			if(s[i] != s[i+1]) ans++;
		}
		if(s[n-1] == '-') ans++;
		cout << "Case #" << X++ << ": " << ans << endl;
	}
	return 0;
}