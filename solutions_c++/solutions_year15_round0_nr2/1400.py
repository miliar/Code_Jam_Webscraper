#include <cstdio>
#include <algorithm>
#include <iostream>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <cstring>
using namespace std;

#define N 1005
#define MII map<int, int>
#define ITER_MII map<int, int>::iterator

int cache[N][N];
void init_cache(int n, int m) {
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= m; j++) {
            cache[i][j] = -1;
        }
    }
}

int dfs(int p, int size) {
    if (p <= size)
        return 0;
    if (cache[p][size] != -1)
        return cache[p][size];

    if (p % size != 0)
        return cache[p][size] = 1 + dfs(p - p % size, size);
    else {
        int count = p / size;
        if (count % 2 == 0)
            return cache[p][size] = 1 + 2 * dfs(count / 2 * size, size);
        else
            return cache[p][size] = 1 + dfs(p - size, size);
    }
}

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int kase, n, answer;
    int a[N], max;
    scanf("%d", &kase);

    for (int kase_no = 1; kase_no <= kase; kase_no++) {
        scanf("%d", &n);
        answer = 0x7fffffff;
        max = 0;

        for (int i = 0; i < n; i++) {
            scanf("%d", &a[i]);
            if (a[i] > max)
                max = a[i];
        }
        init_cache(max, max);

        for (int size = 1; size <= max; size++) {
            int count = size;
            for (int i = 0; i < n; i++) {
                count += dfs(a[i], size);
            }
            if (count < answer)
                answer = count;
        }
        printf("Case #%d: %d\n", kase_no, answer);
    }
    return 0;
}
