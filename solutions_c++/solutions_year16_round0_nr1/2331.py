#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <queue>
#include <set>
#include <climits>
using namespace std;

typedef long long ll;
int testCase;

int state;
ll n;

void sol(ll num)
{
    while(num)
    {
        ll digit = num % 10;
        state |= (1 << digit);
        num /= 10;
    }
}

int main()
{
    //freopen("input.txt", "r", stdin);
    //freopen("codeGem#A.out", "w+", stdout);
    scanf("%d", &testCase);
    for(int tc = 1; tc <= testCase; tc++)
    {
        state = 0;
        ll mul = 0;
        scanf("%lld", &n);
        if(n == 0)
        {
            printf("Case #%d: INSOMNIA\n", tc);
            continue;
        }
        while(state != (1 << 10) -1)
            sol(n * (++mul));
        
        printf("Case #%d: %lld\n", tc, n * mul);
    }
}