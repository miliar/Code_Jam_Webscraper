#include <stdio.h>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int n;
string a;

void input()
{
	cin >> n >> a;
}

void process()
{
	int ans = 0;
	int cnt = 0;
	for (int i = 0; i <= n; i++) {
		if (a[i] > '0') {
			ans += (i - min(i, cnt));
			cnt += (i - min(i, cnt));
		}
		cnt += a[i] - '0';
	}
	cout << ans << endl;
}

int main()
{
	int t;
	freopen("output.txt", "wt", stdout);
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		input();
		process();
	}
	return 0;
}