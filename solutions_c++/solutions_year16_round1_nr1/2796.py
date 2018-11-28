#include <bits/stdc++.h>
using namespace std;
#define ULL unsigned long long
#define LL long long
#define INF 0x3f3f3f3f
#define MAXN 1
#define mod 1000000007
#define rep(i,n) for(int i = 0; i < n; ++i)
#define Rep(i,n) for(int i = 1; i <= n; ++i)

void dfs(string s) {
	if(s.length() == 0) return;
	int p = 0;
	rep(i, s.length()) if(s[i] >= s[p]) p = i;
	cout << s[p];
	dfs(s.substr(0, p));
	cout << s.substr(p+1, s.length()-p-1);
}

int main()
{
	int t, cas = 0;
	cin >> t;
	while(cas++ < t) {
		string s;
		cin >> s;
		printf("Case #%d: ", cas);
		dfs(s);
		puts("");
	}
	return 0;
}

