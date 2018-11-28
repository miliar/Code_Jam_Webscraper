#include <iostream>
#include <vector>

using namespace std;

vector<double> dp(vector<double> answer) {
    int N = answer.size();
    vector<double> dp(2 * N + 7, 0), past(2 * N + 7, 0);
    dp[answer.size() + 2] = 1;
    for (int i = 0; i < N; ++i) {
        swap(dp, past);
        fill(dp.begin(), dp.end(), 0);
        for (int j = -i; j <= i; ++j) {
            dp[j + N - 1 + 2] += past[j + N + 2] * (1 - answer[i]);
            dp[j + N + 1 + 2] += past[j + N + 2] * answer[i];
        }
    }
    return dp;
}

int main() {
    int T; cin >> T;

    for (int test = 1; test <= T; ++test) {
        int N, K; cin >> N >> K;
        vector<double> P(N);
        for (int i = 0; i < N; ++i)
            cin >> P[i];
        vector<double> answer(P.begin(), P.begin() + K);
        for (int i = 0; i < (1 << N); ++i) {
            vector<double> aux;
            for (int j = 0; j < N; ++j)
                if ((1 << j) & i)
                    aux.push_back(P[j]);
            if (int(aux.size()) != K)
                continue;
            if (dp(answer)[K + 2] < dp(aux)[K + 2])
                answer = aux;
        }

        cout.setf(ios::fixed, ios::floatfield);
        cout.precision(10);
        cout << "Case #" << test << ": " << dp(answer)[answer.size() + 2] << "\n";
    }
}
