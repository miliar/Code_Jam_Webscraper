#include <bits/stdc++.h>
using namespace std;

int main() {
	int t, T=1, n;
	scanf("%d", &t);
	while(t--) {
		string s, ans="";
		cin >> s;
		char c=s[0];
		ans+=s[0];
		for(int i=0; i<s.size(); ) {
			int j;
			for(j=i+1; j<s.size(); j++) if(s[j]>=c) {
				c=s[j];
				break;
			}
			if(j<(int)s.size()) ans.insert(ans.begin(), s[j]);
			for(int k=i+1; k<j; k++) ans+=s[k];
			i=j;
		}
		printf("Case #%d: %s\n", T++, ans.c_str());
	}
	return 0;
}
