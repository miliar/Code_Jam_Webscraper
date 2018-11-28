#include <cstdio>
#include <cstring>
#include <cassert>
#include <queue>
#include <algorithm>

#define SIZE(v) (int)(v).size()

const int N = 2000;

int n, a[N], b[N], degree[N], answer[N], position[N + 1];
bool graph[N][N];

bool has_edge(int i, int j) {
    if (i < j) {
        return a[i] >= a[j];
    }
    if (j < i) {
        return b[j] <= b[i];
    }
    return false;
}

bool check() {
    for (int i = 0; i < n; ++ i) {
        int tmp = 1;
        for (int j = 0; j < i; ++ j) {
            if (answer[j] < answer[i]) {
                tmp = std::max(tmp, a[j] + 1);
            }
        }
        if (tmp != a[i]) {
            return false;
        }
    }
    for (int i = 0; i < n; ++ i) {
        int tmp = 1;
        for (int j = i + 1; j < n; ++ j) {
            if (answer[j] < answer[i]) {
                tmp = std::max(tmp, b[j] + 1);
            }
        }
        if (tmp != b[i]) {
            return false;
        }
    }
    return true;
}

int main() {
    int test_count;
    scanf("%d", &test_count);
    for (int t = 1; t <= test_count; ++ t) {
        scanf("%d", &n);
        for (int i = 0; i < n; ++ i) {
            scanf("%d", a + i);
        }
        for (int i = 0; i < n; ++ i) {
            scanf("%d", b + i);
        }
        for (int i = 0; i < n; ++ i) {
            for (int j = 0; j < n; ++ j) {
                graph[i][j] = has_edge(i, j);
            }
        }
        memset(position, -1, sizeof(position));
        for (int i = 0; i < n; ++ i) {
            if (a[i] > 1) {
                graph[i][position[a[i] - 1]] = true;
            }
            position[a[i]] = i;
        }
        memset(position, -1, sizeof(position));
        for (int i = n - 1; i >= 0; -- i) {
            if (b[i] > 1) {
                graph[i][position[b[i] - 1]] = true;
            }
            position[b[i]] = i;
        }
        memset(degree, 0, sizeof(degree));
        for (int i = 0; i < n; ++ i) {
            assert(!graph[i][i]);
        }
        for (int i = 0; i < n; ++ i) {
            for (int j = 0; j < n; ++ j) {
                if (graph[i][j]) {
//printf("%d->%d\n", i, j);
                    degree[j] ++;
                }
            }
        }
        std::priority_queue <int> queue;
        for (int i = 0; i < n; ++ i) {
            if (!degree[i]) {
                queue.push(i);
            }
        }
        int total = n;
        while (!queue.empty()) {
            int i = queue.top();
            queue.pop();
            answer[i] = total --;
            for (int j = 0; j < n; ++ j) {
                if (graph[i][j]) {
                    degree[j] --;
                    if (!degree[j]) {
                        queue.push(j);
                    }
                }
            }
        }
        //assert(check());
        printf("Case #%d:", t);
        for (int i = 0; i < n; ++ i) {
            printf(" %d", answer[i]);
        }
        puts("");
    }
    return 0;
}
