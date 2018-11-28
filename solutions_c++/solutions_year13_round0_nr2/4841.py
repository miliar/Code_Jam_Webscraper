#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>

typedef std::vector<std::vector<int> > t_a;

bool atest(int x, int y, int dx, int dy, t_a& a) {
    int N = a.size(), M = a[0].size();
    int v = a[x][y], p = a[x][y];
    while (0 <= x && x < N && 0 <= y && y < M) {
        v = std::max(a[x][y], v);
        x += dx; y += dy;
    }
    return (p >= v);
}

bool test(int x, int y, int dx, int dy, t_a& a) {
    return (atest(x, y, -dx, -dy, a) && atest(x, y, dx, dy, a));
}

void solve(int caseid) {
    int N, M;
    std::cin >> N >> M;
    t_a a(N);
    for (int i = 0; i < N; i ++) {
        for (int j = 0; j < M; j ++) {
            int x; 
            std::cin >> x;
            a[i].push_back(x);
        }
    }

    bool ok = true;
    for (int i = 0; i < N; i ++)
        for (int j = 0; j < M; j ++) {
            if (!test(i, j, 1, 0, a) && !test(i, j, 0, 1, a)) {
                ok = false;
            }
        }

    std::printf("Case #%d: %s\n", caseid, (ok? "YES": "NO"));

}

int main() {
    int T;
    std::cin >> T;
    for (int i = 1; i <= T; i ++)
        solve(i);
} 

