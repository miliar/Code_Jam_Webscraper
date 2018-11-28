#include<bits/stdc++.h>
#include<ext/numeric>
using namespace std;
using namespace __gnu_cxx;

#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz(v)  (int)v.size()
#define UNVISITED -1
#define CLR(a,v) memset(a,v,sizeof a)
#define PC(x) __builtin_popcount(x)

typedef long long ll;
typedef pair<int, int> ii;
typedef pair<ll, ll> pll;
typedef unsigned long long ull;

int dx[] = { 0, 0, 1, -1, -1, -1, 1, 1 };
int dy[] = { 1, -1, 0, 0, 1, -1, 1, -1 };

string s;

int main() {
#ifndef ONLINE_JUDGE
	freopen("B-large.in", "rt", stdin);
	freopen("out.txt", "wt", stdout);
#endif
	int t;
	cin >> t;
//	scanf("%d", &t);
	for (int c = 1; c <= t; ++c) {
		printf("Case #%d: ", c);
		cin >> s;
		int len = sz(s);
		int ans = 0;
		for (int i = 0; i < len - 1; ++i)
			ans += s[i] != s[i + 1];
		if (s[len - 1] != '+')
			++ans;
		printf("%d\n", ans);
	}
}

