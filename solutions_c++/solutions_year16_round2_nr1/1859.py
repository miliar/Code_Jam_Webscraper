#include <stdio.h>
#include <string>
#include <algorithm>
#include <queue>
#include <stdlib.h>
#include <vector>
#include <iostream>
#include <string>
#define mod 1000000007
#define INT_MAX 2147483647
using namespace std;
int t, tt, cnt[30], n;
string alpha[10] = { "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };
string ans, str;
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-la.out", "w", stdout);
	char must[15] = "zowrufxsgn";
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		printf("Case #%d: ", tt);
		memset(cnt, 0, sizeof(cnt));
		ans = "";
		cin >> str;
		n = str.length();
		for (int i = 0; i < n; i++)	cnt[str[i] - 'A']++;
		for (int i = 0; i < 10; i+=2)
		{
			while (cnt[must[i] - 'a'])
			{
				for (int j = 0; j < alpha[i].length(); j++) cnt[alpha[i][j]-'a']--;
				ans += ('0' + i);
			}
		}
		for (int i = 1; i < 10; i += 2)
		{
			while (cnt[must[i] - 'a'])
			{
				for (int j = 0; j < alpha[i].length(); j++) cnt[alpha[i][j]-'a']--;
				ans += ('0' + i);
			}
		}
		sort(ans.begin(), ans.end());
		cout << ans << endl;
	}
	return 0;
}
