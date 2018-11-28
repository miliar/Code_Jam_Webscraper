#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <vector>
#include <string>
#define LL long long

using namespace std;

const int maxN = 1005;
char str[maxN];
char win[maxN<<1];

void work()
{
    int from, to, len;
    from = to = 1005;
    len = strlen(str);
    win[to] = str[0];
    for (int i = 1; i < len; ++i)
    {
        if (str[i] >= win[from]) win[--from] = str[i];
        else win[++to] = str[i];
    }
    for (int i = from; i <= to; ++i)
        printf("%c", win[i]);
    printf("\n");
}

int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int times = 1; times <= T; ++times)
    {
        scanf("%s", str);
        printf("Case #%d: ", times);
        work();
    }
    return 0;
}
