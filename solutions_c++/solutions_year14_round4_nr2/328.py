#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
#include <map>
#include <iostream>
#include <set>
#include <queue>
#include <stack>
#define zero(x) (((x)>0?(x):-(x))<eps)
//#include <bits/stdc++.h>
#define mem(a,b) memset((a),(b),sizeof((a)))
#define lld long long
#define INF 0x3f3f3f3f
#define eps 1e-6

using namespace std;

int n;
struct s{
    int val;
    int id;
    bool operator <(const s &I) const {
        return val < I.val;
    }
}num[10009];
int f[10009];

void update(int x) {
    while(x <= n) {
        f[x] ++;
        x += x&(-x);
    }
}

int getsum(int x) {
    int ret = 0;
    while(x) {
        ret += f[x];
        x -= x&(-x);
    }
    return ret;
}

int MAIN() {
    scanf("%d", &n);
    for(int i = 1; i <= n; i++) {
        scanf("%d", &num[i].val);
        num[i].id = i;
    }
    sort(num + 1, num + n + 1);
    mem(f, 0);
    int ans = 0;
    int l = 1;
    int r = n;
    for(int i = 1; i <= n; i++) {
//        int vl = num[i].id - l + getsum(n) - getsum(num[i].id);
//        int vr = r - num[i].id + getsum(num[i].id);
        int vl = 0;
        int vr = 0;
        for(int j = i + 1; j <= n; j++) {
            if(num[j].id < num[i].id) vl++;
            else vr++;
        }
//        printf("%d %d %d %d %d %d\n", num[i].val, num[i].id, l, r, vl, vr);
        if(vl <= vr) {
            l++;
            ans += vl;
        } else {
            r--;
            update(num[i].id);
            ans += vr;
        }
    }
    printf("%d\n", ans);
    return 0;
}

int main() {
#ifdef LOCAL_TEST
    freopen("F:/ACMData.txt","r",stdin);
    freopen("F:/out1.txt","w",stdout);
#endif
    int cases;
    scanf("%d", &cases);
    int cc = 1;
    while(cases--) {
        printf("Case #%d: ", cc++);
        MAIN();
    }
    return 0;
}
