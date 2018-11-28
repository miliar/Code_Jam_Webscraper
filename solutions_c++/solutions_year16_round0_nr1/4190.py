#include <cstdio>
#include <cstring>
#include <algorithm>
#include <climits>
#include <cctype>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;

const double pi = acos(-1.0);
const int inf = 0x7fffffff;
const int mod = 1e8 + 7;

bool h[15];

ll solve(ll n)
{
    memset(h,0,sizeof (h));
    for (int i = 1;i <= 1e6; ++ i)
    {
        ll temp = i * n;
        while (temp)
        {
            int a = temp % 10;
            temp /= 10;
            h[a] = 1;
        }
        bool flag = 1;
        for (int j = 0;j <= 9; ++ j)
            if (!h[j])
        {
            flag = 0;
            break;
        }
        if (flag)
            return i;
    }
    return -1;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out","w",stdout);
    int t,k = 1;
    scanf("%d",&t);
    while (t --)
    {
        ll n;
        scanf("%lld",&n);
        printf("Case #%d: ",k ++);
        if (!n)
            puts("INSOMNIA");
        else
        {
            ll res = solve(n);
            if (res == -1)
                puts("INSOMNIA");
            else
                printf("%lld\n",res * n);
        }


    }
    return 0;
}
