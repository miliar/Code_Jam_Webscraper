#include <bits/stdc++.h>

using namespace std;

long long t,i,n,ans,tes;
char s[1500007];
stack<char> st;

int main() {
	scanf("%lld",&t);
	for (tes=1; tes<=t ; tes++) {
		scanf("%s",&s);
		n = strlen(s);
		
		while (!st.empty()) st.pop();
		for (i=0 ; i<n ; i++) {
			if (st.empty()) {
				st.push(s[i]);
			} else if (s[i] == st.top()) {
				st.pop();
			} else {
				st.push(s[i]);
			}
		}
		
		ans = n * 5 - 5 * st.size() / 2;
		printf("Case #%lld: %lld\n",tes,ans);
	}
}
