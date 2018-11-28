#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>
#include <bitset>
#include <map>
using namespace std;

bitset<20005> ex1, ex2;
vector<int> a[25];
int ans = 0, n, tot;

void dfs(int x) {
    if (ans <= (ex1 & ex2).count()) return ;
    if (x > n) {
        ans = (ex1 & ex2).count();
        return ;
    }
    bitset<20005> ex = ex1;
    for (int i = 0; i < a[x].size(); ++i)
        ex1.set(a[x][i]);
    dfs(x + 1);
    ex1 = ex;
    ex = ex2;
    for (int i = 0; i < a[x].size(); ++i)
        ex2.set(a[x][i]);
    dfs(x + 1);
    ex2 = ex;
}

int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int T;
    scanf("%d", &T);
    while (T--) {
        ex1.reset();
        ex2.reset();
        tot = 0;
        map<string, int> mark;
        scanf("%d", &n);
        for (int i = 1; i <= n; ++i) {
            char ch, str[25];
            a[i].clear();
            do {
                scanf("%s%c", str, &ch);
                int y;
                if (mark.count(str))
                    y = mark[str];
                else y = mark[str] = tot++;
                a[i].push_back(y);
            } while (ch != '\n');
        }
        ans = 1 << 30;
        for (int i = 0; i < a[1].size(); ++i)
            ex1.set(a[1][i]);
        for (int i = 0; i < a[2].size(); ++i)
            ex2.set(a[2][i]);
        dfs(3);
        static int ca = 0;
        printf("Case #%d: %d\n", ++ca, ans);
    }
    return 0;
}
