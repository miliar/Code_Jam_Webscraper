#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#define MP make_pair
#define INFI (1 << 30)
#define INFL (1 << 60)
using namespace std;

typedef long long L;
typedef vector<int> VI;
typedef vector<L> VL;
typedef vector<bool> VB;
typedef vector<VI> VVI;

int main() {
	int cases;
	
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &cases);
	for (int tc = 1; tc <= cases; tc++) {
		int x, r, c;
		bool isRic;
		
		scanf("%d %d %d", &x, &r, &c);
		isRic = false;
		if ((r * c) % x != 0)
			isRic = true;
		else {
			if ((r < x - 1) || (c < x - 1))
				isRic = true;
		}
		printf("Case #%d: %s\n", tc, (isRic) ? "RICHARD" : "GABRIEL");
	}
	return 0;
}
