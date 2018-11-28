#include <iostream>
#include <algorithm>
#include <string.h>

using namespace std;

double DP[201][201];

int main()
{
    int T;
    cin >> T;
    for(int ca = 1; ca <= T; ++ca)
    {
        int N, K;
        cin >> N >> K;
        double INP[300];
        for(int i = 0; i < N; ++i)
            cin >> INP[i];
        sort(INP, INP + N);
        // DP[i][j], the prob. of i voted j "YES"
        double ret = 0.0;
        for(int k = 0; k <= K; ++k)
        {
            int tail = K-k;
            //cout << "#" << k << " " << tail << endl;
            double P[300];
            int idx = 0;
            for(int i = 0; i < k; ++i) P[idx++] = INP[i];
            for(int i = N-1; i >= N-tail; --i) P[idx++] = INP[i];
            //cout << "#" << idx << endl;
            memset(DP, 0, sizeof(DP));
            DP[0][0] = 1.0;
            for(int i = 0; i < K; ++i)
            {
                double p = P[i];
                for(int j = 0; j <= i; ++j)
                {
                    DP[i+1][j] += DP[i][j] * (1-p);
                    DP[i+1][j+1] += DP[i][j] * p;
                }
            }
            ret = max(ret, DP[K][K/2]);
        }
        cout.precision(15);
        cout << "Case #" << ca << ": " << fixed << ret << endl;
    }
}
