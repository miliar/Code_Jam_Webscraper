#include <bits/stdc++.h>

using namespace std;

int T,K;
string s;

int main() {
	cin >> T;
	for (int cas=1;cas<=T;cas++) {
		cin >> s >> K;
		int r=0;
		for (int i=0;i+K<=s.size();i++) if (s[i]=='-') {
			r++;
			for (int j=i;j<i+K;j++) s[j]=s[j]=='+'?'-':'+';
		}
		printf("Case #%d: ",cas);
		bool succ=1;
		for (int i=0;i<s.size();i++) if (s[i]=='-') succ=0;
		if (succ) printf("%d\n",r);
		else printf("IMPOSSIBLE\n");
	}
}
