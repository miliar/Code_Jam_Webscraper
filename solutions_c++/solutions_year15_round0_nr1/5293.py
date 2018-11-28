#include <set>
#include <map>
#include <cmath>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

#define pb push_back
#define mp make_pair
#define sz(a) (int)a.size()
#define ms(a, x) memset(a, x, sizeof a)
#define all(a) a.begin(), a.end()
#define forit(i, s) for (__typeof(s.begin()) i = s.begin(); i != s.end(); i++)

typedef long long ll;
typedef pair<int,int> pt;

const int N = 1<<20;
const int inf = 1<<30;

char s[10100];
int len;

bool ok(int cur) {
	cur += s[0];
	for (int i = 1; i <= len; i++) {
		for (int x = 0; x < s[i]; x++) {
			if (cur < i)
				return false;
			cur++;
		}
	}
	return true;
}

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int tests;
	scanf("%d\n", &tests);
	for (int t = 1; t <= tests; t++) {
		scanf("%d %s", &len, s);

		for (int i = 0; i <= len; i++)
			s[i] -= '0';

		int ans = 0;
		while (!ok(ans))
			ans++;

		printf("Case #%d: %d\n", t, ans);
	}

	return 0;
}