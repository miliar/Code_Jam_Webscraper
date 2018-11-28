#include<iostream>
#include<cstdio>
#include<cstring>
#include<string.h>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
#define LL long long 
const int maxn = 110;
string s[maxn];
char ch[maxn][2];
int cnt[2];
int dp[maxn][maxn];
bool cmp(const string&s1, const string&s2)
{
	return s1.size() < s2.size();
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T; cin >> T;
	int ca = 0;
	int n;
	while (T--) {
		scanf("%d", &n);
		++ca;
		printf("Case #%d: ", ca);
		for (int i = 0; i < n; ++i) cin >> s[i];
		sort(s, s + n, cmp);
		int n = s[0].length(), m = s[1].length();
		char pre = ' ';
		int cnt = 0;
		bool ok = true;
		while (true) {
			if (s[0].empty() && s[1].empty()) break;
			else if (s[0].empty()) {
				for (int j = 0; j < s[1].size(); ++j)
				if (s[1][j] != pre) ok = false;
				else ++cnt;
				break;
			}
			else if (s[1].empty()) {
				for (int j = 0; j < s[0].size(); ++j)
				if (s[0][j] != pre) ok = false;
				else ++cnt;
				break;
			}

			if (s[0][0] == s[1][0]) {
				pre = s[0][0];
				s[0].erase(s[0].begin());
				s[1].erase(s[1].begin());
			}
			else if (s[0][0] == pre) {
				s[1] = pre + s[1];
				++cnt;
			}
			else if (s[1][0] == pre) {
				s[0] = pre + s[0];
				++cnt;
			}
			else {
				ok = false; break;
			}
		}
		if (!ok) printf("Fegla Won\n");
		else printf("%d\n", cnt);
	}
}