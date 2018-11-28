#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstdio>
#include <cstring>
#include <climits>
#include <stack>
#include <cmath>
#include <set>
#include <map>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef map<int, int> mii;

int T;
int Smax;
const int Smax_limit = 1001;
int cnt[Smax_limit];
int cum[Smax_limit];

void solve()
{
	int lack = 0;
	memset(cum, 0, sizeof(cum));
	cum[0] = cnt[0];
	for (int i = 1; i <= Smax; ++i) {
		if (cnt[i] > 0 && cum[i-1] < i) {
			lack += i - cum[i-1];
			cum[i-1] += lack;
		}
		cum[i] = cum[i-1] + cnt[i];
	}
	printf("%d", lack);
	return;
}

int main()
{
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		memset(cnt, 0, sizeof(cnt));
		scanf("%d", &Smax);
		char ch; scanf("%c", &ch);
		for (int i = 0; i <= Smax; ++i) {
			scanf("%c", &ch);
			cnt[i] = ch - '0';
		}
		printf("Case #%d: ", t);
		solve();
		printf("\n");
	}
	return 0;
}
