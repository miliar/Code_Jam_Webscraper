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
#define maxn 1100
#define INF (1<<30)
#define PI acos(-1.0)
#define mem(a, b) memset(a, b, sizeof(a))
#define For(i, n) for (int i = 0; i < n; i++)
typedef long long ll;
using namespace std;
double a[maxn], b[maxn];
int n;
int main ()
{
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);
    int t, cnt = 1;
    scanf("%d", &t);
    while(t--) {
        scanf("%d", &n);
        for (int i = 0; i < n; i++) scanf("%lf", a + i);
        for (int i = 0; i < n; i++) scanf("%lf", b + i);
        sort(a, a + n);
        sort(b, b + n);
        int i = 0, j = 0, ans = 0, sum = 0;
        while(i < n && j < n) {
            if (b[j] > a[i]) {
                ans++;
                i++;
                j++;
            }
            else {
                j++;
            }
        }
        i = j = 0;
        while(i < n && j < n) {
            if (a[i] > b[j]) {
                sum++;
                i++;
                j++;
            }
            else {
                i++;
            }
        }
        printf("Case #%d: %d %d\n", cnt++, sum, n - ans);
    }
    return 0;
}
