#include <iostream>
#include <vector>
using namespace std;

int main() {

    int T;
    cin >> T;

    for (int tc = 1; tc <= T; tc++) {
        int E, R;
        int N;
        vector<int> values;

        cin >> E >> R >> N;
        values.resize(N);
        for (int i = 0; i < N; i++) {
            cin >> values[i];
        }

        vector<vector<int> > dp(N, vector<int>(E+1, 0));
        // dp[a][b] = max value if after doing activity #a, I have b remaining energy

        for (int spend = 0; spend <= E; spend++) {
            int gain = spend * values[0];
            int energy = min(E, E-spend+R);
            dp[0][energy] = gain;
        }

        for (int activity = 1; activity < N; activity++) {
            for (int oldEnergy = 0; oldEnergy <= E; oldEnergy++) {
                for (int spend = 0; spend <= oldEnergy; spend++) {
                    int gain = spend * values[activity];
                    int newTotalValue = dp[activity-1][oldEnergy] + gain;
                    int newEnergy = min(E, oldEnergy-spend+R);
                    dp[activity][newEnergy] = max(dp[activity][newEnergy], newTotalValue);
                }
            }
        }

        int ans = 0;
        for (int energy = 0; energy <= E; energy++) {
            ans = max(ans, dp[N-1][energy]);
        }
        cout << "Case #" << tc << ": " << ans << endl;
    }

    return 0;
}

