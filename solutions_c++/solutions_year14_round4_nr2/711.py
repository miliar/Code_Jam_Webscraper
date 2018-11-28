#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>

using namespace std;

#define rep( i, j, k ) for( i = j ; i <= k ; ++i )
#define drep( i, j, k ) for( i = j ; i >= k ; --i )

int T, n, m;
int a[10009];
int s[10008];
int calc1(int x)
{
	for (int i = 1; i <= n; i++) {
		if (a[i] < x) {
			return i;
		}
	}
}
int calc2(int x)
{
	for (int i = n; i; i--) {
		if (a[i] > x) {
			return i;
		}
	}
}
int deal1(int x, int cnt)
{
	for (int i = x, c = 1; c <= cnt; c++) {
		swap(a[x], a[x - 1]);
		x--;
	}
}
int deal2(int x, int cnt)
{
	for (int i = x, c = 1; c <= cnt; c++) {
		swap(a[x], a[x + 1]);
		x++;
	}
}
void work()
{
	int ans = 0, cnt, pos;
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) {
        scanf("%d", &a[i]);
		s[i] = a[i];
    }
	sort(s + 1, s + 1 + n);
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			if (s[i] == a[j]) {
				pos = j;
				break;
			}
		}
		int cnt1 = pos - calc1(a[pos]);
		int cnt2 = calc2(a[pos]) - pos;
		if (cnt1 >= cnt2) {
			deal1(pos, cnt1);
			ans += cnt1;
		} else {
			deal2(pos, cnt2);
			ans += cnt2;
		}
	}
	printf("%d\n", ans);
}
int main()
{
        freopen("B.in", "r", stdin);
        freopen("B2.out", "w", stdout);
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		printf("Case #%d: ", i);
		work();
	}
}
