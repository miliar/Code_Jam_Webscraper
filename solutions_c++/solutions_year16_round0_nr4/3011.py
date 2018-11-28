#include <bits/stdc++.h>

#define INF 0x3f3f3f3f
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define ForC(i, n) for (int i = 0; i < int(n); i++)
#define ForD(i, n) for (int i = int(n-1); i >= 0; i--)

using namespace std;
const double PI = acos(-1.0);

typedef long long ll;
typedef pair<int, int> pii;

int main (void) {
	int t;
	scanf("%d", &t);
	for (int cases = 1; cases <= t; cases++) {
		int k, c, s;
		scanf("%d %d %d", &k, &c, &s);
		printf("Case #%d:", cases);
		for (int i = 1; i <= k; i++) printf(" %d", i);
		printf("\n");
	}
	return 0;
}
