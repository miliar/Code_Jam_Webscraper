#include <bits/stdc++.h>
 
using namespace std;
 
int main() {
	int T, ans;
	string s;

	cin >> T;
	for(int it = 1; it <= T; ++it) {
		cin >> s;
		ans = 0;
		for (unsigned i = 0; i < s.size(); i++) {
			if(i == 0 || s[i] == s[i-1])
				continue;
				ans++;			
		}
		
		if(s[s.size() - 1] == '-')
				ans++;
		printf("Case #%d: %d\n", it, ans);
	}
	return 0;
}
