#include <stdio.h>
#include <map>
#include <string>
#include <vector>
#include <iostream>
#include <queue>

using namespace std;

int min_cost;

void dfs(map<int,int> count,int prev_cost) {
    int maxpan = count.rbegin()->first;
    int cnt = count.rbegin()->second;
//    cout << maxpan << ' ' << cnt <<  ' ' << prev_cost << endl;
    min_cost = min(prev_cost+maxpan, min_cost);
    if (maxpan <= 3) return ;

    count.erase(maxpan);
    for (int i = 1; i <= maxpan/2; ++i) {
        count[i] += cnt;
        count[maxpan-i] += cnt;
        dfs(count, prev_cost+cnt);
        count[i] -= cnt;
        count[maxpan-i] -= cnt;
        if (count[i] == 0) count.erase(i);
        if (count[maxpan-i] == 0) count.erase(maxpan-i);
    }
}
int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int ncase = 1; ncase <= t; ncase++) {
        int D;
        scanf ("%d", &D);
        map<int,int> count;
        while (D--) {
            int v;
            scanf("%d", &v);
            count[v]++;
//            q.push(v);
        }
        min_cost = count.rbegin()->first;
        dfs(count, 0);
        printf("Case #%d: %d\n", ncase, min_cost);
    }
    fclose(stdout);
}
