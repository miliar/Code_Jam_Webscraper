#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <math.h>
#include <string.h>
using namespace std;

#define REP(i, n) for(int i=0;i<(n);i++)
#define FOR(i, j, k) for(int i=(j);i<=(k);i++)
#define mst(x, y) memset(x, y, sizeof(x))
#define pii pair<int, int>
#define fr first
#define sc second
#define seed 13331
#define mod (1e9+7)
#define ll long long
#define ull unsigned long long

static inline int Rint()
{
    struct X{ int dig[256]; X(){
    for(int i = '0'; i <= '9'; ++i) dig[i] = 1; dig['-'] = 1;
    }};
    static     X fuck;int s = 1, v = 0, c;
    for (;!fuck.dig[c = getchar()];);
    if (c == '-') s = 0; else if (fuck.dig[c]) v = c ^ 48;
    for (;fuck.dig[c = getchar()]; v = v * 10 + (c ^ 48));
    return s ? v : -v;
}

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int test;
    cin>>test;
    FOR(cas, 1, test){
        int n;
        char s[1111];
        scanf("%d", &n);
        scanf("%s", s);
        int ans = 0, cnt = 0;
        FOR(i, 0, n){
            int t = s[i] - '0';
            if(cnt < i){
                ans += (i-cnt);
                cnt += (i-cnt);
            };
            cnt += t;
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
