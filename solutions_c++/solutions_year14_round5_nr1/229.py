#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    int T;
    cin >> T;
    cout.precision(16);
    cerr.precision(16);
    for (int testcase = 1; testcase <= T; ++testcase)
    {
        int N, p, q, r, s;
        cin >> N >> p >> q >> r >> s;
        vector<int> as(N);
        for (int i = 0; i < N; ++i)
            as[i] = (int)(((long)i * p + q) % r) + s;
        vector<long> sums(N + 1);
        sums[0] = 0;
        for (int i = 0; i < N; ++i)
            sums[i + 1] = sums[i] + as[i];
        long best = 0;
        for (int a = 0; a < N; ++a)
        {
            long left = sums[a];
            int b = lower_bound(sums.begin() + a, sums.end(), left + (sums[N] - left) / 2) - sums.begin();
            long middle = sums[b] - sums[a];
            long right = sums[N] - sums[b];
            long solveig = max(left, max(middle, right));
            best = max(best, sums[N] - solveig);
            if (b > a)
            {
                --b;
                middle = sums[b] - sums[a];
                right = sums[N] - sums[b];
                solveig = max(left, max(middle, right));
                best = max(best, sums[N] - solveig);
            }
        }
        cout << "Case #" << testcase << ": " << (double)best / sums[N] << "\n";
        cerr << "Case #" << testcase << ": " << (double)best / sums[N] << "\n";
    }
    return 0;
}
