#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>

using namespace std;


int T, n, m;
int a[10009];
int s[10008];
void build()
{
	scanf("%d%d%d", &W, &H, &B);
	for (int k = 1; k <= B; k++) {
		scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
		for (int i = x1 + 1; i <= x2 + 1; i++) {
			for (int j = y1 + 1; j <= y2 + 1; j++) {
				fobid[i][j] = true;
			}
		}
	}
	st = W * H + 1;
	ed = st + 1;
	for (int i = 1; i <= n; i++) {
		add(st, cood())
	}
}
void work()
{
	build();
	printf("%d\n", ans);
}
int main()
{
    //    freopen("B.in", "r", stdin);
    //    freopen("B.out", "w", stdout);
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		printf("Case #%d: ", i);
		work();
	}
}
