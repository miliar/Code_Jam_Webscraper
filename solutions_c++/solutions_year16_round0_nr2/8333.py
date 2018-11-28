#include <bits/stdc++.h>

int main() {
	int T;
	
	scanf("%d",&T);
	for(int tc = 1; tc <= T; tc++) {
		std::string str;
		int ans = 0;
		
		std::cin >> str;
		
		for(int i = 1; i < (int)str.length(); i++) {
			ans += (str[i] != str[i-1]);
		}
		ans += (str[str.length()-1] == '-');
		
		printf("Case #%d: %d\n",tc,ans);
	}
	
	return 0;
}
