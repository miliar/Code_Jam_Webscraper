#include <bits/stdc++.h>
using namespace std;

const int MAXN=1005;

inline void solve()
{
	string s,ans;
	cin >> s;
	ans+=s[0];
	for (int i=1;i<s.length();i++)
	{
		if (s[i]>=ans[0]) ans=s[i]+ans;
		else ans+=s[i];
	}
	cout << ans << endl;
}

int main()
{
	freopen("read.txt","r",stdin);
	freopen("write.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for (int i=1;i<=T;i++)
	{
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}
