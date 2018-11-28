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
int n;
int a[N];
int x[N], y[N];

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int T, cas = 1;
	cin >> T;
	while (T --) {
        scanf("%d", &n);
        for (int i = 0; i < n ; i++) {
            scanf("%d", &a[i]);
        }
        int res = 0;
        for (int i = 0; i < n; i++) {
            x[i] = y[i] = 0;
            for (int j = 0; j < i; j++) {
                if (a[i] < a[j]) x[i] ++;
            }
            for (int j = i + 1; j < n; j++) {
                if (a[i] < a[j]) y[i] ++;
            }
            res += min(x[i], y[i]);
        }
        printf("Case #%d: %d\n", cas ++, res);
	}
	return 0;
}











