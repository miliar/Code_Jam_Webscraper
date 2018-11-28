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
#include <algorithm>
using namespace std;

#define N 102
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

int n, m, r, k;
int a[10], b[10], c[10];

bool gan(int deep, int cur, int die) {
    if (deep == n)
        return cur == die;
    return gan(deep + 1, cur, die) || gan(deep + 1, cur * a[deep], die);
}

bool dfs(int deep) {
    if (deep == n) {
        bool mark = true;
        for (int i = 0; i < k; i++) {
            if (!gan(0, 1, c[i]))
                mark = false;
        }
        if (mark) {
            // printf("%d %d %d \n", a[0], a[1], a[2]);
            for (int i = 0; i < n; i++)
                b[i] = a[i];
        }
        return mark;
    }
    for (int i = 2; i <= m; i++) {
        a[deep] = i;
        if (dfs(deep + 1))
            return true;
    }
    return false;
}

int main() {
#ifndef ONLINE_JUDGE
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int cas, pcas = 1;
    scanf("%d", &cas);
    while (cas--) {
        scanf("%d%d%d%d", &r, &n, &m, &k);
        printf("Case #%d:\n", pcas++);
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < k; j++)
                scanf("%d", &c[j]);

            if (dfs(0)) {
                for (int j = 0; j < n; j++)
                    printf("%d", b[j]);
            } else {
                for (int j = 0; j < n; j++)
                    printf("%d", 2);
            }
            printf("\n");
        }
    }
    return 0;
}