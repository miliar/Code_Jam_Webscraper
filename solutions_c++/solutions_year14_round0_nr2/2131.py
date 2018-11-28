/*
ID: wuqi9395@126.com
PROG:
LANG: C++
*/
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<cmath>
#include<cstdio>
#include<vector>
#include<string>
#include<fstream>
#include<cstring>
#include<ctype.h>
#include<iostream>
#include<algorithm>
#define maxn 1000
#define INF (1<<30)
#define PI acos(-1.0)
#define mem(a, b) memset(a, b, sizeof(a))
#define For(i, n) for (int i = 0; i < n; i++)
typedef long long ll;
using namespace std;
double c, f, x, now;
double ans;
bool gao() {
    double t1 = x / now;
    double t2 = c / now + x / (now + f);
    if (t1 > t2) return true;
    return false;
}
int main ()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t, cnt = 1;
    scanf("%d", &t);
    while(t--) {
        now = 2.0;
        scanf("%lf%lf%lf", &c, &f, &x);
        ans = 0;
        while(gao()) {
            ans += c / now;
            now += f;
        }
        ans += x / now;
        printf("Case #%d: %.7f\n", cnt++, ans);
    }
    return 0;
}
