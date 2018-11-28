#include "bits/stdc++.h"

using namespace std;

int n;

vector <vector <int> > cp;

bool check(const vector <int> &order,
    vector <bool> &used,
    int i) {
        if (i == n) {
            return true;
        }
        else {
            int allBad = 0;
            for (int j = 0; j < n; ++j) {
                if (cp[order[i]][j]) {
                    if (!used[j]) {
                        used[j] = true;
                        if (allBad == 0) {
                            allBad = 1;
                        }
                        if (allBad == 1) {
                            if (!check(order, used, i + 1)) {
                                return false;
                            }
                        }
                        used[j] = false;
                    }
                }
            }
            if (allBad != 1) {
                return false;
            }
            return true;
        }
}

bool check2() {
    vector <int> p(n);
    for (int i = 0; i < n; ++i) {
        p[i] = i;
    }
    do {
        vector <bool> used(n, false);
        if (!check(p, used, 0)) {
            return false;
        }
    } while (next_permutation(p.begin(), p.end()));
    return true;
}

int cost(int i, int curCost) {
    if (i == n * n) {
        if (check2()) {
            return curCost;
        }
        return INT_MAX / 2;
    }
    int x = i / n;
    int y = i % n;
    if (cp[x][y]) {
        return cost(i + 1, curCost);
    }
    int m1 = cost(i + 1, curCost);
    cp[x][y] = 1;
    int m2 = cost(i + 1, curCost + 1);
    cp[x][y] = 0;
    return min(m1, m2);
}

int main() {
    int T;
    scanf("%d", &T);
    for (int z = 1; z <= T; ++z) {
        printf("Case #%d: ", z);
        scanf("%d", &n);
        cp.assign(n, vector<int>(n, 0));
        for (int i = 0; i < n; ++i) {
            int x;
            scanf("%d", &x);
            for (int j = 0; j < n; ++j) {
                cp[i][j] = x % 10;
                x /= 10;
            }
        }

        int m = cost(0, 0);
        printf("%d\n", m);
    }
}
