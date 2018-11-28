#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

const int MAXN = 1010;

char s[MAXN];
int k;

void solve() {
	scanf("%s %d\n", s, &k);
	int n = strlen(s);
	int res = 0;
	for (int i = 0; i <= n - k; ++i) {
		if (s[i] == '-') {
			res++;
			for (int j = i; j < i + k; ++j) {
				if (s[j] == '-')
					s[j] = '+';
				else
					s[j] = '-';
			}
		}
	}
	for (int i = n - k + 1; i < n; ++i) {
		if (s[i] == '-') {
			cout << "IMPOSSIBLE";
			return;
		}
	}
	cout << res;
	return;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d\n", &t);
	for (int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
	fclose(stdin);
	fclose(stdout);
}
