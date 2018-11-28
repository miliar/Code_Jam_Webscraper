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

const int maxn = 110;
const int nchar = 26;

    int _hash(char a) {
        return a - 'A';
    }
struct AC {
    int next[maxn][nchar];
    int cc;
    void init() {
        mem(next, 0);
        cc = 1;
    }
    void insert_trie(char *a) {
        int i = 0;
        int p = 0;
//        printf("%s\n", a);
        while(a[i]) {
            int index = _hash(a[i]);
//            printf("%d %d\n", index, next[p][index]);
            if(next[p][index] == 0) {
//                putchar('!');
//                printf("#%d\n", cc);
                next[p][index] = cc++;
            }
//            printf(".");
            p = next[p][index];
            i++;
        }
    }

    int getans() {
        return cc == 1 ? 0 : cc;
    }
} ac[9];

int n, m;
char str[109][109];

int cal(int a) {
//    putchar('(');
    int vis[109];
    for(int i = 0; i < n; i++) {
        vis[i] = a % m;
        a /= m;
    }
    for(int i = 0; i < m; i++) ac[i].init();
    for(int i = 0; i < n; i++) {
//    putchar('(');
//    printf("%d\n", vis[i]);
        ac[vis[i]].insert_trie(str[i]);
//    putchar(')');
    }
    int ret = 0;
    for(int i = 0; i < m; i++) {
        ret += ac[i].getans();
    }
//    putchar(')');
    return ret;
}

int MAIN() {
    scanf("%d%d", &n, &m);
    int up = 1;
    for(int i = 0; i < n; i++) {
        scanf("%s", str[i]);
        up *= m;
    }
    int maxcc = 0;
    for(int i = 0; i < up; i++) {
        int rt = cal(i);
        maxcc = max(maxcc, rt);
    }
    int ans2 = 0;
    for(int i = 0; i < up; i++) {
        int rt = cal(i);
        if(rt == maxcc) ans2++;
    }
    printf("%d %d\n", maxcc, ans2);
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
