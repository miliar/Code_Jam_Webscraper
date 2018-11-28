#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

long long nice[39] = {1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944,
1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004,
404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201,
1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004};
#define R 38

int T;
long long a,b;

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    scanf("%d", &T);
    for(int t = 1; t <= T; t++)
    {
        scanf("%lld%lld", &a, &b);
        int l,r;
        for(l = 0; nice[l] < a && l <= R; l++);
        for(r = R; nice[r] > b && r >= 0; r--);
        int ans = r-l+1;
        if (ans < 0)
            ans = 0;
        printf("Case #%d: %d\n", t, ans);
    }

    return 0;
}
