#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <algorithm>
#include <bitset>

using namespace std;

void solve(int id) {
    int p, q;
    scanf("%d/%d", &p, &q);
    if ((q &(-q)) != q) { 
        printf("Case #%d: impossible\n", id); 
        return;
    }
    int ans = 0;
    while (p < q) {
        ans ++;
        p = p<<1;
    }
	// output
	printf("Case #%d: %d\n", id, ans > 0 ? ans:1);
}

int main() {
    freopen("d:\\gcj\\small.in", "r", stdin);
    freopen("d:\\gcj\\small.ans", "w", stdout);
	int t = 0;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		solve(i);
	}
    return 0;
}