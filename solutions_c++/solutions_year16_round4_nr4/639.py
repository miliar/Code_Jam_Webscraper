#include <iostream>
#include <vector>

using namespace std;

int main() {
    int T; cin >> T;

    for (int test = 1; test <= T; ++test) {
        int N; cin >> N;
        vector<int> numbers(N, 0);
        int orig = 0;
        for (int i = 0; i < N; ++i) {
            string S; cin >> S;
            for (int j = 0; j < N; ++j)
                if (S[j] == '1') {
                    numbers[i] += (1 << j);
                    ++orig;
                }
        }
        bool ok;
        do {
            ok = false;
            for (int i = 0; i < N; ++i)
                for (int j = 0; j < N; ++j)
                    if (numbers[i] & numbers[j])
                        if ((numbers[i] | numbers[j]) != numbers[i]) {
                            numbers[i] |= numbers[j];
                            ok = true;
                        }
        } while (ok);

        // Now join em
        vector<pair<int, int> > parts;
        int machines = 0;
        for (int i = 0; i < N; ++i) {
            bool same = false;
            for (int j = 0; j < i; ++j)
                if (numbers[i] == numbers[j])
                    same = true;
            if (same)
                continue;
            int count = 0, bits = 0;
            for (int j = 0; j < N; ++j) {
                if ((1 << j) & numbers[i])
                    ++bits;
                if (numbers[j] == numbers[i])
                    ++count;
            }

            if (bits > 0) {
                parts.emplace_back(count, bits);
                machines += bits;
            }
        }

        int dumbs = count(numbers.begin(), numbers.end(), 0);

        if (dumbs == N) {
            cout << "Case #" << test << ": " << N << "\n";
            continue;
        }

        int M = parts.size();
        vector<vector<int>> dp(N + 1, vector<int>(1 << M, numeric_limits<int>::max() / 2));
        dp[0][0] = 0;
        for (int i = 1; i <= N; ++i)
            dp[i][0] = i;

        for (int i = 1; i < (1 << M); ++i) {
            int totalCount = 0, totalBits = 0;
            for (int j = 0; j < M; ++j)
                if ((1 << j) & i) {
                    totalCount += parts[j].first;
                    totalBits += parts[j].second;
                }

            for (int j = i; j > 0 ; j = (j - 1) & j) {
                int auxCount = 0, auxBits = 0;
                for (int k = 0; k < M; ++k)
                    if ((1 << k) & j) {
                        auxCount += parts[k].first;
                        auxBits += parts[k].second;
                    }
                int oldPart = max(totalCount - auxCount, totalBits - auxBits);
                int newPart = max(auxCount, auxBits);
                for (int k = oldPart; k + newPart <= N; ++k)
                    for (int l = 0; k + newPart + l <= N; ++l)
                        dp[k + newPart + l][i] = min(dp[k + newPart + l][i], dp[k][i - j] + (newPart + l) * (newPart + l));
            }
        }
        cout << "Case #" << test << ": " << dp[N].back() - orig << "\n";
    }
}
