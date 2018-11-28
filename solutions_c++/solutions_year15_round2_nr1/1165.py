#include <iostream>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <cstring>
using namespace std;
#define MAX 1000009
#define ll int
void tabular();

ll fn(ll x);
ll reverse(ll x);
bool is_leading(ll x);
const ll inf = 9999999;
ll dp[MAX], x;
int cases, p = 1;

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("c.out", "w", stdout);
    //memset(dp, -1, sizeof(dp));
    tabular();
    scanf("%d", &cases);
    while(cases--)
    {
        scanf("%d", &x);
        printf("Case #%d: %d\n", p++, min(x, dp[x]));
    }


    return 0;
}

void tabular()
{
    dp[0] = 0;
    ll ret;
    for(ll i = 1; i <= 1000000; i++)
    {
        ret = dp[i - 1] + 1;
        ll tmp = reverse(i);

        if(!is_leading(i) && tmp < i)
            ret = min(ret, dp[tmp] + 1);

        dp[i] = ret;
    }
}


ll fn(ll x)
{
    if(x == 0)
        return 0;

    ll& ret = dp[x];
    if(ret != -1)
        return ret;
    ret = -1 * inf;

    ret = fn(x - 1) + 1;
    ll tmp = reverse(x);

    if(!is_leading(x) && tmp < x)
        ret = min(ret, fn(tmp) + 1);

    return ret;
}

ll reverse(ll x)
{
    ll ret = 0;

    while(x)
    {
        ret = ret * 10 + (x % 10);
        x = x / 10;
    }

    return ret;
}

bool is_leading(ll x)
{
    if(x % 10 == 0)
        return 1;
    else
        return 0;
}
