#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
#include <deque>
#include <cmath>
#include <cstdlib>
#include <map>
#include <climits>
#include <limits>
#include <functional>
#include <bitset>
using namespace std;
#define LL long long
#define LD long double
#define mod 1000000007


void input() {

}

char str[1001];

void solve() {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%s", str);
		string s = str;
		string re = "";
		int len = strlen(str);
		for (int j = 0; j < len; j++) {
			if (!j)
				re = s[j];
			else if (re[0] <= s[j])
				re = s[j] + re;
			else
				re += s[j];
		}
		printf("Case #%d: %s\n", i + 1, re.c_str());
	}
}

int main(void) {
	//freopen("input.txt", "r", stdin);
	//freopen("ALout.txt", "w", stdout);
	solve();
	return 0;
}