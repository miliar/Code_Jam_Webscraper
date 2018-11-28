#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
using namespace std;
int a[1005], b[1005], n;
string s;
int get(string s)
{
	int res = 0;
	for (int i = 2; i < s.length(); i++) 
		res = res * 10 + s[i] - '0';
	return res;
}
bool check(int x)
{
	for (int i = x; i < n; i++)
		if (a[i] < b[i - x])
			return false;
	return true;
}
int main()
{
	freopen("dd.in", "r", stdin);
	freopen("d-large.out", "w", stdout);
	int T, cas;
	cin >> T;
	for (cas = 1; cas <= T; cas++) {
		cin >> n;
		for (int i = 0; i < n; i++) {
			cin >> s;
			a[i] = get(s);
		}
		for (int i = 0; i < n; i++) {
			cin >> s;
			b[i] = get(s);
		}
		sort(a, a + n);
		sort(b, b + n);
		int i = 0, j = 0;
		while (i < n && j < n) {
			if (b[j] < a[i])
				j++;
			else
				i++, j++;
		}
		int ans2 = n - i;
		i = 0;
		while (i < n) {
			if (check(i))
				break;
			i++;
		}
		int ans1 = n - i;
		printf("Case #%d: %d %d\n", cas, ans1, ans2);
	}
	return 0;
}
