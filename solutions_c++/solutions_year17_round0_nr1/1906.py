#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstdio>
#include<string>

using namespace std;

void work()
{
	string s;
	int k;
	cin >> s >> k;
	int len = (int)s.size();
	int ans = 0;
	for (int i = 0; i <= len - k; ++i) {
		if (s[i] == '-') {
			ans++;
			for (int j = i; j < i + k; ++j) {
				s[j] = (s[j] == '-' ? '+' : '-');
			}
		}
	}
	for (int i = len - k + 1; i < len; ++i) {
		if (s[i] == '-') {
			cout << "IMPOSSIBLE" << endl;
			return;
		}
	}
	cout << ans << endl;
}

int main()
{
	//freopen("A-large.in", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int q;
	cin >> q;
	for (int i = 1; i <= q; ++i) {
		printf("Case #%d: ", i);
		work();
	}
	return 0;
}
