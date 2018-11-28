#include <cstdio>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <iostream>
#include <queue>
#include <list>
#include <ctime>

using namespace std;

#define mp make_pair
#define sqr(a) ((a)*(a))

typedef long double ld;
typedef long long ll;

const int MAXN = 5e3;
const int INF = 1e9 + 7;

void solve(string &s)
{
	for (int i = 0; i < s.length(); ++i)
		s[i] = (s[i] == '+');

	reverse(s.begin(), s.end());
	int ans = 0;
	for (int i = 0; i < s.length(); ++i)
		if (!s[i]) {
			++ans;
			for (int j = i + 1; j < s.length(); ++j)
				s[j] = !s[j];
		}

	printf("%d\n", ans);
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int t;
	scanf("%d\n", &t);
	for (int i = 1; i <= t; ++i) {
		string s;
		getline(cin, s);
		printf("Case #%d: ", i);
		solve(s);
	}

	return 0;
}