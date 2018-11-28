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

char str[105];
bool st[105];
int len;

void input()
{
    scanf("%s", str);
    len = strlen(str);
    for (int i = 0; i < len; ++i)
        st[i] = str[i]=='+' ? 1 : 0;
}

void turn(int from, int to)
{
    if (from > to) return;
    int mid = (from+to)>>1;
    for (int i = from; i <= mid; ++i)
        swap(st[i], st[from+to-i]);
    for (int i = from; i <= to; ++i)
        st[i] = !st[i];
}

void work()
{
    int ans = 0;
    int top = 0, bottom = len-1, t;
    while (top <= bottom)
    {
        while (st[bottom] == 1 && top <= bottom) bottom--;
        if (top > bottom) break;
        t = top;
        while (st[t] == 1 && t <= bottom) t++;
        if (t > top)
        {
            ans++;
            turn(top, t-1);
        }
        ans++;
        turn(top, bottom);
    }
    printf("%d\n", ans);
}

int main()
{
    //freopen("B-large.in", "r", stdin);
    //freopen("B-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int times = 1; times <= T; ++times)
    {
        input();
        printf("Case #%d: ", times);
        work();
    }
    return 0;
}
