#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <queue>
#include <stack>
#include <cmath>
using namespace std;
#define INF 0x3f3f3f3f
typedef long long ll;
int kase;
char str[1555], ans[5000];
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &kase);
    for (int cas=1; cas<=kase; cas++) {
        memset(str, 0, sizeof(str));
        memset(ans, 0, sizeof(ans));
        scanf("%s", str);
        int mid=2000, low=2000, high=2000;
        ans[mid]=str[0];
        int len=strlen(str);
        for (int i=1; i<len; i++)
            if (str[i]>=ans[low])
                ans[--low]=str[i];
            else
                ans[++high]=str[i];
        printf("Case #%d: ", cas);
        for (int i=low; i<=high; i++)
            printf("%c", ans[i]);
        puts("");
    }
    return 0;
}
