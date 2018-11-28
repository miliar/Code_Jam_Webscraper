#include <bits/stdc++.h>
using namespace std;

int main(){
	ios::sync_with_stdio(false);

	int T;
	cin >> T;

	for(int t = 0; t < T; t++){
		string s;
		cin >> s;
		int ans = (s[s.size()-1] == '+') ? 0 : 1;
		for(size_t i = 1; i < s.size(); i++)
			if(s[i] != s[i-1])
				ans++;
		cout << "Case #" << t+1 << ": " << ans << endl; 
	}

	return 0;
}
