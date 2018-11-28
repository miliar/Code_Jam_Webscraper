#include<stdio.h>
#include <algorithm>
#include <cstring>
#include <queue>
#include <cmath>
#include <vector>
#include <iostream>
#include <map>
#include <stdlib.h>
using namespace std;
#define eps 1e-8
#define inf 0x7f7f7f7f
#define LL long long
#define MOD 1000000007
#define MAXN 20
#define MAXK 110
#include <string>
#include <queue>
#include <ctime>
int m, n;

LL  cnt, num;

int judge(LL x)
{
    LL t = x;
    LL tmp = 0;
    while(t)
    {
        tmp = 10 * tmp + t % 10;
        t /= 10;
    }
    if(x == tmp) return 1;
    return 0;
}

//int find(LL x)
//{
//    int l = 0, r = cnt;
//    while(l < r)
//    {
//        int m = l + (r - l) / 2;
//        if(pl[m] >= x) r = m;
//        else l = m + 1;
//    }
//    return l;
//}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    int cas = 0;
    num = 0;
LL pl[49] = {
    0,
    1,
    4,
    9,
    121,
    484,
    10201,
    12321,
    14641,
    40804,
    44944,
    1002001,
    1234321,
    4008004,
    100020001,
    102030201,
    104060401,
    121242121,
    123454321,
    125686521,
    400080004,
    404090404,
    10000200001LL,
    10221412201LL,
    12102420121LL,
    12345654321LL,
    40000800004LL,
    1000002000001LL,
    1002003002001LL,
    1004006004001LL,
    1020304030201LL,
    1022325232201LL,
    1024348434201LL,
    1210024200121LL,
    1212225222121LL,
    1214428244121LL,
    1232346432321LL,
    1234567654321LL,
    4000008000004LL,
    4004009004004LL,
    100000020000001LL,
    100220141022001LL,
    102012040210201LL,
    102234363432201LL,
    121000242000121LL,
    121242363242121LL,
    123212464212321LL,
    123456787654321LL,
    400000080000004LL,
};
    while(t--)
    {
        LL a, b;
        scanf("%I64d%I64d", &a, &b);
        LL ans = 0;
        for(int i = 0; i < 49; ++i)
        {
            if(pl[i] >= a && pl[i] <= b) ++ans;
        }
        printf("Case #%d: %I64d\n", ++cas, ans);
    }
    return 0;
}
