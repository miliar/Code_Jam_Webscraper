/*************************************************************************
	> File Name: ga.cpp
	> Author: skt
	> Mail: sktsxy@gmail.com 
	> Created Time: 2014年05月31日 星期六 21时59分31秒
 ************************************************************************/

#include <bits/stdc++.h>
using namespace std;
#define MAXN 10005
int t, Cas = 1, n, x, a[MAXN], pos;
void work()
{
    printf("Case #%d: ", Cas ++);
    scanf("%d %d", &n, &x);
    for (int i = 1; i <= n; i ++) {
        scanf("%d", &a[i]);
    }
    sort(a+1, a+1+n);
    pos = 0;
    for (int i = n; i >= 1; i --) {
        if (a[i] * 2 <= x) {
            pos = i;
            break;
        }
    }
    int now = pos + 1, ans = 0, di = 0;
    for (int i = pos; i >= 1; i --) {
        if (now > n) {
            di += i;
            break;
        }
        if (a[i] + a[now] <= x) {
            ans ++;
            now ++;
        } else {
            di ++;
        }
    }
    ans += (n - now + 1);
    ans += (di % 2) ? (di / 2 + 1) : (di / 2);
    cout << ans << endl;
}
int main()
{
 //   freopen("in", "r", stdin);
    scanf("%d", &t);
    while (t --) {
        work();
    }
	return 0;
}
