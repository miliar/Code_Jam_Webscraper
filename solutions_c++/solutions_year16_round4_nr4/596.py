#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

int main() {
    long T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        long N;
        cin >> N;
        vector<string> can_op(N);
        for (int i = 0; i < N; i++) cin >> can_op[i];
        vector<vector<long>> op(N, vector<long>(N));
        long op_bit = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                op[i][j] = can_op[i][j] == '1';
                op_bit += op[i][j] << (N*i+j);
            }
        }
        int best = 1e9;
        for (long sol = 0; sol < (1 << (N*N)); sol++) {
            if ((sol & op_bit) != op_bit) continue;
            vector<long> rows(N);
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    rows[i] += !!(sol & (1 << (N*i+j))) << j;
                }
            }
            long good = 1;
            map<long, long> cnt;
            for (int i = 0; i < N; i++) cnt[rows[i]]++;
            for (int i = 0; i < N; i++) {
                if (cnt[rows[i]] != __builtin_popcount(rows[i])) good = 0;
            }
            long ored = 0;
            for (int i = 0; i < N; i++) ored |= rows[i];
            good &= ored == (1 << N) - 1;
            if (good) best = min(best, __builtin_popcount(sol) -
                                       __builtin_popcount(op_bit));
        }
        cout << "Case #" << t << ": " << best << endl;
    }
}
