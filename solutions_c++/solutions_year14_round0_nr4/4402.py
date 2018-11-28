#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <queue>
#include <vector>
#include <set>
#include <stack>
#include <map>
#include <math.h>
#include <time.h>
#include <string>
using namespace std;
typedef long long LL;
const int INF = 0x3f3f3f3f;
const int N = 1010;
const int M = 1605;
const int MOD = 1000000007;

using namespace std;
double a[N];
double b[N];

int deal(int l, int n)
{
	int cnt = 0;
	int i = l + 1;
	int j = 1;
	for (; i <= n && j <= n-l; i++, j++){
		while (b[j] > a[i]) {
            i++;
        }
		if (i <= n) {
            cnt++;
        }
	}
	return cnt;
}

int solve(int l, int n)
{
	int cnt = 0;
	int ans = 0;
	int i = l + 1;
	int j = 1;
	for (; i <= n && j <= n-l; i++, j++) {
		while (a[i] > b[j]) {
            j++;
        }
		if (n - l >= j) {
            cnt++;
        }
	}
    ans = n - l - cnt;
	return ans;
}

int main()
{
    //freopen("in.in", "r", stdin);
	//freopen("out.out", "w", stdout);
	int cases;
    scanf("%d", &cases);
    int n;
	for (int t = 1; t <= cases; t++) {

        int ans = 0, cnt = 0;

		scanf("%d", &n);

		for (int i = 1; i <= n; i++) {
            scanf("%lf", &a[i]);
        }

		for (int i = 1; i <= n; i++) {
            scanf("%lf", &b[i]);
        }

		sort(a + 1, a + n + 1);
		sort(b + 1, b + n + 1);

		ans = solve(0, n);
		cnt = deal(0, n);

		for (int i = 1; i <= n; i++) {
			if (b[n-i+1] > a[i]) {
                int tmp = deal(i, n);
                if(tmp > cnt) {
                    cnt = tmp;
                }
			}
        }

		printf("Case #%d: %d %d\n", t, cnt, ans);
	}
    return 0;
}
