#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <ctime>
#include <cmath>
#include <cassert>
#include <numeric>
#include <cstdlib>
#include <algorithm>
using namespace std;

#define N 1005
#define M 5200
#define ll long long
#define inf 0x7fffffff
#define lson (id<<1)
#define rson (id<<1|1)

#define eps 1e-6
#define pii pair<int,int>
#define pdd pair<double,int>
#define MP(i,j) make_pair(i,j)
#define It map<int,int>::iterator
#define X first
#define Y second

ll a[N], L, R;
void init();

int main() {
#ifndef ONLINE_JUDGE
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int cas, pcas = 1;
    init();
    scanf("%d", &cas);
    while (cas--) {
        scanf("%I64d%I64d", &L, &R);
        int ans = 0;
        for (int i = 1; i < 40; i++) {
            if (a[i] >= L && a[i] <= R)
                ans++;
        }
        printf("Case #%d: %d\n", pcas++, ans);
    }
    return 0;
}

void init() {
    a[0] = 0LL;
    a[1] = 1LL;
    a[2] = 4LL;
    a[3] = 9LL;
    a[4] = 121LL;
    a[5] = 484LL;
    a[6] = 10201LL;
    a[7] = 12321LL;
    a[8] = 14641LL;
    a[9] = 40804LL;
    a[10] = 44944LL;
    a[11] = 1002001LL;
    a[12] = 1234321LL;
    a[13] = 4008004LL;
    a[14] = 100020001LL;
    a[15] = 102030201LL;
    a[16] = 104060401LL;
    a[17] = 121242121LL;
    a[18] = 123454321LL;
    a[19] = 125686521LL;
    a[20] = 400080004LL;
    a[21] = 404090404LL;
    a[22] = 10000200001LL;
    a[23] = 10221412201LL;
    a[24] = 12102420121LL;
    a[25] = 12345654321LL;
    a[26] = 40000800004LL;
    a[27] = 1000002000001LL;
    a[28] = 1002003002001LL;
    a[29] = 1004006004001LL;
    a[30] = 1020304030201LL;
    a[31] = 1022325232201LL;
    a[32] = 1024348434201LL;
    a[33] = 1210024200121LL;
    a[34] = 1212225222121LL;
    a[35] = 1214428244121LL;
    a[36] = 1232346432321LL;
    a[37] = 1234567654321LL;
    a[38] = 4000008000004LL;
    a[39] = 4004009004004LL;
}