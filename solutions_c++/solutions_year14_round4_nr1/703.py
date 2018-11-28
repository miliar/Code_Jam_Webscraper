#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>

using namespace std;


int T, n, cap;
int a[100008];
void work()
{
    int ans = 0;
    scanf("%d%d", &n, &cap);
    for (int i = 1; i <= n; i++) {
        scanf("%d", &a[i]);
    }
    sort(a + 1, a + 1 + n);
    int p1 = 1, p2 = n;
    while (p1 < p2) {
        if (a[p1] + a[p2] <= cap) {
            p1++; p2--;
        } else {
            p2--;
        }
        ans++;
    }
    if (p1 == p2) {
        ans++;
    }
	printf("%d\n", ans);
}
int main()
{
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		printf("Case #%d: ", i);
		work();
	}
}
