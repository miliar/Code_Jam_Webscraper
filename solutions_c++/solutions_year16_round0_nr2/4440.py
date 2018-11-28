#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<algorithm>
#include<cmath>
#include<string.h>
#include<stdio.h>
#include<queue>

using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t,i,k,l,ans;
	char s[105];
	cin >> t;
	k = 1;
	while (t--)
	{
		cin >> s;
		l = strlen(s);
		s[l] = '+';
		ans = 0;
		for (i = l - 1; i >= 0; i--)
		{
			if (s[i] != s[i + 1]) ans++;
		}
		cout << "Case #" << k++ << ": " << ans << endl;
	}
}