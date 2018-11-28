#include <iostream>
#include <vector>
#include <queue>
using namespace std;

long depth(long v, vector<vector<long>> &inv, vector<long> cycle) {
    long best = 0;
    for (auto u : inv[v]) {
        if (cycle[u]) continue;
        best = max(best, 1 + depth(u, inv, cycle));
    }
    return best;
}

int main() {
    long T, N;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> N;
        vector<long> bff(N);
        for (int i = 0; i < N; i++) cin >> bff[i];
        vector<vector<long>> inv(N);
        for (int i = 0; i < N; i++) bff[i]--, inv[bff[i]].push_back(i);

        vector<long> cycle(N);
        long single = 0;
        long multiple = 0;
        for (int i = 0; i < N; i++) {
            vector<long> visited(N);
            //cout << i << endl;
            //if (visited[i]) continue;
            //for (int i = 0; i < N; i++) cout << " " << visited[i]; cout << endl;
            long j = i;
            while (!visited[j]) visited[j] = 1, j = bff[j];
            if (cycle[j]) continue;
            long k = j;
            long len = 0;
            do cycle[k] = 1, len++, k = bff[k]; while (k != j);
            single = max(single, len);
            if (len != 2) continue;
            vector<long> depths;
            do {
                depths.push_back(depth(k, inv, cycle));
                k = bff[k];
            } while (k != j);
            long best_depth = 0;
            for (int i = 0; i < depths.size(); i++) {
                best_depth = max(best_depth, depths[i] + depths[(i+1)%depths.size()]);
            }
            multiple += len + best_depth;
        }

        cout << "Case #" << t << ": " << max(single, multiple) << endl;
    }
}
