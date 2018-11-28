//#pragma comment(linker,"/STACK:1024000000,1024000000")
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <cstdlib>
#include <queue>
#include <stack>
#include <utility>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
typedef long  long LL;

const int N = 100005;
const int M = 1000005;
const int inf = 1 << 28;
const int mod = 1e9 + 7;
const double eps = 1e-8;
using namespace std;
int n, x;
int a[N];



int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int T, cas = 1;
	cin >> T;
	while (T --) {
        scanf("%d%d", &n, &x);
        for (int i = 0; i < n ; i++) {
            scanf("%d", &a[i]);
        }
        sort(a, a + n);
        priority_queue<int> q;
        int res = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (!q.empty()) {
                int m = q.top();
                if (m >= a[i]) {
                    q.pop();
                    continue;
                }
            }
            q.push(x - a[i]);
            res ++;
        }
        printf("Case #%d: %d\n", cas ++, res);
	}
	return 0;
}











