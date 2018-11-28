
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#define MAXN 25

using namespace std;

int N;
string adj[MAXN];

int fact[] = {1, 1, 2, 6, 24};
vector <int> perm[5][5];

bool check() {
    vector <int> workers(N);
    for (int i = 0; i < N; i++)
        workers[i] = i;

    do {
        for (int ii = 0; ii < N; ii++) {
            int i = workers[ii];
            vector <int> machines;
            vector <vector <int>> block(ii);
            for (int k = 0; k < N; k++)
                if (adj[i][k] == '1') {
                    machines.push_back(k);
                    for (int jj = 0; jj < ii; jj++) {
                        int j = workers[jj];
                        if (adj[j][k] == '1')
                            block[jj].push_back(k);
                    }
                }
            if (machines.size() == 0)
                return false;

            if (ii == 1) {
                if (machines.size() == 1) {
                    for (int k : block[0])
                        if (k == machines[0])
                            return false;
                }
            }
            else if (ii == 2) {
                if (machines.size() <= 2) {
                    for (int i0 = 0; i0 < block[0].size(); i0++)
                        for (int i1 = 0; i1 < block[1].size(); i1++)
                            if (block[0][i0] != block[1][i1]) {
                                int m0 = block[0][i0];
                                int m1 = block[1][i1];
                                if (machines.size() == 1
                                        && (machines[0] == m0 || machines[0] == m1))
                                    return false;
                                if (machines.size() == 2
                                        && ((machines[0] == m0 && machines[1] == m1)
                                            || (machines[0] == m1 && machines[1] == m0)))
                                    return false;
                            }
                }
            }
            else if (ii == 3) {
                if (machines.size() <= 3) {
                    for (int i0 = 0; i0 < block[0].size(); i0++)
                        for (int i1 = 0; i1 < block[1].size(); i1++)
                            for (int i2 = 0; i2 < block[2].size(); i2++)
                            if (block[0][i0] != block[1][i1]
                                    && block[1][i1] != block[2][i2]
                                    && block[2][i2] != block[0][i0]) {
                                int m0 = block[0][i0];
                                int m1 = block[1][i1];
                                int m2 = block[2][i2];
                                if (machines.size() == 1
                                        && (machines[0] == m0 || machines[0] == m1 || machines[0] == m2))
                                    return false;
                                if (machines.size() == 2
                                        && ((machines[0] == m0 && machines[1] == m1)
                                            || (machines[0] == m1 && machines[1] == m0)
                                            || (machines[0] == m0 && machines[1] == m2)
                                            || (machines[0] == m2 && machines[1] == m0)
                                            || (machines[0] == m2 && machines[1] == m1)
                                            || (machines[0] == m1 && machines[1] == m2)))
                                    return false;
                                if (machines.size() == 3
                                        && ((machines[0] == m0 && machines[1] == m1 && machines[2] == m2)
                                            || (machines[0] == m0 && machines[1] == m2 && machines[2] == m1)
                                            || (machines[0] == m1 && machines[1] == m2 && machines[2] == m0)
                                            || (machines[0] == m1 && machines[1] == m0 && machines[2] == m2)
                                            || (machines[0] == m2 && machines[1] == m1 && machines[2] == m0)
                                            || (machines[0] == m2 && machines[1] == m0 && machines[2] == m1)))
                                    return false;
                            }
                }
            }
        }
    } while (next_permutation(workers.begin(), workers.end()));

    return true;
}

int solve_naive() {
    int min_cost = N * N;
    for (int mask = 0; mask < (1 << (N * N)); mask++) {
        bool to_check = true;
        vector <pair <int, int>> added;
        for (int k = 0; k < N * N; k++) {
            if ((mask & (1 << k)) == 0)
                continue;
            int i = k / N, j = k % N;
            if (adj[i][j] == '1') {
                to_check = false;
                break;
            }
            added.push_back({i, j});
        }
        if (!to_check)
            continue;
        for (auto p : added)
            adj[p.first][p.second] = '1';
        if (check()) {
            int cost = __builtin_popcount(mask);
            if (cost < min_cost)
                min_cost = cost;
        }
        for (auto p : added)
            adj[p.first][p.second] = '0';
    }
    return min_cost;
}

int solve() {
    return 0;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> N;
        for (int i = 0; i < N; i++)
            cin >> adj[i];
        cout << "Case #" << t << ": " << solve_naive() << endl;
        //cout << "Case #" << t << ": " << solve << endl;
    }
}
