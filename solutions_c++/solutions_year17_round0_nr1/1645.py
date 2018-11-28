#include <bits/stdc++.h>

using namespace std;

int main() {
	
	int T;
	cin >> T;
	
	for(int tt = 1; tt <= T; tt++) {
		printf("Case #%d: ", tt);
		string s;
		cin >> s;
		int K;
		cin >> K;
		
		int count = 0;
		for(int i = 0; i <= (int)s.length()-K; i++) {
			if(s[i] == '-') {
				count++;
				for(int j = i; j < i+K; j++) {
					s[j] = s[j]=='-'?'+':'-';
				}
			}
		}
		
		for(int i = 0; i < (int)s.length(); i++) {
			if(s[i] == '-') count = -1;
		}
		
		if(count < 0) printf("IMPOSSIBLE\n");
		else printf("%d\n", count);
	}
	
	return 0;
}
