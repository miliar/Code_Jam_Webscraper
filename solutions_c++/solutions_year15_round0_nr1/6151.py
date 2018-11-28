#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <vector>
#define MP make_pair
#define INFI (1 << 30)
using namespace std;

typedef vector< pair<int, int> > VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<bool> VB;

int main() {
	int cases, mx, cnt, cur;
	char in[1005];
	
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &cases);
	for (int tc = 1; tc <= cases; tc++) {
		scanf("%d %s", &mx, in);
		cnt = cur = 0;
		for (int i = 0; i <= mx; i++) {
			if (cur < i) {
				cnt += (i - cur);
				cur += (i - cur);
			}
			cur += ((int) in[i] - '0');
		}
		printf("Case #%d: %d\n", tc, cnt);
	}
	return 0;
}
