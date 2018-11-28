#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cmath>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
using namespace std;
#define mem(x) memset(x,0,sizeof x)
#define LL long long
const int maxn = 1010;
char s[maxn];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin.tie(NULL);
	int t; cin >> t;
	for (int kcase = 1; kcase <= t; kcase++)
	{
		scanf("%s", s);
		string ans = "";
		int len = strlen(s);
		char maxs = 'A' - 1;
		ans.push_back(s[0]);
		maxs = max(s[0], maxs);
		for (int i = 1; i < len; i++)
		{
			if ( s[i] > maxs||s[i]==maxs) { ans = s[i] + ans; maxs = max(s[i], maxs); }
			else ans = ans + s[i];
		}
		printf("Case #%d: ", kcase);
		cout << ans << endl;
	}
	return 0;
}