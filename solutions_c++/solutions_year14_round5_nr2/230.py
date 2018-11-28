#include <vector>
#include <algorithm>
#include <iostream>
#include <climits>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int testcase = 1; testcase <= T; ++testcase)
    {
        int P, Q, N;
        cin >> P >> Q >> N;
        vector<int> H(N);
        vector<int> G(N);
        for (int i = 0; i < N; ++i)
            cin >> H[i] >> G[i];
        vector<int> tab(1002, INT_MIN);
        tab[1] = 0;
        vector<int> prev(1002);
        for (int i = 0; i < N; ++i)
        {
            // cerr << "Monster #" << i << ":\n";
            swap(prev, tab);
            tab.assign(1002, INT_MIN);
            int towerTurns = (H[i] + Q - 1) / Q;
            for (int j = 0; j <= 1001; ++j)
            {
                if (prev[j] == INT_MIN)
                    continue;
                int jj = j + towerTurns;
                tab[jj] = max(tab[jj], prev[j]);
                // cerr << "  " << j << " (" << prev[j] << ") -> Give up -> " << jj << "\n";
            }
            if (prev[0] != INT_MIN && towerTurns > 1)
            {
                int point = H[i] - Q;
                for (int k = 0; ; ++k)
                {
                    int pts = point - k * (P + Q);
                    if (pts <= 0)
                        break;
                    if ((pts - 1) % Q < P)
                    {
                        int jj = (pts - 1) / Q;
                        tab[jj] = max(tab[jj], prev[0] + G[i]);
                        // cerr << "  0 (" << prev[0] << ") -> beat-behind(" << k << ") -> " << jj << "\n";
                        break;
                    }
                }
            }
            for (int j = 1; j <= 1001; ++j)
            {
                if (prev[j] == INT_MIN)
                    continue;
                if (j >= (H[i] + P - 1) / P)
                {
                    int jj = j - (H[i] + P - 1) / P;
                    tab[jj] = max(tab[jj], prev[j] + G[i]);
                    // cerr << "  " << j << " (" << prev[j] << ") -> beat-first2(" << l << ") -> " << jj << "\n";
                }
                bool found = false;
                for (int k = 0; ; ++k)
                {
                    int pts = H[i] - k * (P + Q);
                    if (pts <= 0)
                        break;
                    if ((pts - 1) % Q < P)
                    {
                        int jj = j + (pts - 1) / Q - 1;
                        tab[jj] = max(tab[jj], prev[j] + G[i]);
                        // cerr << "  " << j << " (" << prev[j] << ") -> beat-first1(" << k << ") -> " << jj << "\n";
                        found = true;
                        break;
                    }
                }
                if (found)
                    continue;
                for (int l = 1; l <= min(j, (H[i] - 1) / P); ++l)
                {
                    int pts = H[i] - l * P;
                    if ((pts - 1) % (P + Q) >= Q)
                    {
                        int jj = j - l;
                        tab[jj] = max(tab[jj], prev[j] + G[i]);
                        // cerr << "  " << j << " (" << prev[j] << ") -> beat-first2(" << l << ") -> " << jj << "\n";
                        break;
                    }
                }
            }
        }
        int ans = *max_element(tab.begin(), tab.end());
        cout << "Case #" << testcase << ": " << ans << "\n";
        cerr << "Case #" << testcase << ": " << ans << "\n";
    }
    return 0;
}
