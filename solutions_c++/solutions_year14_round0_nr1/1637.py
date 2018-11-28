#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <queue>
#include <bitset>
#include <set>
#include <map>
#include <algorithm>
#include <iomanip>
#include <limits>

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;
typedef pair<LL, LL> PLL;
typedef pair<int, double> PID;
typedef pair<double, double> PDD;

#define pb(x) push_back(x)
#define X first
#define Y second

int T, cases, r, x, ans, cnt;
bool table[17];

int main(){
	for (scanf("%d", &T), cases = 1; cases <= T; ++cases) {
		printf("Case #%d: ", cases);
		memset(table, 0, sizeof(table));
		cnt = 0;
		scanf("%d", &r);
		for (int i = 1; i <= 4; ++i) {
			for (int j = 1; j <= 4; ++j) {
				scanf("%d", &x);
				if (i == r) table[x] = true;
			}
		}
		scanf("%d", &r);
		for (int i = 1; i <= 4; ++i) {
			for (int j = 1; j <= 4; ++j) {
				scanf("%d", &x);
				if (i == r && table[x]) {
					ans = x;
					++cnt;
				}
			}
		}
		if (cnt == 1) printf("%d\n", ans);
		else if (cnt > 1) printf("Bad magician!\n");
		else printf("Volunteer cheated!\n");
	}
}
